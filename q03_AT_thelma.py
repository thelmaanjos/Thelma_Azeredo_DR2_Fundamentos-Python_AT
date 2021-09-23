class Question_03:

    def __init__(self):
        self.list_of_numbers = []
        self.max_range = 2
        self.multiplication_result = 1
        self.A = 0
        self.B = 0

    def ask_for_nums(self):
        i = 0
        while i < self.max_range:
            try:
                inputed_num = int(input("Enter an integer: "))
                self.list_of_numbers.append(inputed_num)
                i+=1
            except ValueError:
                print("This is number is not an integer.")
        return self

    def assign_variables(self):
        self.A = self.list_of_numbers[0]
        self.B = self.list_of_numbers[1]
        return self

    def potencia(self): 
        for i in range(self.B): 
            self.multiplication_result *= self.A 
        return self

    def print_output(self):
        print(f"{self.A} ** {self.B} = {self.multiplication_result}")

def main():
    Question_03().ask_for_nums().assign_variables().potencia().print_output()

main()