from fastapi import FastAPI

app = FastAPI()



@app.on_event("startup")
def startup_event():
    database.create_tables()


@app.get("/")
def health():
    return "Hello World"
