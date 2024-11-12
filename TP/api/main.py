from fastapi import FASTAPI  
app = FastAPI()

@app.get(path="/")
async def root():
    return{"message":"Hello, World"}