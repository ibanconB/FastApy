from http.client import HTTPException
from random import randrange

from fastapi import FastAPI, HTTPException
from PydanticModels.models import PostParams

app = FastAPI()

# Base de datos simulada de posts, cada uno incluye un "id" para hacer posible la búsqueda por id
my_posts = [
    {
        "id": 1,
        "title": "Introducción a FastAPI",
        "content": "FastAPI es un framework web moderno y rápido para construir APIs con Python...",
        "published": "2024-10-31"
    },
    {
        "id": 2,
        "title": "Beneficios de Pydantic",
        "content": "Pydantic permite la validación de datos en Python de una forma sencilla y eficiente...",
        "published": "2024-10-30"
    },
    {
        "id": 3,
        "title": "Creación de APIs RESTful",
        "content": "Aprender a construir APIs RESTful es esencial para desarrolladores backend...",
        "published": "2024-10-29"
    }
]

# Función para encontrar un post por ID y devolver el índice
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
    return None

# Endpoint para obtener todos los posts
@app.get("/posts")
def get_all_posts():
    return {"data": my_posts}

# Endpoint para obtener un post por ID
@app.get("/posts/{id}")
def get_post(id: int):
    post = next((p for p in my_posts if p["id"] == id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post_detail": post}

# Endpoint para crear un nuevo post
@app.post("/posts", status_code=201)
def create_post(new_post: PostParams):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 10000)  # Genera un ID único
    my_posts.append(post_dict)
    return {"data": post_dict}

# Endpoint para eliminar un post por ID
@app.delete("/posts/{id}", status_code=204)
def delete_post(id: int):
    index = find_post_index(id)
    if index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    deleted_post = my_posts.pop(index)
    return {"message": f"Post with id {id} deleted", "post": deleted_post}
