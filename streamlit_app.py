import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import streamlit as st

ref = st.text_input(label = "Digite aqui a sua referência (exemplo 012023): ")

# Configurações do Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Caminho para o Chrome WebDriver
webdriver_path = "C:\\Users\\matheus.hendrico\\OneDrive - FGV\\Área de Trabalho\\Automações Python\\chromedriver.exe"  # Substitua pelo caminho correto

# URL da página do Acre
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_638"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_AC_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Alagoas
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_639"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_AL_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Amapá
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_641"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_AP_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Amazonas
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_640"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_AM_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Bahia
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_642"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_BA_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Ceara
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_643"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_CE_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Distrito Federal
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_644"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_DF_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Espirito Santo
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_645"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_ES_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Goias
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_646"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_GO_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Maranhão
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_647"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_MA_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Mato Grosso
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_650"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_MT_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Mato Grosso do Sul
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_649"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_MS_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Minas Gerais
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_648"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_MG_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Pará
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_651"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_PA_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)



# URL da página do Paraíba
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_652"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_PB_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Paraná
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_655"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_PR_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)



# URL da página do Pernambuco
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_653"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_PE_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)



# URL da página do Piauí
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_654"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_PI_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Rio de Janeiro
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_656"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_MT_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Rio Grande do Norte
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_657"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_RN_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Rio Grande do Sul
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_660"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_RS_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página do Rondônia
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_658"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_RO_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)



# URL da página do Roraima
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_659"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_RR_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página de Santa Catarina
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_662"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_SC_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página de São Paulo
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_664"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_SP_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)



# URL da página de Sergipe
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_663"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_SE_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# URL da página de Tocantins
url = "https://www.caixa.gov.br/site/Paginas/downloads.aspx#categoria_661"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(webdriver_path, options=chrome_options)

# Acessar a página
driver.get(url)

# Aguardar o carregamento da página
time.sleep(5)

# Obter o conteúdo HTML da página
html = driver.page_source

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar todos os links na página
links = soup.find_all("a", href=True)

# Iterar sobre os links encontrados
for link in links:
    href = link["href"]

    # Verificar se o link é um zip e corresponde ao valor da referência
    if href.endswith(".zip") and re.search(r"_TO_"+ref+"_", href):
        # Montar a URL completa do arquivo zip
        zip_url = urllib.parse.urljoin(url, href)

        # Fazer o download do arquivo zip
        file_name = href.split("/")[-1]
        print(f"Baixando {file_name}...")
        urllib.request.urlretrieve(zip_url, file_name)


# Fechar o navegador
driver.quit()
