# 📡 Monitor de Rede 

Um sistema moderno e eficiente para monitoramento de dispositivos de rede em tempo real, com dashboard web e notificações nativas do Windows.

## 🚀 Funcionalidades

- **Monitoramento em Tempo Real**: Verifica a conectividade de múltiplos hosts simultaneamente via ping.
- **Organização por Áreas**: Agrupe seus dispositivos por categorias (ex: Servidores, Portais, Roteadores).
- **Dashboard Web Moderno**: Interface responsiva com tema escuro (Dark Mode) inspirada no design moderno.
- **Uptime Dinâmico**: Contador de tempo de inatividade (OFF) atualizado segundo a segundo no navegador.
- **Notificações do Windows**: Alertas visuais e sonoros via `winotify` quando um dispositivo muda de status.
- **Lógica Anti-Falso Positivo**: O sistema só altera o status após 2 falhas ou 2 sucessos consecutivos.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.11+ com [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: HTML5, CSS3 e JavaScript (Vanilla)
- **Notificações**: [winotify](https://pypi.org/project/winotify/)
- **Servidor**: [Uvicorn](https://www.uvicorn.org/)

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- [Python 3.11 ou superior](https://www.python.org/downloads/)
- Sistema Operacional Windows (para as notificações nativas)

## 🔧 Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/DomTobias/Monitoramento-de-Rede.git
   cd monitoramento-de-rede
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install fastapi uvicorn[standard] winotify
   ```

## ⚙️ Configuração

Edite o arquivo `hosts.json` na raiz do projeto para adicionar os dispositivos que deseja monitorar:

```json
[
    {
        "area": "Servidores",
        "hosts": [
            {"nome": "Servidor Principal", "ip": "192.168.1.10"},
            {"nome": "Backup", "ip": "192.168.1.11"}
        ]
    },
    {
        "area": "Portais",
        "hosts": [
            {"nome": "Intranet", "ip": "10.0.0.5"}
        ]
    }
]
```

## 🏃 Execução

Para iniciar o monitoramento e o servidor web, execute:

```bash
python main.py
```

Após iniciar, acesse o dashboard em seu navegador:
👉 **[http://localhost:8000](http://localhost:8000)**

## 📂 Estrutura do Projeto

- `main.py`: Servidor FastAPI e lógica de monitoramento em background.
- `index.html`: Interface do usuário (Frontend).
- `notificacao.py`: Integração com o sistema de notificações do Windows.
- `hosts.json`: Arquivo de configuração dos dispositivos.
- `requirements.txt`: Lista de bibliotecas necessárias.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido para facilitar a gestão de infraestrutura de rede. 🐨📡
