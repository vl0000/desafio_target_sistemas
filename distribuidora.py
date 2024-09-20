import json
import sys


def proportions(inp: dict):
    """Calcula as proporções entre os faturamentos por estado"""
    total: float = sum(map(float, inp.values()))

    for k in inp.keys():
        print(f"{k}: {(inp[k]/total)*100:.2f}%")


if __name__ == "__main__":
    file = input("Nome do arquivo. ex: ./dados.json\n")
    data: dict = dict()

    with open(file, 'r') as f:
        try:
            data = json.loads(f.read())
        except:
            print("O arquivo não pode ser lido")
            sys.exit(1)
        f.close()

    proportions(data)
