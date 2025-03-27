from bs4 import BeautifulSoup
with open('home_aula.html', 'r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content, 'lxml')
    #print(soup.prettify())#imprime o html de forma identada
    #tags=soup.find('h5')#acha o primeiro
    courses_html_tags=soup.find_all('h5')# Encontra todas as tags <h5> no arquivo HTML e retorna uma lista delas
    
    """ for course in courses_html_tags:
        print(course.text)#imprime o texto dentro da tag """
    course_cards=soup.find_all('div', class_='card')# Encontra todas as tags <div> com a classe 'card' no arquivo HTML e retorna uma lista delas
    for course in course_cards:
        #print(course.h5)#imprime o texto da tag com a tag
        course_name=course.h5.text #imprime o texto da tag sem a tag
        course_price=course.a.text.split()[-1]#imprime o texto da tag sem a tag e o ultmio elemento da lista
        print(f'{course_name} costs {course_price}')
        