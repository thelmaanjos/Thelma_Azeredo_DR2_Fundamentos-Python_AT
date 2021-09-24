
"""
10. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
E:
a. Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI 
(a partir de 2001), #SWE, DEN, NOR
qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
i. Curling
ii. Patinação no gelo (skating)
iii. Esqui (skiing)
iv. Hóquei sobre o gelo (ice hockey)
b. Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve
imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e
gênero (masculino ou feminino) cada medalha foi obtida.

"""
import requests
# relatório mostrando o total de medalhas de cada um dos países
# e
#em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

# 2006,Turin,Biathlon,Biathlon,POL,15km mass start,M,Silver


class Question_10():

    def __init__(self):
        self.url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'
        self.build_table()

    def build_table(self):
        csv = requests.get(self.url).text
        # Separa as linhas em uma lista
        linhas = csv.splitlines()
        # Separa os rotulos da coluna
        column_names = linhas[0].split(',') # Year,City,Sport,Discipline,NOC,Event,Event gender,Medal

        self.winter_olympics_medals = []
        #Year,City,Sport,Discipline,NOC,Event,Event gender,Medal
        # 1992,Albertville,Biathlon,Biathlon,EUN,7.5km,W,Gold
        for linha in range(1, len(linhas)):
            # linha = 2006,Turin,Biathlon,Biathlon,POL,15km mass start,M,Silver
            #linha[0] => 2
            colunas = linhas[linha].split(',') #extrai valores separados por virgula
            # colunas = [1992,Albertville,Biathlon,Biathlon,EUN,7.5km,W,Gold]
            #colunas[0] => 1992
            obj = {}
            # Year,City,Sport,Discipline,NOC,Event,Event gender,Medal
            # 1992,Albertville,Biathlon,Biathlon,EUN,7.5km,W,Gold
            # {'Year': '2006', 'City': 'Turin', 'Sport': 'Skiing', 'Discipline': 'Snowboard', 'NOC': 'USA', 'Event': 'Snowboard Cross', 'Event gender': 'W', 'Medal': 'Silver'}
            for index, name in enumerate(column_names):
                obj[name] = colunas[index]
                self.winter_olympics_medals.append(obj)

    # def teste(self):
    #     val = 0
    #     for item in self.winter_olympics_medals:
    #         if item['NOC'] == 'SWE' and item['Medal'] == 'Gold' and int(item['Year']) >= 2001 and item['Sport'] in ['Skiing', 'Ice Hockey', 'Curling', 'Skating']:
    #             val += 1
    #             print(item)
    #     print(val)

    def by_country_list(self, country_list):
        self.country_list = country_list
        return self

    def by_starting_year(self, year):
        self.starting_year = year
        return self

    def by_sport_list(self, sport_list):
        self.sport_list = sport_list
        return self

    def get_total_gold_medals(self, country):
        self.medal_count_by_country[country] = 0
        for medal in self.winter_olympics_medals:
            if int(medal['Year']) >= self.starting_year and medal['NOC'] == country and medal['Sport'] in self.sport_list and medal['Medal'] == 'Gold':
                self.medal_count_by_country[country] += 1

    def print_winner(self):
        self.medal_count_by_country = {}
        for country in self.country_list:
            self.get_total_gold_medals(country)

        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        ranking = sorted(self.medal_count_by_country.items(), key=lambda x: x[1], reverse=True) # [('NOR', 88), ('SWE', 48), ('DEN', 0)]

        print(f'O Vencedor em Numeros de Medalhas de Ouro foi o País "{ranking[0][0]}" com {ranking[0][1]} Medalhas')
        return self


def main():
    Question_10().by_country_list(['SWE', 'DEN', 'NOR']).by_starting_year(2001).by_sport_list(['Skiing', 'Ice Hockey', 'Curling', 'Skating']).print_winner()
    #Question_10().teste()

main()