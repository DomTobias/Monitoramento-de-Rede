import time
import json
import os
import platform
import subprocess
import threading
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from notificacao import notificacao_on, notificacao_off

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estado global do monitoramento
monitor_data = []
# status_history armazena o estado de cada host por IP
status_history = {} 

def testar_ping(ip):
    is_windows = platform.system().lower() == "windows"
    param_count = "-n" if is_windows else "-c"
    param_timeout = "-w" if is_windows else "-W"
    timeout_val = "1000" if is_windows else "1"
    
    comando = ["ping", param_count, "1", param_timeout, timeout_val, ip]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return resultado.returncode == 0
    except:
        return False

def carregar_hosts():
    caminho = "hosts.json"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def background_monitor():
    global monitor_data
    while True:
        areas = carregar_hosts()
        new_data = []
        
        for area_item in areas:
            area_name = area_item["area"]
            hosts_list = area_item["hosts"]
            updated_hosts = []
            
            for host in hosts_list:
                ip = host["ip"]
                nome = host["nome"]
                
                if ip not in status_history:
                    status_history[ip] = {
                        "estado": "Verificando", 
                        "inicio_off": None, 
                        "falhas": 0, 
                        "sucessos": 0
                    }
                
                conectado = testar_ping(ip)
                hist = status_history[ip]
                
                if conectado:
                    hist["sucessos"] += 1
                    hist["falhas"] = 0
                    # Transição para ON após 2 sucessos
                    if hist["sucessos"] >= 2 and hist["estado"] != "ON":
                        if hist["estado"] == "OFF":
                            notificacao_on(nome, ip)
                        hist["estado"] = "ON"
                        hist["inicio_off"] = None
                else:
                    hist["falhas"] += 1
                    hist["sucessos"] = 0
                    # Transição para OFF após 2 falhas
                    if hist["falhas"] >= 2 and hist["estado"] != "OFF":
                        hist["estado"] = "OFF"
                        hist["inicio_off"] = time.time() # Timestamp para o front calcular
                        notificacao_off(nome, ip)
                
                updated_hosts.append({
                    "nome": nome,
                    "ip": ip,
                    "status": hist["estado"],
                    "inicio_off": hist["inicio_off"] # Enviamos o timestamp bruto
                })
            
            new_data.append({
                "area": area_name,
                "hosts": updated_hosts
            })
        
        monitor_data = new_data
        time.sleep(2) # Frequência de checagem

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=background_monitor, daemon=True)
    thread.start()

@app.get("/api/status")
def get_status():
    return monitor_data

@app.get("/")
def read_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
