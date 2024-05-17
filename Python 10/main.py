"""
Fayllar: file, byte -lardan ibaretdir

Fayl tipleri:
1 - Binary tipler:
    * pdf, doc, jpg, png
    
2 - Text tipleri:
    * txt, xml, html
"""


"""
Encoding: Datanin byte qurulusu > nece saxladildigi ile bagli

1 - ASCII (128 simvol)
2 - UNICODE (1.114 milyon)

"""


"""
Python fayli acmaq ucun -> open()
"""

# encoding olmadan
# file = open("sozler.txt")
# print(file.read())
# file.close()



# try:
#     file = open("sozler.txt", encoding="utf-8")
#     print(file.read())
#     file.close()
    
# except FileNotFoundError:
#     print("Bele bir fayl movcud deyil...")


"""
with
Context manager
Butun fayl islerini gormek ucun(oxuma, yazma, silme) burada teyin olunur
"""

# with open("sozler.txt", encoding="utf-8") as data:
#     myFile = data.read()
#     print(myFile)



"""
Fayl acma (Modlari):
    * r: oxuma(read)
    * w: yazma(write)
    * a: elave etme(append)
    * x: yaratmaq(create)
    t: text formatinda 
    b: binary formatinda 
    +: update (read + write)  
"""


"""
Numune:
r > Oxuma

with open("sozler.txt", encoding="utf-8", mode="r") as data:
    print(data.read())
"""


"""
Binary formatinda oxuma:

with open("chess.jpg", mode="rb") as data:
    print(data.read())
"""



# -----------------------------------------------------------------
"""
Oxuma - Yazma
Oxuma methodlari:
    * read() - tum fayli oxuyur
    * readline() - yalniz birinci setri oxuyur
    * readlines() - qalan butun setirleri tek tek oxuyur
"""

# Numuneler:

# with open("lorem.txt", mode="rt", encoding="utf-8") as lorem:
#     print(lorem.read())


# ilk 30 simvolu gostermek ucun
# with open("lorem.txt", mode="rt", encoding="utf-8") as lorem:
#     print(lorem.read(30))


# Setir setir oxuma:
# with open("lorem.txt", mode="rt", encoding="utf-8") as lorem:
    # print(lorem.readline())
    

# Tum setirleri list formatinda oxumaq ucun:
# with open("lorem.txt", mode="rt", encoding="utf-8") as lorem:
#     print(lorem.readlines())



# Butun fayli setir setir oxumaq
# with open("lorem.txt", mode="rt", encoding="utf-8") as lorem:
#     for setir in lorem:
#         print(setir.split())


"""
Yazma islerimiz:
    * w -> write: bos file edib ele yazmaga baslayir
    * a -> append: movcud fayla elave ederek yazmaga baslayir
"""

# w ile ac:
# with open("lorem.txt", mode="w") as lorem:
#     lorem.write("Salam Dunya")

# a ile ac:
# with open("lorem.txt", mode="a") as lorem:
#     lorem.write("\nSalam Dunya")


# Bir nece setr elave etmek ucun:
# with open("lorem.txt", mode="a") as lorem:
#     elave__olunacaq__setrler = ['\nMikhail Tal', '\nRobert', "\nMessi"]
#     lorem.writelines(elave__olunacaq__setrler)


# --------------------------------------------------------------------------

"""
Silme - Yeniden Adlandirma - Yaratma

os kitabxanasi ile edilir
"""

import os 
# Yeniden adlandirma > rename()
# os.rename("UpdateLorem.txt", "lorem.txt")


# Silme -> remove()
# os.remove("index.html", "home.html")

# import glob, os
# for f in glob.glob("*.html"):
#     os.remove(f)

# Yarat -> open(...., mode="x")
# with open("NewFile.txt", mode="x", encoding="utf-8") as data:
#     data.write("Salam new file...")
    
    
# Movcud fayl varsa yarada bilmerik
# with open("lorem.txt", mode="x", encoding="utf-8") as data:
#     data.write("Salam new file...")