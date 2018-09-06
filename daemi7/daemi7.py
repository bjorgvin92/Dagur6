my_int = int(input('Give me an int >= 0: '))

kvoti = my_int
bstr = ''

while True:
    afgangur = kvoti % 2
    kvoti = kvoti // 2
    bstr += str(afgangur)
    if kvoti == 0:
        bstr = bstr[::-1]
        break




print("The binary of", my_int, "is", bstr)