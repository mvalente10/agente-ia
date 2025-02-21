from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "API está funcionando! Vá para /docs para ver a documentação"}

# Endpoint GET para o agente de IA
@app.get("/run-agent")
def run_agent():
    return {"message": "Agente de IA em execução!"}

# Endpoint POST para o agente de IA
@app.post("/run-agent")
async def run_agent_post(request: Request):
    try:
        data = await request.json()
        input_text = data.get("input", "Nenhuma entrada fornecida")
        return {"message": f"Agente processou o input: {input_text}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Outros endpoints existentes
@app.post("/generate_code/")
async def generate_code(request: Request):
    return {"message": "Código gerado com sucesso!"}

@app.post("/create_github_repo/")
async def create_github_repo(request: Request):
    return {"message": "Repositório do GitHub criado com sucesso!"}

@app.post("/push_code_to_github/")
async def push_code_to_github(request: Request):
    return {"message": "Código enviado para o GitHub com sucesso!"}
