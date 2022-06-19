import selenium, time, warnings,  sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
warnings.filterwarnings("ignore")

#-----------------------------------------------------------------------------------------------
#SETANDO INFORMACOES FIXAS
cpf = ""
rg = ""
nasc = ""
instituicao = ""
dirRaiz = 'C://///'

#-----------------------------------------------------------------------------------------------
#INICIANDO O CHROMEDRIVER
chrome_options = webdriver.ChromeOptions()
chromedriver = dirRaiz+"Driver/chromedriver.exe"
chrome_options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

#-----------------------------------------------------------------------------------------------
#REALIZANDO A EDIÇÃO DO PERFIL E VENDO VAGAS RECOMENDADAS
try:
    driver.get("https://estagiei.netlify.app/")
    print("Editar perfil")
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/button/a'))).click()
    print("Editando perfil")
    time.sleep(2)
    driver.find_element_by_id('cadastroEstudante_cpf').send_keys(cpf)
    print("CPF inserido")
    time.sleep(2)
    driver.find_element_by_id('cadastroEstudante_rg').send_keys(rg)
    print("RG inserido")
    time.sleep(2)
    driver.find_element_by_id('cadastroEstudante_dataNascimento').send_keys(nasc)
    print("Selecionando competência")
    time.sleep(2)
    driver.find_element_by_id('cadastroEstudante_instEnsino').send_keys(instituicao)
    print("Competência selecionada")
    time.sleep(2)
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cadastroEstudante"]/div[6]/div/div/div/div'))).click()
    time.sleep(2)
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[6]/div'))).click()
    print("Competência inserida")
    time.sleep(2)
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cadastroEstudante"]/div[7]/div/div/div/button[2]'))).click()
    print("Alterações salvas")
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div[1]/div[1]/div/div[2]/div'))).click()
    print("Verificando vagas recomendadas")
    
except:
    print('Falha ao executar o script de teste, execução finalizada!')
    sys.exit()