# RovieAgent

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.137+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![AWS](https://img.shields.io/badge/AWS-Deployed-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Multi-Agent Browser Swarm with MCP Integration** — Autonomous AI agents that navigate the web simultaneously, communicate via Model Context Protocol, and form a collective intelligence to solve complex tasks.

## Live Demo

- **API URL**: http://18.226.28.204:8000/
- **Docs**: http://18.226.28.204:8000/docs

## Features

- **Browser Swarm** — Multiple agents navigate the web simultaneously
- **MCP Integration** — Model Context Protocol for tool connectivity
- **Persistent Memory** — Agents learn and evolve over time
- **Visual Orchestrator** — Drag-and-drop agent workflows

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Python 3.12 |
| **AI Agents** | CrewAI + Browser Use |
| **MCP** | Model Context Protocol |
| **Deploy** | AWS EC2 |

## Installation

```bash
git clone https://github.com/RobsonViieira/rovieagent.git
cd rovieagent
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

uvicorn main:app --host 0.0.0.0 --port 8000

cat > README.md << 'EOF'
# RovieAgent

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.137+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![AWS](https://img.shields.io/badge/AWS-Deployed-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Multi-Agent Browser Swarm with MCP Integration — Autonomous AI agents that navigate the web simultaneously, communicate via Model Context Protocol, and form a collective intelligence to solve complex tasks.

## Live Demo

- **API URL**: http://18.226.28.204:8000/
- **Docs**: http://18.226.28.204:8000/docs

## Features

- **Browser Swarm** — Multiple agents navigate the web simultaneously
- **MCP Integration** — Model Context Protocol for tool connectivity
- **Persistent Memory** — Agents learn and evolve over time
- **Visual Orchestrator** — Drag-and-drop agent workflows

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Python 3.12 |
| **AI Agents** | CrewAI + Browser Use |
| **MCP** | Model Context Protocol |
| **Deploy** | AWS EC2 |

## Installation

```bash
git clone https://github.com/RobsonViieira/rovieagent.git
cd rovieagent
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.17.0-1010-aws x86_64)
 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
 System information as of Sun Jun 14 17:17:46 UTC 2026
  System load:  0.0                Temperature:           -273.1 C
  Usage of /:   26.8% of 28.02GB   Processes:             118
  Memory usage: 44%                Users logged in:       0
  Swap usage:   0%                 IPv4 address for ens5: 172.31.11.146
 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.
   https://ubuntu.com/aws/pro
Expanded Security Maintenance for Applications is not enabled.
27 updates can be applied immediately.
To see these additional updates run: apt list --upgradable
10 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm
*** System restart required ***
Last login: Sun Jun 14 17:08:52 2026 from 187.74.102.223
ubuntu@ip-172-31-11-146:~$ cd ~ && rm -rf nexusagent && mkdir nexusagent && cd nexusagent
ubuntu@ip-172-31-11-146:~/nexusagent$ cat > main.py << 'PYEOF'
from fastapi import FastAPI
app = FastAPI(title="NexusAgent", version="0.1.0")
@app.get("/")
async def root():
    return {"name": "NexusAgent", "version": "0.1.0", "status": "running"}
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.get("/api/v1/agents")
async def agents():
    return {"agents": [
        {"id": "research", "name": "Research Agent", "status": "available"},
        {"id": "content", "name": "Content Agent", "status": "available"},
        {"id": "code", "name": "Code Agent", "status": "available"}
    ]}
PYEOF
ubuntu@ip-172-31-11-146:~/nexusagent$ python3 -m venv venv && source venv/bin/activate && pip install fastapi uvicorn
Collecting fastapi
  Using cached fastapi-0.137.0-py3-none-any.whl.metadata (26 kB)
Collecting uvicorn
  Using cached uvicorn-0.49.0-py3-none-any.whl.metadata (6.7 kB)
Collecting starlette>=0.46.0 (from fastapi)
  Using cached starlette-1.3.1-py3-none-any.whl.metadata (6.4 kB)
Collecting pydantic>=2.9.0 (from fastapi)
  Using cached pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
Collecting typing-extensions>=4.8.0 (from fastapi)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.2 (from fastapi)
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi)
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting click>=7.0 (from uvicorn)
  Using cached click-8.4.1-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.9.0->fastapi)
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.4 (from pydantic>=2.9.0->fastapi)
  Using cached pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Collecting anyio<5,>=3.6.2 (from starlette>=0.46.0->fastapi)
  Using cached anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting idna>=2.8 (from anyio<5,>=3.6.2->starlette>=0.46.0->fastapi)
  Using cached idna-3.18-py3-none-any.whl.metadata (6.1 kB)
Using cached fastapi-0.137.0-py3-none-any.whl (121 kB)
Using cached uvicorn-0.49.0-py3-none-any.whl (71 kB)
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached click-8.4.1-py3-none-any.whl (116 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached pydantic-2.13.4-py3-none-any.whl (472 kB)
Using cached pydantic_core-2.46.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Using cached starlette-1.3.1-py3-none-any.whl (73 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached anyio-4.13.0-py3-none-any.whl (114 kB)
Using cached idna-3.18-py3-none-any.whl (65 kB)
Installing collected packages: typing-extensions, idna, h11, click, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, anyio, starlette, pydantic, fastapi
Successfully installed annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.13.0 click-8.4.1 fastapi-0.137.0 h11-0.16.0 idna-3.18 pydantic-2.13.4 pydantic-core-2.46.4 starlette-1.3.1 typing-extensions-4.15.0 typing-inspection-0.4.2 uvicorn-0.49.0
(venv) ubuntu@ip-172-31-11-146:~/nexusagent$ sudo fuser -k 8000/tcp 2>/dev/null
|| echo "Porta liberada"
(venv) ubuntu@ip-172-31-11-146:~/nexusagent$ uvicorn main:app --host 0.0.0.0 --port 8000
INFO:     Started server process [616762]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     187.74.102.223:39928 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     187.74.102.223:39928 - "GET / HTTP/1.1" 200 OK
cat > README.md << 'EOF'
# NexusAgent 🤖🌐
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.137+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![AWS](https://img.shields.io/badge/AWS-Deployed-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
> **Multi-Agent Browser Swarm with MCP Integration** — Autonomous AI agents that navigate the web simultaneously, communicate via Model Context Protocol, and form a collective intelligence to solve complex tasks.
## 🚀 Live Demo
🔗 **API URL**: http://18.226.28.204:8000/
📚 **Docs**: http://18.226.28.204:8000/docs
## ✨  Features
- 🌐 **Browser Swarm** — Multiple agents navigate the web simultaneously
- 🔗 **MCP Integration** — Model Context Protocol for tool connectivity
- 🧠 **Persistent Memory** — Agents learn and evolve over time
- 📊 **Visual Orchestrator** — Drag-and-drop agent workflows
## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Python 3.12 |
| **AI Agents** | CrewAI + Browser Use |
| **MCP** | Model Context Protocol |
| **Deploy** | AWS EC2 |
## 📦 Installation
```bash
git clone https://github.com/seu-usuario/nexusagent.git
cd nexusagent
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
cat > .gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.env
