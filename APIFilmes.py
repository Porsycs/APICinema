import requests


# Chave de API do TMDb
api_key = '{chave_api}'


#Salvar em arquivo o resultado
def salvar_resultado_em_arquivo(resultado, arquivoNome):
    with open(f'Filmes_{arquivoNome}.txt', 'w') as arquivo:
        arquivo.write(resultado)

def obter_ids_filmes(url):
    try:
        # Faz uma requisição GET para obter a lista de filmes populares
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Extrai os dados da resposta
            data = response.json()
            # Obtém os IDs de todos os filmes
            ids_filmes = [filme['id'] for filme in data['results']]
            return ids_filmes
        else:
            # Caso contrário, exibe uma mensagem de erro
            print('Erro ao obter lista de Ids de Filmes:', response.status_code)

    except Exception as e:
        # Caso ocorra uma exceção, exibe uma mensagem de erro
        print('Erro ao obter lista de Ids de Filmes:', str(e))


def obter_informacoes_filme(url):
    id_filmes = obter_ids_filmes(url)
    try:
        todosDados = []  # Lista vazia para armazenar todos os dados

        for filme_id in id_filmes:
            # Faz uma requisição GET para obter as informações do filme em português
            url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={api_key}&language=pt-BR'
            response = requests.get(url)

            # Verifica se a requisição foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                # Extrai os dados da resposta
                data = response.json()
                # Manipulação de Dados
                titulo = data['title']
                sinopse = data['overview']
                generos = ', '.join([genero['name'] for genero in data['genres']])
                dataLancamento = data['release_date']
                NotaMedia = data['vote_average']
                Link = f'https://www.themoviedb.org/movie/{filme_id}?language=pt-BR'
            else:
                # Caso contrário, exibe uma mensagem de erro
                print(f'Erro ao obter informações do filme {filme_id}:', response.status_code)

            dados = f"Título: {titulo}\nSinopse: {sinopse}\nGêneros: {generos}\nData de Lançamento: {dataLancamento}\nNota: {NotaMedia}\nLink: {Link}\n\n"
            todosDados.append(dados)  # Adiciona os dados à lista

        return '\n'.join(todosDados)

    except Exception as e:
        # Caso ocorra uma exceção, exibe uma mensagem de erro
        print(f'Erro ao obter informações do filme', str(e))



resultadoPopulares = obter_informacoes_filme(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=pt-BR')
resultadoTop = obter_informacoes_filme(f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR')
resultadoNow = obter_informacoes_filme(f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=pt-BR')
resultadoUpComing = obter_informacoes_filme(f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=pt-BR')
salvar_resultado_em_arquivo(resultadoPopulares, arquivoNome='Populares')
salvar_resultado_em_arquivo(resultadoTop, arquivoNome='Top')
salvar_resultado_em_arquivo(resultadoNow, arquivoNome='Now')
salvar_resultado_em_arquivo(resultadoUpComing, arquivoNome='Upcoming')
