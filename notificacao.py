from winotify import Notification

def notificacao_on(nome, ip):
    try:
        n_on = Notification(
            app_id="Monitor de Rede",
            title=f"{nome} ONLINE",
            msg=f"{nome} ({ip}) está conectado",
            duration="short",
            icon=r"C:\Users\Gabriel Tobias\Desktop\ADS\monitoramento\icons\antenna_on.png",
            launch="http://localhost:8000"
        )
        n_on.show()
    except Exception as e:
        print(f"Erro ao enviar notificação ON: {e}")

def notificacao_off(nome, ip):
    try:
        n_off = Notification(
            app_id="Monitor de Rede",
            title=f"{nome} OFFLINE",
            msg=f"{nome} ({ip}) está desconectado",
            duration="short",
            icon=r"C:\Users\Gabriel Tobias\Desktop\ADS\monitoramento\icons\antenna_off.png",
            launch="https://localhost:8000"
        )
        n_off.show()
    except Exception as e:
        print(f"Erro ao enviar notificação OFF: {e}")
