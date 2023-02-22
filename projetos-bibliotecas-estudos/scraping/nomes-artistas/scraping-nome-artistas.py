# Importar bibliotecas
import requests
import csv
from bs4 import BeautifulSoup

#headers = {
#    'User-Agent': 'Seu nome, example.com',
#    'From': 'email@example.com'
#}
#url = 'https://example.com'
#page = requests.get(url, headers = headers)

# Criar um arquivo para gravar, adicionar linha de cabeçalhos
f = csv.writer(open('scraping-nomes-artistas.csv', 'w'))
f.writerow(['Name', 'Link'])

# Coletar e analisar a primeira página da letra Z
#page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')
#soup = BeautifulSoup(page.text, 'html.parser')

# Coletar e analisar as 4 páginas da Letra Z
pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Remover links inferiores
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Pegar todo o texto da div BodyText
    artist_name_list = soup.find(class_='BodyText')

    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
    artist_name_list_items = artist_name_list.find_all('a')

    # Usar .contents para pegar as tags <a> filhas
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        # Adicionar em uma linha o nome de cada artista e o link associado
        f.writerow([names, links])