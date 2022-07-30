import random


def remove_newlines(fname):
    flist = open(fname, encoding="utf-8").readlines()
    return [s.rstrip("\n") for s in flist]


def insert_quotes(fname):
    count_insert = input("How many quotes would you like to insert? ")
    f = open(fname, "a")
    for i in range(0, int(count_insert)):
        quote = input(f"Enter the new quote({i + 1}) : ")
        if len(quote) > 0:
          f.write("%s\n" % quote)
    f.close()


def main():
    filename = "quotes.txt"
    quotes = remove_newlines(filename)
    print("\nWelcome to the Random Quote Generator!")
    print("1. Get a random quote\n2. Insert quotes")
    state = input("Enter your choice = ")

    if state == "1":
        generate = "y"
        while generate == "y":
            print("\nHere's a random quote: ")
            print("-" * 50)
            print(f'"{random.choice(quotes)}"')
            print("-" * 50 + "\n")
            generate = input("generate another quote? (y/n) ")
    elif state == "2":
        insert_quotes("quotes.txt")
        print("Quote inserted successfully!")

    print("-" * 50)
    print("Thanks for using the Random Quote Generator!")
    again = input("Would you like to using random quote generator again? (y/n) ")
    if again == "y":
        main()


if __name__ == "__main__":
    main()
