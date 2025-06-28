from dependencies import *
import os
import json

async def add(location:str,id:str,isbn:str,name:str) -> bool:
    """add a book to a collection using id

    Args:
        location (str): collection id
        id (str): the id of the book
        isbn (str): the isbn of the book
        name (str): the name of the book

    Returns:
        bool: always `True` if run successfully
    """
    with open(os.path.join(locationPath,location+".json"),"r+",encoding="utf-8") as f:
        data = json.load(f)
        data[id] = {"name":name,"ISBN":isbn,"isHere":True}
        f.seek(0)
        json.dump(data,f)
        f.truncate()
    return True