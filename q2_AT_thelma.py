class Question_02:

    def __init__(self):
        self.list_of_even_numbers = []
        self.n_number = 0
        self.sum_of_even_nums = 0

    def get_flag_number(self):
        self.n_number = int(input("Enter a number: "))
        return self

    def get_even_numbers(self):
        for i in range(1, self.n_number + 1):
            if i % 2 == 0:
                self.list_of_even_numbers.append(i)
        return self
    
    def sum_even_numbers(self):
        self.sum_of_even_nums = sum(self.list_of_even_numbers)
        return self

    def print_output(self):
        print(f"List of even numbers from 1 to {self.n_number}: {self.list_of_even_numbers}")
        print(f"Total sum of even numbers: {self.sum_of_even_nums}")

def main():
    Question_02().get_flag_number().get_even_numbers().sum_even_numbers().print_output()

main()