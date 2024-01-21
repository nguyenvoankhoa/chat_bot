from fastapi import FastAPI
from pydantic import BaseModel
from Utils import chat_bot

app = FastAPI()


class Data(BaseModel):
    question: str
    answer: str | None


@app.post("/request")
def post_question(data: Data):
    answer = chat_bot(data)
    return answer

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
