from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Example endpoint with path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# Example endpoint with query parameter
@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
