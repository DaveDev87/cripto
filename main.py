""" Esto funciona con Python 3.8^ """
from utils import max_bits, randomString, toStr, toComma
from random import randint


def desencriptar(indice, data):
    arr = indice.split(",")
    cont = 0
    resul = ""

    for item in arr:
        resul += data[cont]
        cont += int(item) + 1

    return resul


def addString(value):
    resul = randomString(value)
    return resul


def main():
    f = open("data.txt", "r")
    text = f.read()
    large = len(text)
    newLarge = max_bits(large)

    key = []
    data = []

    for idx, item in enumerate(text):
        data.append(item)
        value = randint(0, 20)
        key.append(value)
        data.append(addString(value))

    print(desencriptar(toComma(key), toStr(data)))


if __name__ == "__main__":
    main()
