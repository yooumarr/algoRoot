from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from rag import retrieve_function
from code_gen import generate_code
from functions import functions

app = FastAPI()

class ExecutionRequest(BaseModel):
    prompt: str
    arguments: Dict = None

class ExecutionResponse(BaseModel):
    function: str
    code: str

session_memory = {}

@app.post("/execute", response_model=ExecutionResponse)
async def execute_function(request: ExecutionRequest):
    prompt = request.prompt

    if "session_id" in request.arguments and request.arguments["session_id"] in session_memory:
        full_prompt = session_memory[request.arguments["session_id"]] + " " + prompt
    else:
        full_prompt = prompt

    function_name = retrieve_function(full_prompt)

    if not function_name:
        raise HTTPException(status_code=404, detail="Function not found.")

    code = generate_code(function_name, request.arguments)

    if "session_id" in request.arguments:
        if request.arguments["session_id"] not in session_memory:
            session_memory[request.arguments["session_id"]] = ""
        session_memory[request.arguments["session_id"]] = full_prompt

    return ExecutionResponse(function=function_name, code=code)