from fastapi import FastAPI, HTTPException

app = FastAPI()
db = {"accounts": [],  "posts": []}


@app.get("/")
async def root():
    return {"message": "This is the C4C Backend Workshop Backend!"}

# ********************************** ACCOUNTS **********************************************


@app.get("/accounts")
@app.post("/accounts")
def add_account():


@app.delete("/accounts/{id}")
def delete_account(account_id):
    accounts = db['accounts']
    for account in accounts:
        if account_id == account['id']:
            db['accounts'].remove(account)
    raise HTTPException(status_code=404, detail="Item not found")


# ********************************** SPECIFIC ACCOUNT **********************************************

@app.get("/accounts/{id}")
def get_account(account_id):
    accounts = db['accounts']
    for account in accounts:
        if account_id == account['id']:
            return account
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/accounts/{id}")
# ********************************** POSTS **********************************************
@app.get("/posts")
# EXERCISE
@app.put("/posts")
@app.delete("posts")
