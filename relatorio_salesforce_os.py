from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule
import subprocess
import os
import pandas as pd

def extracao_arquivo_salesforce(): 

    # Configurar o WebDriver (aqui usamos o Chrome)
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Abrir a página de login
    driver.get('https://desktopsa.my.salesforce.com/')
    time.sleep(2)
    
    # Encontrar os elementos de entrada de texto para nome de usuário e senha
    username_input = driver.find_element(By.NAME, 'username')  # ou use outro localizador apropriado
    password_input = driver.find_element(By.NAME, 'pw')  # ou use outro localizador apropriado
    
    # Inserir as credenciais
    username_input.send_keys('login_usuario')
    password_input.send_keys('senha_usuario')
    
    # Submeter o formulário de login
    password_input.send_keys(Keys.RETURN)

    # Acessando diretamente o link onde está o relatório, fazendo o download do arquivo
    driver.get('https://desktopsa.my.salesforce.com/servlet/PrintableViewDownloadServlet?isdtp=p1&reportId=00OV2000001IPtpMAG&detailsOnly=true')

    # Esperar 30 segundos para o relatório carrega
    time.sleep(30)

    # Fechar o navegador
    driver.quit()

    # Caminho que o arquivo foi baixado
    download_path = r"C:\Users\clizan.lopes\Documentos"
    return download_path

# Função para executar o comando
def executar_comando():
    comando = extracao_arquivo_salesforce()
    subprocess.run(comando, shell=True)

# Agendar a execução do comando
schedule.every().day.at("08:27").do(executar_comando)  # Executar às 08:10
schedule.every().day.at("12:09").do(executar_comando)  # Executar às 15:50
schedule.every().day.at("16:56").do(executar_comando)  # Executar às 16:50

# Loop principal para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)
