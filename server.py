from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

next_post_id: int = 0
app = FastAPI()
db = {"posts": []}

class Post(BaseModel):
    title: str
    body: str

@app.get("/")
async def root():
    return {"message": "This is the C4C Backend Workshop Backend!"}

# Returns all posts
@app.get("/posts")
def get_posts():
    return db['posts']

# Creates a new entry for Post
# Will raise exception if body parameters are invalid
@app.post("/posts")
def add_post(new_post: Post):
    if (new_post.title.strip() == '' or new_post.body.strip() == ''):
        raise HTTPException(status_code=400, detail="Invalid input")
    else:
        global next_post_id
        id = next_post_id
        db['posts'].append({ 'id': id, 'title': new_post.title, 'body': new_post.body })
        next_post_id += 1
        return id

# Removes a post from the 'database'
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    posts = db['posts']
    for post in posts:
        if post_id == post['id']:
            db['posts'].remove(post)
            return 'OK'
    raise HTTPException(status_code=404, detail="Item not found")

# Retrieves a single post from the 'database'
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    posts = db['posts']
    for post in posts:
        if post_id == post['id']:
            return post
    raise HTTPException(status_code=404, detail="Item not found")

# Exercises
# Updates a post in the 'database'
@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post):
    pass

# Deletes all posts from the 'database'
@app.delete("/posts")
def delete_all_posts():
    pass