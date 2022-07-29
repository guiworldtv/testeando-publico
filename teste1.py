import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://vimeo.com/search/sort:latest?q=AULA/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.find('div',attrs={'class': 'iris_p_infinite__item span-1'})

print(noticias)

for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

  # print(titulo.text)
  # print(titulo['href']) # link da notícia

  # Subtítulo: div class="feed-post-body-resumo"
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if (subtitulo):
    # print(subtitulo.text)
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    lista_noticias.append([titulo.text, '', titulo['href']])


news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)

# print(news)
