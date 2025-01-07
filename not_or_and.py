a = float(input("enter a random number: "))
# b = float(input("enter another random number: "))

# if a > b:
#     print("a ist größer als b")
# elif a < b:
#     print("b ist größer als a")
# elif a <= b:
#     print("kleiner oder gleich")
# elif a != b:
#     print("not equal")
# elif a >= b:
#     print("größer oder gleich")
# else:
#     print("equal")

is_even = (a == 2 and a != -1) or (a % 2 == 0)
if not is_even:
    print("Number is uneven")
else:
    print("Number is even")
