from bs4 import BeautifulSoup
import requests # para fazer requisições HTTP
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text #fazendo requisição HTTP das vagas de emprego de python e pegando o texto da página

    soup=BeautifulSoup(html_text, 'lxml')#criando um objeto BeautifulSoup
    #pagina atualizou a estrutura HTML, então o código abaixo não funciona mais
    # jobs=soup.find('li', class_='clearfix job-bx wht-shd-bx')#pegando todas as vagas de emprego da página
    # print(jobs)
    # agora o li não tem nenhuma classe mas tem dentro uma div que tem a classe srp-listing clearfix
    jobs=soup.find_all('div', class_='srp-listing clearfix')#pegando todas as vagas de emprego da página
    # print(job)
    # não tem mais few days no published date, então não tem como pegar o tempo da vaga de emprego
    numeros_validos = [str(i) for i in range(1, 11)]#pegando os números válidos de 1 a 10
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='posting-time').text
        if any(num in published_date for num in numeros_validos):
            company_name = job.find('span', class_='srp-comp-name').text.replace(' ', '')#pegando o nome da empresa e tirando os espaços em branco
            skills= job.find('div', class_='srp-keyskills').text.replace(" ", ",").strip()#pegando as skills da vaga de emprego
            more_info = job.a['href']#pegando o link da vaga de emprego
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Published Date: {published_date.strip()}\n')
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Skills: {skills}\n')
                    f.write(f'More Info: {more_info}\n')
                print(f'file saved: {index}.txt')
                
            
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes... (ctrl + c to stop)')
        time.sleep(time_wait*60) #espera 10 minutos para fazer a próxima requisição

