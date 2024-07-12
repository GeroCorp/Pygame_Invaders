from settings import *
from functions import *
import json
import os

def swap(list:list,i:int,j:int):
    """Swapea elementos de una lista

    Args:
        list (list): Lista a swapear
        i (int): Primer indice
        j (int): Segundo indice
    """
    aux=list[i]                
    list[i]=list[j]
    list[j]=aux
  
def removeDup(lista: list)->list:
    """Removes the duplicated items in a list

    Args:
        lista (list): List to filter

    Returns:
        list: Filtered list
    """
    inList = set()
    newList = []
    for item in lista:
        if type(item) == dict:
            strItem = json.dumps(item, sort_keys=True)
            print(strItem)

            if strItem not in inList:
                newList.append(item)
                inList.add(strItem)

        else:
            if item not in inList:
                newList.append(item)
                inList.add(item)

    return newList

def validateFile(fileToValidate):
    """Verifies csv file existence. Creates one if not founded.

    Args:
        fileToValidate (path): CSV file path

    Returns:
        bool: returns file existence
    """
    temp = False
    try:
        with open(getActualPath(fileToValidate), 'r', encoding="utf-8") as file:
                temp= file.read()
    except:
        print("File doesn't exist.\nCreating one...")
    if not temp:
        with open(getActualPath(fileToValidate), 'w', encoding='utf-8') as file:
            file.write("username,score")
        temp= True
    else:
        temp = True
    return temp

def loadBestScores (thisFile) -> list:
    """Loads data from a CSV file

    Args:
        thisFile (path): CSV file path

    Returns:
        list: Returns the file's data in a list
    """
    newList = []
    if validateFile(thisFile):
        with open(getActualPath(thisFile), 'r', encoding="utf-8") as file:
            keys = file.readline().strip('\n').split(",")

            for u in file.readlines():
                user = {}
                u = u.strip('\n').split(',')
                username,score = u
                user["username"] = username
                user["score"] = int(score)

                newList.append(user)
            
            if len(newList) == 0:
                user = {}
                user["username"] = "Gero"
                user["score"] = 10
                newList.append(user)

    return newList

def saveBestScores (thisFile, user):
    """Saves the user data in a CSV file

    Args:
        thisFile (path): File's path
        user (dict): User dictionary with data to save
    """
    if validateFile(thisFile):
        print("s")
        previusScores = loadBestScores(thisFile)
        
        print(previusScores)
        with open(getActualPath(thisFile), 'w', encoding='utf-8') as file:
            newList = []

            keys = ','.join(list(previusScores[0].keys())) + '\n'
            file.write(keys)


            newList.append(user)
            for score in previusScores:
                newList.append(score)

            newList=removeDup(newList)
            for i in range(len(newList)-1):
                for j in range(i + 1 , len(newList)):
                    if newList[i]['score'] < newList[j]['score']:
                        swap(newList , i , j)

            for user in newList:
                dataList= []

                print("a")
                values = list(user.values())
                for value in values:
                    if isinstance(value,int):
                        dataList.append(str(value))
                    else:
                        dataList.append(value)
                    print(dataList)
                line = ','.join(dataList) + '\n'
                file.write(line)

def saveLastScore(thisFile, user):
    """Saves user scores sorted by last entered

    Args:
        thisFile (path): _description_
        user (_type_): _description_
    """
    filePath = getActualPath(thisFile)
    if os.path.exists(filePath):
        with open(filePath, 'r', encoding="utf-8") as file:
            try:
                data =json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    
    data.insert(0,user)

    with open(filePath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    
def loadLastestScore (thisFile):
    """Loads scores from json sorted by last score

    Args:
        thisFile (path): File's path

    Returns:
        list: List with user's data
    """
    filePath = getActualPath(thisFile)
    if os.path.exists(filePath):
        with open(filePath, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    return data

