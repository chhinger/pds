#from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI" }


#@app.get("/items/{item_id}") # get is a request method  
#def read_item(item_id: int, q: Union[str, None] = None):
    """
    

    """

    return {"item_id": item_id, "q": q}