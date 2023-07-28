
import datetime
import os
from datetime import datetime, timedelta

# Obter o horário atual
horario_atual = datetime.now()
print(horario_atual)

import pandas as pd


import requests
from bs4 import BeautifulSoup

from urllib.parse import quote, quote_plus, unquote


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

# Baixe os recursos necessários para o NLTK
nltk.download('punkt')
nltk.download('stopwords')

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

import openai
openai.api_key = OPEN_AI_KEY



# Obter a data de hoje
data_hoje = datetime.today().strftime('%Y-%m-%d')
print(data_hoje)
dias = 0


# Obter a data de ontem
data_ontem = (datetime.today() - timedelta(days=dias)).strftime('%Y-%m-%d')
print(data_ontem)

lista_palavras = pd.DataFrame(['crédito','cra', 'cri','FIIs','FIagro','imobiliário','INCC','securitizadora','securitização','captação','startup','fintech','tokenização','CVM','construção','loteamento','condomínio','IPTU','ITBI','imóvel','edifício'], columns=['Words'])
tam_lista = len(lista_palavras)

link = 'https://valor.globo.com/busca/?q='

parte_01_link = 'https://valor.globo.com/busca/?q='
parte_02_link = '&order=recent&from=' + data_ontem + 'T00%3A00%3A00-0300&to=' + data_hoje + 'T23%3A59%3A59-0300'


noticias = pd.DataFrame()
conta = 0


for palavras in range(0,tam_lista):
    print("-"*200)
    palavra = lista_palavras.loc[palavras,'Words']
    link_acesso = parte_01_link + palavra + parte_02_link
    print(link_acesso)
    # URL do site com os parâmetros de busca
    url = link_acesso
    # Fazendo a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200 indica sucesso)
    if response.status_code == 200:
        # Obtendo o conteúdo HTML da página
        html_content = response.text

        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encontrar a div com a classe "results--"
        div_results = soup.find('div', class_='results--')
        
        if div_results != None:
            print("Resultados para a palavra: " + palavra)
            # Extrair o conteúdo dentro da div
            conteudo_div_results = div_results.get_text()
            #print(div_results)

            # Encontrar todos os elementos 'a' dentro da div_results
            links_noticias = div_results.find_all('a', href=True)

            # Extrair e exibir os links de cada notícia
            for link in links_noticias:
                url_noticia = 'https:' + link['href']

                # Link original fornecido
                link_original = url_noticia
                # Extrair a parte do link que contém o código
                if "&u=" in link_original:
                    codigo_parte_url = link_original.split("&u=")[1]
                    # O restante do seu código aqui
                else:
                    codigo_parte_url = link_original
                # Extrair o código da URL até "&syn=False&key="
                codigo_codigo_sem_syn_key = codigo_parte_url.split("&syn")[0]

                # Decodificar a parte do código para remover os códigos de escape
                codigo_decodificado = unquote(codigo_codigo_sem_syn_key)

                # Substituir os caracteres especiais pelos desejados (barras e traços)
                codigo_transformado = codigo_decodificado.replace("/", "/").replace("=", "-")

                # Exibir o resultado
                
                if conta ==0:
                    print(codigo_transformado)
                    noticias.loc[conta,'link']=codigo_transformado
                    noticias.loc[conta,'palavra']  =palavra
                    conta = conta + 1
                else:
                    if codigo_transformado != noticias.loc[conta-1,'link']:
                        print(codigo_transformado)
                        noticias.loc[conta,'link']=codigo_transformado
                        noticias.loc[conta,'palavra']  =palavra
                        conta = conta + 1
                    else:
                        foo = "WASD"
                #print(url_noticia)
        else:
            print("Sem resultados para a palavra: " + palavra)

    else:
        print(f"Não foi possível acessar o site. Código de status: {response.status_code}")


    
noticias = noticias[~noticias['link'].str.contains('patrocinado')]
noticias = noticias[~noticias['link'].str.contains('valor-ri')]
noticias = noticias[~noticias['link'].str.contains('&page-')]
noticias = noticias[~noticias['link'].str.contains('conteudo-de-marca')]


import pandas as pd
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from urllib.parse import quote, quote_plus, unquote


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

# Baixe os recursos necessários para o NLTK
nltk.download('punkt')
nltk.download('stopwords')



import openai
openai.api_key = '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'



# Obter a data de hoje
data_hoje = datetime.today().strftime('%Y-%m-%d')
print(data_hoje)
dias = 0


# Obter a data de ontem
data_ontem = (datetime.today() - timedelta(days=dias)).strftime('%Y-%m-%d')
print(data_ontem)

lista_palavras = pd.DataFrame(['crédito','cra', 'cri','FIIs','FIagro','imobiliário','INCC','securitizadora','securitização','captação','startup','fintech','tokenização','CVM','construção','loteamento','condomínio','IPTU','ITBI','imóvel','edifício'], columns=['Words'])
tam_lista = len(lista_palavras)

link = 'https://valor.globo.com/busca/?q='

parte_01_link = 'https://valor.globo.com/busca/?q='
parte_02_link = '&order=recent&from=' + data_ontem + 'T00%3A00%3A00-0300&to=' + data_hoje + 'T23%3A59%3A59-0300'


noticias = pd.DataFrame()
conta = 0


for palavras in range(0,tam_lista):
    print("-"*200)
    palavra = lista_palavras.loc[palavras,'Words']
    link_acesso = parte_01_link + palavra + parte_02_link
    print(link_acesso)
    # URL do site com os parâmetros de busca
    url = link_acesso
    # Fazendo a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200 indica sucesso)
    if response.status_code == 200:
        # Obtendo o conteúdo HTML da página
        html_content = response.text

        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encontrar a div com a classe "results--"
        div_results = soup.find('div', class_='results--')
        
        if div_results != None:
            print("Resultados para a palavra: " + palavra)
            # Extrair o conteúdo dentro da div
            conteudo_div_results = div_results.get_text()
            #print(div_results)

            # Encontrar todos os elementos 'a' dentro da div_results
            links_noticias = div_results.find_all('a', href=True)

            # Extrair e exibir os links de cada notícia
            for link in links_noticias:
                url_noticia = 'https:' + link['href']

                # Link original fornecido
                link_original = url_noticia
                # Extrair a parte do link que contém o código
                if "&u=" in link_original:
                    codigo_parte_url = link_original.split("&u=")[1]
                    # O restante do seu código aqui
                else:
                    codigo_parte_url = link_original
                # Extrair o código da URL até "&syn=False&key="
                codigo_codigo_sem_syn_key = codigo_parte_url.split("&syn")[0]

                # Decodificar a parte do código para remover os códigos de escape
                codigo_decodificado = unquote(codigo_codigo_sem_syn_key)

                # Substituir os caracteres especiais pelos desejados (barras e traços)
                codigo_transformado = codigo_decodificado.replace("/", "/").replace("=", "-")

                # Exibir o resultado
                
                if conta ==0:
                    print(codigo_transformado)
                    noticias.loc[conta,'link']=codigo_transformado
                    noticias.loc[conta,'palavra']  =palavra
                    conta = conta + 1
                else:
                    if codigo_transformado != noticias.loc[conta-1,'link']:
                        print(codigo_transformado)
                        noticias.loc[conta,'link']=codigo_transformado
                        noticias.loc[conta,'palavra']  =palavra
                        conta = conta + 1
                    else:
                        foo = "WASD"
                #print(url_noticia)
        else:
            print("Sem resultados para a palavra: " + palavra)

    else:
        print(f"Não foi possível acessar o site. Código de status: {response.status_code}")


    
noticias = noticias[~noticias['link'].str.contains('patrocinado')]
noticias = noticias[~noticias['link'].str.contains('valor-ri')]
noticias = noticias[~noticias['link'].str.contains('&page-')]
noticias = noticias[~noticias['link'].str.contains('conteudo-de-marca')]

#encontra se tem alguma notícia com mais de uma palavra
noticias = noticias.reset_index(drop=True)
tam_news = len(noticias)

for palavra in range(0,tam_news):
    link_procurado = noticias.loc[palavra,'link']
    pala_procurado = noticias.loc[palavra,'palavra']
    conta = 1
    noticias.loc[palavra,'conta'] = conta
    noticias.loc[palavra,'palavras'] = pala_procurado
    print(link_procurado)
    for procura in range(0,tam_news):
        link_encontra = noticias.loc[procura,'link']
        pala_encontra = noticias.loc[procura,'palavra']
        if palavra != procura and pala_procurado != pala_encontra and link_procurado == link_encontra:
            noticias.loc[palavra,'palavras'] = noticias.loc[palavra,'palavras'] + "; " + pala_encontra
            conta = conta +1
            noticias.loc[palavra,'conta'] = conta
            
            
noticias
noticias = noticias.sort_values(by='conta', ascending=True)
noticias = noticias.reset_index(drop=True)
noticias



noticias_sem_duplicatas = noticias.drop_duplicates(subset='link')
noticias_sem_duplicatas = noticias_sem_duplicatas.reset_index(drop=True)

tam_noticias = len(noticias_sem_duplicatas)
noticias_sem_duplicatas

# def para gerar bullets points do conteúdo

def create_bullet_points(text, num_points=7):
    # Tokenização do texto em frases
    sentences = sent_tokenize(text)

    # Remover stopwords
    stop_words = set(stopwords.words("portuguese"))
    word_tokens = nltk.word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]

    # Frequência das palavras
    word_freq = FreqDist(filtered_text)

    # Pontuação das frases baseada nas frequências das palavras
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_freq.keys():
                if len(sentence.split(" ")) < 30:  # Limitar o tamanho das frases para evitar resumos muito longos
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] = word_freq[word]
                    else:
                        sentence_scores[sentence] += word_freq[word]

    # Selecionar as 5 principais frases para o resumo
    summarized_sentences = nlargest(num_points, sentence_scores, key=sentence_scores.get)

    # Formatar como bullet points
    bullet_points = ["- " + sentence for sentence in summarized_sentences]

    return bullet_points

for i in range(0,tam_noticias):
    link_noticia = noticias_sem_duplicatas.loc[i,'link']
    link_final = 'https://leiaisso.net/' + link_noticia
    noticias_sem_duplicatas.loc[i,'link_free'] = link_final
    # URL do link que desejamos fazer o scrape
    url = link_final
    # Faz a solicitação HTTP para acessar a página
    response = requests.get(url)
    link_encurtado = response.url
    noticias_sem_duplicatas.loc[i,'link_short'] = link_encurtado
    
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o conteúdo da notícia dentro da div com class="content"
        try:
            conteudo_noticia = soup.find('div', class_='content').get_text()
            data_noticia = soup.find('p', class_='info text-feat').get_text()
            titulo = soup.find('h1', class_='title').get_text()

            noticias_sem_duplicatas.loc[i,'data'] = data_noticia
            noticias_sem_duplicatas.loc[i,'titulo'] = titulo
            noticias_sem_duplicatas.loc[i,'conteudo'] = conteudo_noticia
            
            print(titulo)
            palavras_chave = noticias_sem_duplicatas.loc[i,'palavras'] 
            print("--- Palavras chave: " +  palavras_chave)
            texto_resumido = ""
            resumo_bullet_points = create_bullet_points(conteudo_noticia, num_points=7)
            for point in resumo_bullet_points:
                texto_resumido = texto_resumido + point
            #print(texto_resumido)
        
            response = openai.Completion.create(
              engine='text-davinci-003',
              prompt='Faça o resumo destes bullet points desta notícia: ' + texto_resumido,
              temperature=0.1,
              max_tokens=1000
            )

            reply = response.choices[0].text.strip()
            
            print("--- RESUMO POR IA ---")
            print(reply)
            noticias_sem_duplicatas.loc[i,'resumo'] = reply
            
            
            response = openai.Completion.create(
              engine='text-davinci-003',
              prompt="Em uma escala de -100 até 100, sendo -100 para 100% negativo ou tristeza ou desolação ou desanimador e +100 para  positivo ou alegre ou 100% feliz ou empolgante para o texto a seguir, qual nota seria? Retorne somente a nota. " + reply,
              temperature=0.1,
              max_tokens=1000
            )

            reply = response.choices[0].text.strip()
            reply

            nota = int(reply)
            noticias_sem_duplicatas.loc[i,'nota'] = nota
            print(nota)

            if nota>=-100 and nota < -75:
                resposta_emoji = "😭" #(Super negativo ou triste ou desolador)
            if nota>=-75 and nota < -50:
                resposta_emoji = "😢" #(Negativo ou triste)
            if nota>=-50 and nota < -25:
                resposta_emoji = "😞" #(Triste ou desanimado)
            if nota>=-25 and nota < 0:
                resposta_emoji = "🙁" #(Um pouco triste ou insatisfeito)
            if nota>=0 and nota < 25:
                resposta_emoji = "😐" #(Neutro)
            if nota>=25 and nota < 50:
                resposta_emoji = "🙂" #(Um pouco positivo ou satisfeito)
            if nota>=50 and nota < 75:
                resposta_emoji = "😄" #(Feliz ou empolgado)
            if nota>=75 and nota <= 100:
                resposta_emoji = "😍"  #(Muito feliz ou animado)

            noticias_sem_duplicatas.loc[i,'emoji'] = resposta_emoji
            print("Sentimento da notítica:" + resposta_emoji)

            
        except:
            foo = "WASD"
    else:
        print(f"Não foi possível acessar a página. Status code: {response.status_code}")
    print(link_final)
    

import pandas as pd

# Exemplo de DataFrame com as informações das notícias
data = {
    'Manchete': ['Notícia 1', 'Notícia 2', 'Notícia 3', 'Notícia 4', 'Notícia 5', 'Notícia 6', 'Notícia 7', 'Notícia 8', 'Notícia 9', 'Notícia 10'],
    'Data': ['2023-07-25', '2023-07-26', '2023-07-27', '2023-07-28', '2023-07-29', '2023-07-30', '2023-07-31', '2023-08-01', '2023-08-02', '2023-08-03'],
    'Resumo': ['Resumo da notícia 1', 'Resumo da notícia 2', 'Resumo da notícia 3', 'Resumo da notícia 4', 'Resumo da notícia 5', 'Resumo da notícia 6', 'Resumo da notícia 7', 'Resumo da notícia 8', 'Resumo da notícia 9', 'Resumo da notícia 10'],
    'Matéria completa': ['Texto completo da notícia 1', 'Texto completo da notícia 2', 'Texto completo da notícia 3', 'Texto completo da notícia 4', 'Texto completo da notícia 5', 'Texto completo da notícia 6', 'Texto completo da notícia 7', 'Texto completo da notícia 8', 'Texto completo da notícia 9', 'Texto completo da notícia 10'],
    'Link': ['www.noticia1.com', 'www.noticia2.com', 'www.noticia3.com', 'www.noticia4.com', 'www.noticia5.com', 'www.noticia6.com', 'www.noticia7.com', 'www.noticia8.com', 'www.noticia9.com', 'www.noticia10.com']
}

df_noticias = pd.DataFrame(data)

caminho = '/Users/feliperibeiro/Downloads/'


# Monta o conteúdo do arquivo HTML
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Notícias</title>
</head>
<body>
    <h1>Lista de Notícias</h1>
    <ul>
"""

# Itera sobre as linhas da DataFrame e monta as notícias em HTML
for _, linha in noticias_sem_duplicatas.iterrows():
    emoji = linha['emoji']
    manchete = linha['titulo']
    data = linha['data']
    resumo = linha['resumo']
    materia_completa = linha['conteudo']
    link = linha['link_short']
    palavras = linha['palavras']

    html_content += f"""        <li>
            <small>{emoji}</small>
            <small> - </small>
            <small>Palavras chave: </small>
            <small>{palavras}</small>
            <strong>{manchete}</strong>
            <small>{data}</small>
            <button class="btn-resumo" onclick="toggleResumo(this)">+</button>
            <div class="resumo" style="display: none;">
                <strong>Resumo:</strong>
                <p>{resumo}</p>
                <button class="btn-materia-completa" onclick="toggleMateriaCompleta(this)">Leia a matéria completa aqui</button>
                <div class="materia-completa" style="display: none;">
                    <strong>Matéria completa:</strong>
                    <p>{materia_completa}</p>
                </div>
            </div>
        </li>
"""
# Adiciona o fechamento das tags HTML
html_content += """    </ul>

    <script>
        function toggleResumo(button) {
            const resumoDiv = button.nextElementSibling;
            resumoDiv.style.display = resumoDiv.style.display === "none" ? "block" : "none";
        }

        function toggleMateriaCompleta(button) {
            const materiaCompletaDiv = button.nextElementSibling;
            materiaCompletaDiv.style.display = materiaCompletaDiv.style.display === "none" ? "block" : "none";
        }
    </script>
</body>
</html>
"""

# Salva o conteúdo no arquivo noticias.html
with open(caminho + "index.html", "w", encoding="utf-8") as arquivo_html:
    arquivo_html.write(html_content)

print("Arquivo HTML com as notícias criado com sucesso!")

# Obter o horário atual
horario_atual = datetime.now()
print(horario_atual)
