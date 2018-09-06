name = input("Input a name: ")
bil = name.find(' ')
single_stafur = (name[bil+1:bil+2])

print(f'{single_stafur.upper()}. {name[:bil-1].capitalize()}')