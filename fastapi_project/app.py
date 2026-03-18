from fastapi import FastAPI
from starlette.templating import Jinja2Templates as Jinja2Templates  # noqa

SET_NUMBER = 0

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.post("/action/{run}")
# async def perform_action(run: int):
#     # Simulate performing an action based on the 'run' parameter
#     result = f"Action performed for run {run}"
#     return {"result": result}

@app.get("/template")
async def render_template():
    templates = Jinja2Templates(directory="./fastapi_project/templates/")
    return templates.TemplateResponse("index.html", context={
            "request":{}, 
            "content":SET_NUMBER
        })

@app.post("/set_number/{number}")
async def set_number(number: int):
    global SET_NUMBER
    SET_NUMBER = number
    print(f"Number set to {SET_NUMBER}")
    return {"message": f"Number set to {SET_NUMBER}"}

@app.get("/get_number")
async def get_number():
    return {"number": SET_NUMBER}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)