import random as r 

upper_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 's', 'y', 'x', 'z']
lower_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'S', 'Y', 'X', 'Z']
symbols = ['!','@','#','$','(',')','_']
numbers = [1,2,3,4,5,6,7,8,9,0]
lenght = int(input("Введите длину пароля: "))
password = ''
for i in range(lenght):
    letter = r.randint(1, 5)
    if letter == 1:
        password = password + r.choice(upper_case)
    elif letter == 2:
        password = password + r.choice(lower_case)
    elif letter == 3:
        password = password + r.choice(symbols)
    elif letter == 4:
        password = password + str(r.choice(numbers))
print(password)
