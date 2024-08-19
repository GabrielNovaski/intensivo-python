import pyautogui
from time import sleep
import pandas as pd

tabela = pd.read_csv(r"C:\Users\Ghn12\OneDrive\Documentos\Python\hashtag\produtos.csv")

for linha in tabela:
    print(linha)