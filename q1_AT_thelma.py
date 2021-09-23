class Question_01:

    def __init__(self):
        self.tuple = (46, 10, 8)
        
    def print_ascended_tuple(self):
        for num in self.tuple:
            if not isinstance(num, int):
                print("This tuple does not contain 3 integers.")
                return
        print(sorted(self.tuple))

def main():
    Question_01().print_ascended_tuple()

main()