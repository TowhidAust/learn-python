i = 1
temp = 10
space = 0
while i <= 10:
    my_space = ""
    if i == 0:
        my_space = space * ""
    else:
        my_space = space * " "

    print(my_space + temp * " * ")

    temp = temp - 1
    space = space + 1
    i = i + 1
