from fastapi import FastAPI
from pydantic import BaseModel

from app.agent.agent import NoLLMAgent


app = FastAPI(
    title="LangChain No-LLM Agent",
    version="1.0.0"
)

agent = NoLLMAgent()


class AgentRequest(BaseModel):
    input: str


class AgentResponse(BaseModel):
    output: str


@app.get("/readiness")
def health():
    return {
        "status": "healthy",
        "agent": "langchain-no-llm-agent"
    }


@app.post("/invocations", response_model=AgentResponse)
def invoke(request: AgentRequest):

    result = agent.invoke(request.input)

    return AgentResponse(
        output=result
    )