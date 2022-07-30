import random


def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip("\n") for s in flist]


def main():
    quotes = remove_newlines("quotes.txt")
    print("Welcome to the Random Quote Generator!")
    count = input("How many quotes would you like to generate? ")

    for i in range(0, int(count)):
        print(f"{i + 1}. {random.choice(quotes)}")

    print("-" * 50)
    print("Thanks for using the Random Quote Generator!")
    again = input("Would you like to generate another quote? (y/n) ")
    if again == "y":
        main()


if __name__ == "__main__":
    main()
