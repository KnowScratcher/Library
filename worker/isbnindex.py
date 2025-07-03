from dependencies import *
import os
import json

async def refreshAll():
    """refreshes all isbn index in `isbn.json`"""
    data = {}
    for i in os.listdir(locationPath): # i is the location (file)
        with open(os.path.join(locationPath,i),"r",encoding="utf-8") as f:
            jsn:dict = json.load(f)
        i = i[:-5]
        for j in jsn: # j is the isbn
            data[j] = i
    with open(isbnIndexPath,"w",encoding="utf-8") as f:
        json.dump(data,f)

async def set(isbn,location):
    """sets a index to `isbn.json`"""
    isbnIndex[isbn] = location
    with open(isbnIndexPath,"w",encoding="utf-8") as f:
        json.dump(isbnIndex,f)
    return True