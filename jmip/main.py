from fastapi import FastAPI

#the API routes
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Market API Running"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Welcome to the page"}

@app.get("/job/job1")
def job1():
    return {"message": "Description of job 1"}