from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def testing_api():
    try:
        return {"Message": "Ok"}
    except Exception as e:
        return {"Message":print(e)}
        