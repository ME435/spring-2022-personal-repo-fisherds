def main():
    print("Ready")

    while True:
        name = input("What is your name? ")
        if name == "":
            print("Goodbye")
            break
        print(f"Hello, {name}!")


main()
