from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def entry():
    return {"Hello": "Optimized", "Version": "1.0.0"}
