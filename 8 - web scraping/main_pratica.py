import requests
from bs4 import BeautifulSoup

url = "https://www.statsf1.com/pt/circuit-interlagos.aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# o site não aceita requisições de scripts, então precisamos colocar um header com o User-Agent do navegador
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup=BeautifulSoup(response.content, "lxml")
    tabela = soup.find("table", id="ctl00_CPH_Main_RPT_Circuit_ctl01_GV_GP")
    
    if tabela:
        with open("interlagos.txt", "w", encoding="utf-8") as arquivo:
            linhas = tabela.find_all("tr")
            for linha in linhas[1:]:
                colunas = linha.find_all("td")
                data = colunas[0].get_text().strip()
                vencedor = colunas[6].get_text().strip()
                melhor_volta = colunas[8].get_text().strip()
                arquivo.write(f"Data da corrida: {data}\n")
                arquivo.write(f"Quem ganhou a corrida: {vencedor}\n")
                arquivo.write(f"Melhor volta: {melhor_volta}\n")
                arquivo.write("-" * 30 + "\n")
        print("Dados salvos em 'interlagos.txt'")
else:
    print(f"Erro ao acessar a página: {response.status_code}")