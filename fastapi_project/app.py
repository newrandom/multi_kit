from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.templating import Jinja2Templates as Jinja2Templates  # noqa

SET_NUMBER = 0

app = FastAPI()


class NumberPayload(BaseModel):
    number: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/template")
async def render_template(request: Request):
    templates = Jinja2Templates(directory="./fastapi_project/templates/")
    return templates.TemplateResponse("index.html", context={
            "request": request,
            "content":SET_NUMBER
        })

@app.post("/set_number/")
async def set_number(payload: NumberPayload):
    global SET_NUMBER
    SET_NUMBER = payload.number
    print(f"Number set to {SET_NUMBER}")
    return {"message": f"Number set to {SET_NUMBER}"}

@app.get("/get_number")
async def get_number():
    return {"number": SET_NUMBER}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)