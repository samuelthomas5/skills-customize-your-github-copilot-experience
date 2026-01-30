"""
FastAPI REST API Starter Code
Complete this assignment by building out the endpoints and implementing the requirements.
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="My REST API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define a Pydantic model for your main data object
# Example: A model for a User, Product, Task, etc.
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create a simple in-memory data store
# Example: items = []


# TODO: Implement a GET endpoint to retrieve all items
# @app.get("/items", response_model=List[Item])
# async def get_all_items():
#     pass


# TODO: Implement a GET endpoint to retrieve a single item by ID
# @app.get("/items/{item_id}", response_model=Item)
# async def get_item(item_id: int):
#     pass


# TODO: Implement a POST endpoint to create a new item
# @app.post("/items", response_model=Item, status_code=201)
# async def create_item(item: Item):
#     pass


# TODO: Implement a PUT endpoint to update an existing item
# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: Item):
#     pass


# TODO: Implement a DELETE endpoint to remove an item
# @app.delete("/items/{item_id}", status_code=204)
# async def delete_item(item_id: int):
#     pass


# Optional: Add a root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI REST API"}


if __name__ == "__main__":
    import uvicorn
    # Run with: python starter-code.py
    # API will be available at: http://localhost:8000
    # API docs available at: http://localhost:8000/docs
    uvicorn.run(app, host="0.0.0.0", port=8000)
