# import modules
import os
import json

with open("params.json", "r") as f:
    params = json.load(f)

path = params["path"]
recupPath = params["recupPath"]
showCorrupt = params["showCorrupt"]
maxIndent = params["maxIndent"]

# get the indent of the path
def getIndent(path: str):
    return len(path.split("/")) - 2

indentPath = getIndent(path)

print('--------------------')

# loop to get all files
num = 0
empty = 0
def directory(path: str):
    global num, empty

    indentNum = getIndent(path) - indentPath
    tab = "    " * (indentNum)
    for file in os.listdir(path):
        num += 1

        # set the color
        color = ""
        if os.stat(path + file).st_size == 0:
            empty += 1
            color = '\033[91m'

            if not showCorrupt:
                continue

        endline = ""
        if color:
            endline = '\033[0m'

        if indentNum <= maxIndent:
            print(color + tab + file + endline)

        if os.path.isdir(path + file):
            directory(path + file + "/")


directory(path)

print('--------------------')

print("Results :")
print(f"Empty files : {round(empty/num*100, 2)}% - {empty} / {num} files")