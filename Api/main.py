import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routers.login import login_router
from routers.register import register_router



app = FastAPI()
origins = [
    "http://localhost:8000",
    "localhost:8000",
    "https://localhost:8000",
    "127.0.0.1:8000",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(login_router)
app.include_router(register_router)



@app.get('/')
def get_root():
    return 'JobUtopia'


# for debugging purposes
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)