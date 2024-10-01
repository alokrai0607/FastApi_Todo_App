from fastapi import FastAPI
from app.controllers import todo_controller
from app.config import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(todo_controller.router)

app.add_middleware(
    CORSMiddleware, ##Cross-Origin Resource Sharing
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#  .\venv\Scripts\Activate

#  .\venv\Scripts\uvicorn app.main:app --reload