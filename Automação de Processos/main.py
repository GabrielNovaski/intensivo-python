import pyautogui
from time import sleep
import pandas as pd

# ACESSANDO O NAVEGADOR
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# ENTRANDO NO SITE
pyautogui.click(x=288, y=67)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(1)
# LOGANDO USANDO EMAIL E SENHA
pyautogui.click(x=405, y=398)
pyautogui.hotkey('ctrl', 'a')
sleep(1)
pyautogui.write('testeautomatico@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('enter')

tabela = pd.read_csv(r"C:\Users\Ghn12\OneDrive\Documentos\Python\hashtag\produtos.csv")

#CADASTRANDO PRODUTOS
for linha in tabela.index:
    pyautogui.click(x=433, y=277)

    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press('tab')
    pyautogui.press('enter')