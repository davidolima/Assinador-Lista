import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

file = open('info.txt', 'r')
file = file.readlines()
info = {}
for line in file:
    line = line.replace("\n","")
    line = line.split(': ')
    info[line[0]] = line[1] 

time.sleep(1)
nome = info['nome']
listaInicial = info['link_lista_inicial']
listaFinal = info['link_lista_final']
horarioInicial = int(info['horario_lista_inicial'])
horarioFinal = int(info['horario_lista_final'])

def iniciarDriver():
    global driver
    try:
        driver = webdriver.Chrome(executable_path='chromedriver')
    except:
        driver = webdriver.Firefox(executable_path='geckodriver')

if horarioInicial <= int(time.localtime().tm_hour) < horarioInicial+1:
    iniciarDriver()
    driver.get(listaInicial)
    field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".quantumWizTextinputPaperinputInput")))
    field.click()
    field.send_keys(nome)
    enviar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel")))
    enviar.click()
    
    print("Lista Inicial Assinada com o nome",nome)
    input("Pressione Enter pra sair.")
    driver.quit()
    quit()

if horarioFinal-1 <= int(time.localtime().tm_hour) < horarioFinal:
    iniciarDriver()
    driver.get(listaFinal)
    field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".quantumWizTextinputPaperinputInput")))
    field.click()
    field.send_keys(nome)
    enviar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel")))
    enviar.click()
    print("Lista Final assinada com o nome", nome)
    input("Pressione Enter pra sair.")
    driver.quit()
    quit()

else:
    print("Não há listas pra assinar",time.localtime().tm_hour,"horas")
    input("Pressione Enter pra sair.")
    driver.quit()
    quit()