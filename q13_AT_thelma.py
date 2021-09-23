import requests
from bs4 import BeautifulSoup
from collections import Counter

class Question_13():
   
    def __init__(self):
        self.list_of_words = []
        self.dict_of_words = {}
        self.filtered_dict = {}
        self.ladies_occurrences = 0
        self.total_occurrences = 0
        self.url = requests.get('http://brasil.pyladies.com/about/').text
        self.bs_soup = BeautifulSoup(self.url, 'html.parser')

    def populate_list_of_words(self):
        for txt in self.bs_soup.findAll('p', {'class':'about-text'}):
            words = txt.text.lower().split()
            for word in words:
                self.list_of_words.append(word)
        return self
            
    def populate_dictionary(self):
        for word in self.list_of_words:
            if word in self.dict_of_words:
                self.dict_of_words[word] += 1
            else:
                self.dict_of_words[word] = 1
        if self.dict_of_words[word] == 1:
            self.ladies_occurrences = self.dict_of_words.get('ladies','0')
        return self
    
    def sum_dict_values(self):
        values = self.dict_of_words.values()
        self.total_occurrences = sum(values)
        return self
    
    def filter_dict_values(self):
        self.filtered_dict = {key: value for key, value in self.dict_of_words.items() if value == 1 }
        return self

    def print_output(self):
        print(f"Total number of words in the body page: {self.total_occurrences}")
        print(f"Words with only one occurrence: {self.filtered_dict.keys()}")
        print(f"Number of currences of the word 'ladies': {self.ladies_occurrences}")

def main():
    Question_13().populate_list_of_words().populate_dictionary().sum_dict_values().filter_dict_values().print_output()

main()
