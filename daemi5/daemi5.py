#Ætla að nota enumerate til þess að telja alla stafi í strengnum. nota isnumber() til þess að komast að því hvort næsti stafur sem tala með IF statement, ef svo hendi ég henni í tóma strenginn.
s = input("Input a string: ")
empty = ''

for counter, value in enumerate(s):
    if str.isdigit(value):
        empty += value

print(empty)