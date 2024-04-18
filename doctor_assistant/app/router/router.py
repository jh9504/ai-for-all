from doctor_assistant.app.database import get_db
from doctor_assistant.app.main import app
from requests import Request


@app.post("/create_content")
def create_content(request: Request):
    id = request.id
    db = get_db()

    print(id)
