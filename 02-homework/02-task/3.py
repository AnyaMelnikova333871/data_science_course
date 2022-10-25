str = input()
upper_flag = False
lower_flag = False
good_string_flag = False
i = 0
len_of_str = len(str)

if len_of_str >= 8:
    while i < len_of_str:
        char = str[i]

        if char.islower():
            lower_flag = True
        elif char.isupper():
            upper_flag = True
        i += 1
        if upper_flag and lower_flag:
            good_string_flag = True
            break


if good_string_flag:
    print("noice")
else:
    print("try another password")

