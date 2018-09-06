#
s = input("Input a string: ")

for counter, value in enumerate(s):
    if value == 'o':
        print(counter)