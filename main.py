from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    user_id: int

@app.post("/recommend")
def recommend(data: UserInput):

    uid = data.user_id

    if uid % 4 == 1:
        products = ["Mobile", "Laptop", "Power Bank"]
    elif uid % 4 == 2:
        products = ["Shoes", "T-Shirt", "Jeans"]
    elif uid % 4 == 3:
        products = ["Books", "Notebook", "Pen"]
    else:
        products = ["Headphones", "Smart Watch", "Bluetooth Speaker"]

    return {
        "user_id": uid,
        "recommendations": products
    }
