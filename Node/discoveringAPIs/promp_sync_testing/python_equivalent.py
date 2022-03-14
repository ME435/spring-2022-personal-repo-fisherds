def main():
    print("Ready")
    while True:
        answer = input("What is your name? ")
        if answer == "":
            print("Goodbye")
            break
        print(f"Hello, {answer}!")

main()