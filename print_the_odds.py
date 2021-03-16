odd = []

for i in range(0, 10):
    user_input = int(input("Enter number "))
    if user_input % 2 != 0:
        odd.append(user_input)

if len(odd) == 0:
    print("No odds")
else:
    print(max(odd))
