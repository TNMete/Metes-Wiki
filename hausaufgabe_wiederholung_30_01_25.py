# - Exercise 1

# name = input("Bitte gib deinen Namen ein: ")
# age = int(input("enter your age: "))
# yourage = 2025 - age + 100

# print(f"Hello {name}, you will be 100 years old in the year {yourage}")

# - Exercise 2

# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("this is an uneven number.")
# else:
#     print("this is an even number.")

# - Exercise 3

# liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for x in liste:
#     if x < 5:
#         print(x)

# - Exercise 4

# num = int(input("choose a number: "))

# listRange = list(range(1, num + 1))

# liste = []

# for number in listRange:
#     if num % number == 0:
#         liste.append(number)

# print(liste)

# - Exercise 5

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# compare = list(set(a) & set(b))

# print(compare)

# - Exercise 6

# def ist_palindrom(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]


# def main():
#     eingabe = input("Gib einen String ein: ")

#     if ist_palindrom(eingabe):
#         print("Der String ist ein Palindrom.")
#     else:
#         print("Der String ist kein Palindrom.")


# if __name__ == "__main__":
#     main()

# - Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [number for number in a if number % 2 == 0]

print(b)
