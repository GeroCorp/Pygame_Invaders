from settings import *
from functions import *
import json
import os


listaScores = [{'username':"a",'score':15},
               {'username':"b",'score':21},
               {'username':"c",'score':18},
               {'username':"h",'score':27},
               {'username':"r",'score':30},
               {'username':"n",'score':50},
               {'username':"p",'score':9},
               {'username':"w",'score':10},
               {'username':"d",'score':14}
               ]


def mostrarDatos(lista:list)->None:
    """Muestra tabla de datos de una lista

    Args:
        lista (list): Lista con datos de los posts
    """
    print(f"{'User':<10} {'Score':<8}")
    print(f"===============================")
    for user in lista:
        print(f" {user['username']:<10} {user['score']:<8}")

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

def loadBestScores (thisFile):
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



def saveBestScores (thisFile:str, user):

    if validateFile(thisFile):
        print("s")
        previusScores = loadBestScores(thisFile)
        
        print(previusScores)
        with open(getActualPath(thisFile), 'w', encoding='utf-8') as file:
            newList = []

            # if len(previusScores) >1:
            keys = ','.join(list(previusScores[0].keys())) + '\n'
            file.write(keys)
            # else:
            #     keys = ','.join(previusScores[0]) + '\n'
            #     file.write(keys)

            
            # for user in scoreList:
            newList.append(user)
            for score in previusScores:
                # if user["score"] > score["score"]:
                #     newList.append(user)
                # else:
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
    

    
user ={
    "username": "Gero",
    "score": 100
}

