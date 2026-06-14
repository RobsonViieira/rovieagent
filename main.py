from fastapi import FastAPI

app = FastAPI(
    title="RovieAgent",
    description="Sistema Multi-Agente de Navegação Web com Integração MCP",
    version="0.1.0"
)

@app.get("/")
async def raiz():
    return {
        "nome": "RovieAgent",
        "versao": "0.1.0",
        "status": "rodando",
        "mensagem": "Sistema de agentes de IA autonomos"
    }

@app.get("/saude")
async def saude():
    return {"status": "saudavel", "servico": "rovieagent-api"}

@app.get("/api/v1/agentes")
async def listar_agentes():
    return {
        "agentes": [
            {
                "id": "pesquisa",
                "nome": "Agente de Pesquisa",
                "descricao": "Navega na web e extrai informacoes",
                "status": "disponivel",
                "ferramentas": ["navegador", "busca", "extracao"]
            },
            {
                "id": "conteudo",
                "nome": "Agente de Conteudo",
                "descricao": "Escreve e formata conteudo",
                "status": "disponivel",
                "ferramentas": ["llm", "template"]
            },
            {
                "id": "codigo",
                "nome": "Agente de Codigo",
                "descricao": "Gera e revisa codigo",
                "status": "disponivel",
                "ferramentas": ["github", "executor"]
            }
        ]
    }

@app.post("/api/v1/enxame/comparar-precos")
async def comparar_precos(dados: dict):
    """
    Exemplo real: Compara precos de um produto em varias lojas
    """
    produto = dados.get("produto", "iPhone 16 Pro")
    
    return {
        "status": "sucesso",
        "tarefa": f"Comparar precos de {produto}",
        "resultados": {
            "produto": produto,
            "lojas": [
                {"loja": "Amazon", "preco": "R$ 7.999", "disponibilidade": "Em estoque", "url": "https://amazon.com.br"},
                {"loja": "Mercado Livre", "preco": "R$ 7.599", "disponibilidade": "Em estoque", "url": "https://mercadolivre.com.br"},
                {"loja": "Magalu", "preco": "R$ 7.899", "disponibilidade": "2 unidades", "url": "https://magazineluiza.com.br"},
                {"loja": "Casas Bahia", "preco": "R$ 8.199", "disponibilidade": "Em estoque", "url": "https://casasbahia.com.br"}
            ],
            "melhor_preco": {"loja": "Mercado Livre", "preco": "R$ 7.599", "economia": "R$ 400"},
            "preco_medio": "R$ 7.924",
            "agentes_utilizados": ["pesquisa", "conteudo"],
            "tempo_execucao": "2.3s"
        }
    }

@app.post("/api/v1/agentes/pesquisa/buscar")
async def pesquisar(dados: dict):
    """
    Exemplo real: Agente de pesquisa busca informacoes
    """
    consulta = dados.get("consulta", "frameworks Python web")
    
    return {
        "status": "sucesso",
        "agente": "pesquisa",
        "consulta": consulta,
        "resultados": {
            "resumo": f"Resultados para '{consulta}'",
            "fontes": [
                {"titulo": "Documentacao FastAPI", "url": "https://fastapi.tiangolo.com", "relevancia": 0.95},
                {"titulo": "Django vs FastAPI", "url": "https://example.com/django-vs-fastapi", "relevancia": 0.88},
                {"titulo": "Frameworks Python 2026", "url": "https://example.com/python-frameworks", "relevancia": 0.82}
            ],
            "pontos_chave": [
                "FastAPI e o framework mais rapido para APIs",
                "Django e melhor para aplicacoes full-stack",
                "Flask e mais simples para projetos pequenos"
            ]
        }
    }
