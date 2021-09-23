import random

class Question_06:

    def __init__(self):
        self.list_of_numbers = []
        self.list_of_odd_numbers = []
        self.list_of_even_index_elements = []
        self.max_range = 10

    def ask_for_nums(self):
        for num in range(self.max_range):
            self.list_of_numbers.append(random.randint(0, 100))
            self.tuple_of_numbers = tuple(self.list_of_numbers)
        return self

    def get_odd_nums(self):
        for num in self.list_of_numbers:
            if num % 2:
                self.list_of_odd_numbers.append(num)
        return self

    def get_even_index_elements(self):
        for num in self.list_of_numbers:
            if self.list_of_numbers.index(num) % 2 == 0:
                self.list_of_even_index_elements.append(num)
        return self     

    def print_output(self):
        print(f"Original tuple: {tuple(self.tuple_of_numbers)}")
        print(f"List of odd numbers: {self.list_of_odd_numbers}")
        print(f"Tuple of numbers in even positions: {tuple(self.list_of_even_index_elements)}")

def main():
    Question_06().ask_for_nums().get_odd_nums().get_even_index_elements().print_output()

main()