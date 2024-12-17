import random

secret_number = random.randint(1, 100)

print("I've chosen a number, gl with your choice!")

chosen_number = input("guess my number: ")
print(f"you've chosen {chosen_number}!")


if int(chosen_number) > secret_number:
    print("you're thinking too big my friend!")
elif int(chosen_number) < secret_number:
    print("think bigger!")
else:
    print("wow, you are lucky!")

richtig = False

while not richtig:
    chosen_number = int(input("guess my number: "))
    if chosen_number < secret_number:
        print("think bigger!")
    elif chosen_number > secret_number:
        print("you're thinking too big my friend!")
    else:
        print("Jackpot")
        richtig = True
