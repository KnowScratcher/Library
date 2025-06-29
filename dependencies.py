import os
import json

basePath = os.path.dirname(__file__)
"""`directory`: top directory"""
dataPath = os.path.join(basePath, "data")
"""`directory`: top > data directory"""
locationPath = os.path.join(dataPath, "locations")
"""`directory`: top > data > locations directory"""
isbnIndexPath = os.path.join(dataPath, "isbn.json")
"""`file`: top > data > isbn.json"""
collectionNameIndexPath = os.path.join(dataPath, "name.json")
"""`file`: top > data > name.json"""
# bookNameIndexPath = os.path.join(dataPath, "bookName.json")
# """`file`: top > data > bookName.json"""
isbnIndex: dict = {}
"""`cache`: top > data > isbn.json"""
collectionNameIndex: dict = {}
"""`cache`: top > data > name.json"""
# bookNameIndex: dict = {}
# """`cache`: top > data > bookName.json"""

if not os.path.exists(dataPath):  # create data directory
    os.makedirs(dataPath)
if not os.path.exists(isbnIndexPath):  # create index file
    json.dump({}, open(isbnIndexPath, "w", encoding="UTF-8"))
if not os.path.exists(collectionNameIndexPath):  # create name file
    json.dump({}, open(collectionNameIndexPath, "w", encoding="UTF-8"))
# if not os.path.exists(bookNameIndexPath):  # create name file
#     json.dump({}, open(bookNameIndexPath, "w", encoding="UTF-8"))
if not os.path.exists(locationPath):  # create locations directory
    os.makedirs(locationPath)

with open(isbnIndexPath, "r", encoding="UTF-8") as i:  # read ISBN index
    isbnIndex: dict = json.load(i)

with open(collectionNameIndexPath, "r", encoding="UTF-8") as i:  # read ISBN index
    collectionNameIndex: dict = json.load(i)

# with open(bookNameIndexPath, "r", encoding="UTF-8") as i:  # read ISBN index
#     bookNameIndex: dict = json.load(i)


async def getBasePath():
    return basePath


async def getDataPath():
    return dataPath


async def getIndexPath():
    return isbnIndexPath


async def getISBNindex():
    return isbnIndex


async def getCollectionNameIndex():
    return collectionNameIndex


# async def getBookNameIndex():
#     return bookNameIndex


async def writeISBNindex(data: dict):
    global isbnIndex
    isbnIndex = data


async def refreshIndex():
    global isbnIndex
    with open(isbnIndexPath, "r", encoding="UTF-8") as i:  # read ISBN index
        isbnIndex = json.load(i)
