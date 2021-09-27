import requests
from bs4 import BeautifulSoup

class Question_12():

    def __init__(self):
        self.url = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html').text
        self.bs_soup = BeautifulSoup(self.url, 'html.parser')
        self.filter_states = ['DF', 'GO', 'MT', 'MS']
        self.data_list = []

    def show_tables(self):
        for data in self.bs_soup.find_all('div', {'class': 'tabela'}): 
            print(data.get_text())
            print(self.data_list)
        return self

    def show_state_info(self):
        input_state = input("Enter a midwest Brazilian state: ")
        for state in self.filter_states:
            if input_state not in self.filter_states:
                print("Not a valid state.")
                return
            else:
                print('hi')
               

    def print_output(self):
        #print(self.data.get_text())
        pass

def main():
    Question_12().show_tables().show_state_info()#.print_output()

main()