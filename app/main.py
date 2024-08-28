from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# Set up Jinja2 environment
templates = Environment(loader=FileSystemLoader("app/templates"))

@app.get("/", response_class=HTMLResponse)
async def read_calculator(request: Request):
    return templates.get_template("calculator.html").render()

@app.get("/calculate")
async def calculate(request: Request, a: float, b: float, operation: str):
    result = None
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b != 0:
            result = a / b
        else:
            result = "Error: Division by zero"
    return {"result": result}
