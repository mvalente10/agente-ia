from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando! Vá para /docs para ver a documentação"}

@app.get("/run-agent")
def run_agent():
    return {"message": "Agente de IA em execução!"}

@app.post("/run-agent")
async def run_agent_post(request: Request):
    try:
        data = await request.json()
        input_text = data.get("input", "Nenhuma entrada fornecida")
        return {"message": f"Agente processou o input: {input_text}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
