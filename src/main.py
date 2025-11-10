from fastapi import FastAPI


app = FastAPI()

call_count = 0



@app.get("/")
def root():
    global call_count
    call_count += 1
    return {"Hello": "World"}

@app.get("/called_count")
def called_count():
    return {"called_count": call_count}

def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
