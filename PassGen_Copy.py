import random
import string

def main():
    choice =[]
    print("Password Generator")
    print("1. Upper case letters")
    print("2. Lower case letters")
    print("3. Special Characters")
    print("4. Numbers")
    # print("5. Exit")

    n = int(input("How many choice want to include: "))
    for i in range(n):
        value = int(input("Enter option number: "))
        if 1 <= value <= 4:
            choice.append(value)
        else:
            print("Invalid Number! Enter between 1 and 4")

    length = int(input("Length of password: "))
    if length < len(choice):
        print("Invalid length")
        return
    else:
        eachlen = length // len(choice)
        extralen = length % len(choice)


    # if extralen!=0:
    #     for j in range(1, extralen+1):
    #         choice.append(j)

    result=[]

    for i in choice:

        if i == 1:
            # if extralen >0:
            #     result.extend(random.choices(string.ascii_uppercase, k=eachlen+1))
            # else:
            #     result.extend(random.choices(string.ascii_uppercase, k=eachlen))

            result.extend(random.choices(string.ascii_uppercase, k=eachlen + (1 if extralen > 0 else 0)))

        elif i == 2:
            # if extralen >0:
            #     result.extend(random.choices(string.ascii_lowercase, k=eachlen+1))
            # else:
            #     result.extend(random.choices(string.ascii_lowercase, k=eachlen))

            result.extend(random.choices(string.ascii_lowercase, k=eachlen + (1 if extralen > 0 else 0)))


        elif i == 3:
            if extralen >0:
                result.extend(random.choices(string.punctuation, k=eachlen+1))
            else:
                result.extend(random.choices(string.punctuation, k=eachlen))

        elif i == 4:
            # rand_num = random.choices(string.digits, k=length)
            # rand_num = "".join(rand_num)
            # # print(rand_num)
            # result += rand_num
            if extralen >0:
                result.extend(random.choices(string.digits, k=eachlen+1))
            else:
                result.extend(random.choices(string.digits, k=eachlen))

        else:
            print("Invalid")

        extralen-=1

    # print(result)
    random.shuffle(result)

    finalres = ''.join(result)
    print(f"Your Password: {finalres}")

        # elif choice == 5:
        #     break

if __name__ == "__main__":
    main()

