from dependencies import *
import os
import json

async def checkValid(id:str, name:str) -> bool:
    """check if a collection duplicates

    Args:
        id (str): the id of the collection
        name (str): the display name of the collection

    Returns:
        bool: `True`: won't be duplicate, `False`: will be duplicate
    """
    lni = list(collectionNameIndex.items())
    i = [x[0] for x in lni]
    n = [x[1] for x in lni]
    return not (id in list(i) or name in list(n))

async def registerLocation(id:str,name:str) -> bool:
    """register a collection

    Args:
        id (str): the id of the collection
        name (str): the display name of the collection

    Returns:
        bool: whether it succeed
    """
    if not await checkValid(id,name):
        return False
    collectionNameIndex[id] = name
    with open(collectionNameIndexPath,"w",encoding="utf-8") as f:
        json.dump(collectionNameIndex,f)
    with open(os.path.join(locationPath,id+".json"),"w",encoding="utf-8") as f:
        json.dump({},f)
    return True