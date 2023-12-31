import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

from routers.login import login_router
from routers.register import register_router
from routers.search import search_router, search_company_router, search_professional_router, search_admin_router
from routers.admin import  admin_router
from routers.companies import companies_router
from routers.professionals import professionals_router
from routers.messages import messages_router
from routers.generator import generator_router
from routers.user import users_router


app = FastAPI()
origins = [
    "http://localhost",
    "https://localhost",
    "127.0.0.1",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://localhost:80",
    "localhost:80",
    "https://localhost:80",
    "127.0.0.1:80",
    "http://127.0.0.1:80",
    "https://127.0.0.1:80",
    "https://jobutopia.vercel.app/",
    "http://jobutopia.vercel.app/",
    "https://jobutopia.vercel.app",
    "http://jobutopia.vercel.app",
    "https://jobutopia.vercel.app:80",
    "http://jobutopia.vercel.app:80",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex="http?://jobutopia.vercel.app.*",
)

app.include_router(login_router)
app.include_router(register_router)
app.include_router(search_router)
app.include_router(admin_router)
app.include_router(companies_router)
app.include_router(professionals_router)
app.include_router(search_professional_router)
app.include_router(search_company_router)
app.include_router(search_admin_router)
app.include_router(messages_router)
app.include_router(generator_router)
app.include_router(users_router)


@app.get('/')
def get_root():
    return 'JobUtopia'


# for debugging purposes
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload



# prof_token -> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcl9pZCI6MywiZGVmYXVsdF9vZmZlcl9pZCI6MiwiZmlyc3RfbmFtZSI6Ik1pY2hhZWwiLCJsYXN0X25hbWUiOiJMaXZpbmdzdG9uIiwic3VtbWFyeSI6IkV4cGVyaWVuY2VkIFB5dGhvbiBkZXZlbG9wZXIiLCJhZGRyZXNzIjoiVWJiby1FbW11bnNsYWFuIHN0ci4sIEFtc3RlcmRhbSwgTkUiLCJzdGF0dXMiOiJhY3RpdmUiLCJ1c2VybmFtZSI6InRlc3R1c2VyMiIsImFwcHJvdmVkIjp0cnVlLCJpc3N1ZWQiOiIyMDIzLTEyLTA3IDEzOjUzOjA2LjQzNTMzMSIsInVzZXJfdHlwZSI6IlByb2Zlc3Npb25hbCJ9.dL1dMoZbk_6kTWA0N5Hser0ZGBF_EhBpB2iUsJmkJiY


# comp_token -> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcl9pZCI6NSwibmFtZSI6IlBlcHNpIiwiZGVzY3JpcHRpb24iOiJXZSBtYWtlIHRoZSBmaXp6eSBkcmluayIsImFkZHJlc3MiOiJMb3MgQW5nZWxlcywgQ2FsaWZvcm5pYSIsInBpY3R1cmUiOm51bGwsInVzZXJuYW1lIjoidGVzdHVzZXI0IiwiYXBwcm92ZWQiOnRydWUsImlzc3VlZCI6IjIwMjMtMTItMDEgMDk6Mzc6MTguNDQ5MTgwIn0.Y4NLeAWHC92LmzDfv3H8hlLjFpd4XbvI8mr22-xvFV0


