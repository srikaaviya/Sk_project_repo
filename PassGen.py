import random
import string
import csv
import os

def main():
    choice =[]

    
    print("Password Generator")
    print("1. Upper case letters")
    print("2. Lower case letters")
    print("3. Special Characters")
    print("4. Numbers")

    n = int(input("How many choice want to include: "))
    for i in range(n):
        value = int(input("Enter option number: "))
        if 1 <= value <= 4:
            choice.append(value)
        else:
            print("Invalid Number! Enter between 1 and 4")

    while True:
        length = int(input("Length of password: "))
        if length >= len(choice):
            eachlen = length // len(choice)
            extralen = length % len(choice)
            break
        else:
            print("Invalid length!")

    result=[]
    for i in choice:
        chars_to_add = eachlen + (1 if extralen > 0 else 0)

        char_sets = {
            1: string.ascii_uppercase,
            2: string.ascii_lowercase,
            3: string.punctuation,
            4: string.digits
        }

        result.extend(random.choices(char_sets[i], k=chars_to_add))
        extralen -= 1

    random.shuffle(result)
    finalres = ''.join(result)
    print(f"Your Password: {finalres}")

    print("Do you want to save the password? (Yes/No)")
    save_choice = input("Enter your choice: ").lower().strip()
    if save_choice=="no":
        return
    else:
        label = input("Enter username/Label for password: ")
        file_name = "savedpass.csv"

        if os.path.exists(file_name):
            with open(file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([label, finalres])
        else:
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["UserName/Label", "Password"])
                writer.writerow([label, finalres])

        print("Password saved!")


if __name__ == "__main__":
    main()

