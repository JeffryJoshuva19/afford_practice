from fastapi import FastAPI;

app=FastAPI()

@app.get("/hello")
def getpage():
    return {"hello everyone how are you"}

