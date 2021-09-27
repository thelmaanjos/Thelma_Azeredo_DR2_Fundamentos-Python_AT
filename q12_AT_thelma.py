import requests
from bs4 import BeautifulSoup

class Question_12():

    def __init__(self):
        self.url = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html').text
        self.bs_soup = BeautifulSoup(self.url, 'html.parser')
        self.filter_states = ['DF', 'GO', 'MT', 'MS']
        self.cell = 'div', {'class': 'celula'}

    def show_tables(self):
        for data in self.bs_soup.find_all('div', {'class': 'tabela'}): 
            print(data.get_text())
        return self

    def show_state_info(self):
        input_state = input("Enter a midwest Brazilian state: ")
        for state in self.filter_states:
            if input_state not in self.filter_states:
                print("Not a valid state.")
                return
            else:
                for data in self.bs_soup.find_all('div', {'class': 'linha'}): 
                    if input_state == data.find_all(self.cell)[0].get_text():
                        print(data.find_all(self.cell)[0].get_text())
                        print(data.find_all(self.cell)[1].get_text())
                        print(data.find_all(self.cell)[2].get_text())
                        print(data.find_all(self.cell)[3].get_text())
                        print(data.find_all(self.cell)[4].get_text())
                return self

def main():
    Question_12().show_tables().show_state_info()

main()