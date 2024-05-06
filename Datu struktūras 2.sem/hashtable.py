class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def add_entry(self, number, name):
        self.phonebook[number] = name

    def delete_entry(self, number):
        if number in self.phonebook:
            del self.phonebook[number]

    def find_entry(self, number):
        if number in self.phonebook:
            return self.phonebook[number]
        else:
            return "not found"


def main():
    n = int(input())
    phone_book = PhoneBook()

    for _ in range(n):
        query = input().split()
        command = query[0]
        number = int(query[1])

        if command == "add":
            name = query[2]
            phone_book.add_entry(number, name)
        elif command == "delete":
            phone_book.delete_entry(number)
        elif command == "find":
            print(phone_book.find_entry(number))


if __name__ == "__main__":
    main()
