exit = soma = count = 0
while exit != 999:
    num = int(input("type a number [999 to exit]:"))
    if num != 999:
        soma += num
        count += 1
    exit = num
print(f"You typed {count} numbers and their sum is {soma}!")