x = 200

def closest_number(a, b, c):
    diff1 = abs(a - x)
    diff2 = abs(b - x)
    diff3 = abs(c - x)

    if diff1 < diff2 and diff1 < diff3:
        return "A", a
    elif diff2 < diff1 and diff2 < diff3:
        return "B", b
    elif diff3 < diff1 and diff3 < diff2:
        return "C", c
    else:
        return "All", "There is a tie"


print("Find the closest number to", x)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

letter, value = closest_number(num1, num2, num3)

if letter == "All":
    print("There is a tie. Some numbers are equally close to", x)
else:
    print(f"Letter {letter} or {value} is the closest number to {x}")