# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]
# numbers = []
# for i in range(0, 5):
#     number = int(input('Eded daxil edin: '))
#     numbers.append(number)
# numbers.sort()
# print(numbers)



# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 
# sentence = input('Cumle daxil edin: ')
# allWords = sentence.split(' ')
# answer = ''

# for word in allWords: 
#     sortedWord = ''.join(sorted(word))
#     answer += sortedWord + ' '
# print(answer)


# 3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13

# tebrikler . 4 cehdde 13 reqemeni tapdiz
# n = 13
# tries = 0
# while True:
#     number = int(input('Eded daxil edin: '))
#     if(n > number):
#         print('Daxil etdiyiniz eded asagidi, bextiniz birde sinayin')
#         tries += 1
#         continue
    
#     elif(n < number):
#         print('Daxil etdiyiniz eded yuxaridi, bextiniz birde sinayin')
#         tries += 1
#         continue

#     else: 
#         tries += 1
#         print(f'Tebrikler, ededi {tries} cehdde tapdiniz')
#         break



# # 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)
# for num in range(2, 100):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else: print(num)

nums = [1, 2, 3, 4, 5, 6]

print([x * 2 for x in nums if x * 2 > 5])