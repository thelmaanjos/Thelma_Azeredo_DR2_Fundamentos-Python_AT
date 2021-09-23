class Question_04:

    def __init__(self):
        self.list_of_numbers = []
        self.inverted_list = []
        self.quantity_of_numbers = 5

    def get_numbers(self):
        for i in range (self.quantity_of_numbers):
            num = int(input("Enter a number: "))
            self.list_of_numbers.append(num)
        return self

    def invert_list(self):
        self.inverted_list = self.list_of_numbers[::-1]
        return self

    def print_output(self):
        print(f"Original list of numbers: {self.list_of_numbers}")
        print(f"Inverted list: {self.inverted_list}")

def main():
    Question_04().get_numbers().invert_list().print_output()

main()