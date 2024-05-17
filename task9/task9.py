with open('file1.txt', mode='w') as data:
    data.write('salam necesen')


with open('file1.txt', mode="rt", encoding="utf-8") as data:
    dataWithUpper = data.read().upper()
    print(dataWithUpper)

with open('file2.txt', mode='w') as data:
    data.write(dataWithUpper)