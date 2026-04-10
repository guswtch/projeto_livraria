import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = "http://books.toscrape.com/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        print("Conexão bem-sucedida!")
    else:
        print("ERRO: A conexão não foi bem-sucedida.")
        return
    
    soup = BeautifulSoup(resposta.text, "html.parser")
    print(soup.title)

    livros_html = soup.find_all("article", class_ = "product_pod")
    print(len(livros_html))

    dados_extraidos = []

    for livro in livros_html:
        dicionario_livro ={
        "titulo" : livro.h3.a["title"],
        "preco" : livro.find("p", class_ = "price_color").text
        }
        dados_extraidos.append(dicionario_livro)
    
    print(dados_extraidos)

    arquivo = open(file="relatorio_livros.csv", mode="w", newline="", encoding="utf-8")
    cabecalho = ["titulo", "preco"]
    writer = csv.DictWriter(arquivo, fieldnames=cabecalho)
    writer.writeheader()
    writer.writerows(dados_extraidos)
    arquivo.close()

    print("Relatório CSV gerado com sucesso!")
main()