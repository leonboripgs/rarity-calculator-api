from fastapi import FastAPI
from getRarity import GetRarity

app = FastAPI()

@app.get("/{id}")
def read_root(id):
    obj = GetRarity(id)
    res = obj.calculateRarity()
    return({"rarity" : float("{0:.2f}".format(res))})