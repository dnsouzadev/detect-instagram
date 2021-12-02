import requests
from bs4 import BeautifulSoup
from easygui import fileopenbox
from sys import exit



def main():
    try:
        selector = int(input('[1] -> Se você quiser testar apenas um usuário. \n[2] -> Se você desejar testar uma lista de usuários. \n>>> '))
        if selector == 1:
            usuario = input('Ok! Conte-me qual usuário é: ')
            print()
            print(have_account(usuario))
        elif selector == 2:
            lista1 = fileopenbox(default='*.txt', title='Insira sua lista!')
            lista = open(lista1, encoding='utf-8').read().splitlines()
            for lg in lista:
                print(have_account(lg))
        else:
            print('Número Inválido!')
    except:
        print('Opção inválida!')
        exit()



def have_account(user):
    res = requests.get(f'https://www.instagram.com/{user}/', allow_redirects=False)
    soup = BeautifulSoup(res.text, "html.parser")
    if not res.status_code == 404:
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:description":
                info = tag.get("content", None)
                info = info.split()
                seguidores= info[0]
                seguindo = info[2]
                posts = info[4]
                return f'@{user}-> {seguidores} Seguidores | {seguindo} Seguindo | {posts} Posts'
    return f'@{user} -> Não tem conta ativa no instagram!'


if __name__ == "__main__":
   main()