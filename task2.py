# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# import math

# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
# def listSqrt(list):
#     sqrtNums = []
#     for x in list:
#         if x <= 0 or int(math.sqrt(x)) * int(math.sqrt(x)) != x: 
#             continue
#         else: 
#             sqrtNums.append(int(math.sqrt(x)))

#     return sqrtNums

# print(listSqrt(mylist))


#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']
# a = [-1,1,2,2,6,7,7,'say']
# def nonRepeative(myList):
#     return [x for x in myList if myList.count(x) < 2]

# print(nonRepeative(a))

# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın
# a = input('Reqemler daxil edin?\n')
# def getMultip(inp):
#     sum = 1
#     for a in inp.split():
#         sum *= int(a)

#     return sum

# print(getMultip(a))

# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
# num = int(input('Eded daxil edin\n'))
# print([x for x in range(1, num + 1) if num % x == 0])


# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}
# mylist=['may','iyun','iyul']

# print({x: len(x) for x in mylist})

# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# print([x.split()[0].lower() for x in names])

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results = []
# for i in range(len(nums1)):
#     results.append((nums1[i] + nums2[i]) / 2)

# print(results)


# results=[ 2.5, 3.5, 4.5]
