import json
from os import system

answer = 0

with open("./src/todolist.json", mode="r", encoding="utf-8") as jsonFile:
    lists = json.load(jsonFile)

def writeChanges():
    with open("./src/todolist.json", mode="w", encoding="utf-8") as jsonFile:
        json.dump(lists, jsonFile)

def DeletarLista(selectedList):
    lists.remove(selectedList)

def Remover(selectedList):
    answer = int(input("Qual item deseja remover?: "))
    if (answer >= len(selectedList["items"])):
        quit(0)
    selectedList["items"].pop(answer)


def Adicionar(selectedList):
    newItem = input("Didite o texto do seu novo item: ")
    selectedList["items"].append({"text": newItem, "checked": False})


def Marcar(selectedList):
    answer = int(input("Qual item deseja marcar?: "))
    if (answer >= len(selectedList["items"])):
        quit(0)
    selectedList["items"][answer]["checked"] = True

def Desmarcar(selectedList):
    answer = int(input("Qual item deseja desmarcar?: "))
    if (answer >= len(selectedList["items"])):
        quit(0)
    selectedList["items"][answer]["checked"] = False


handleOptions = [Adicionar, Remover, Marcar, Desmarcar, DeletarLista]


def handleList(index: int):
    selectedList = lists[index]
    while True:
        global answer

        system("cls")

        for index, item in enumerate(selectedList["items"]):
            marker = ''
            if (item["checked"]):
                marker = '✅'
            else:
                marker = '❌'
            print(index, '-', item["text"] + ": " + marker)

        print("\nO que você deseja fazer?")

        for index, item in enumerate(handleOptions):
            print(index, '-', item.__name__)

        print("Digite qualquer outro número que não seja equivalente à uma das opções acima para sair.")

        answer = int(input("-> "))

        if (answer >= len(handleOptions)):
            break
        handleOptions[answer](selectedList)



def AdicionarLista():
    name = input("Digite o nome de sua lista: ")
    lists.append({"name": name, "items": [{"text": "Item de exemplo", "checked": True}]})

def GerenciarLista():
    global answer
    for index, item in enumerate(lists):
        print(index, '-', item["name"])
    answer = int(input("\nEscolha uma lista para gerenciar: "))
    if (answer >= len(lists)):
        quit(0)
    handleList(answer)


mainOptions = [AdicionarLista, GerenciarLista]

def main():
    while True:
        for index, item in enumerate(mainOptions):
            print(index, '-', item.__name__)
        print("Digite qualquer outro número que não seja equivalente à uma das opções acima para sair.")
        answer = int(input("-> "))
        if (answer >= len(mainOptions)):
            quit(0)
        mainOptions[answer]()
        writeChanges()

main()
