﻿# Arquivo principal do agente de IA
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}

@app.get("/run-agent/")
def run_agent():
    return {"message": "Agente de IA em execução!"}
