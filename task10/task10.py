import os
import shutil

main_directory = 'main_directory'
sub_directory = os.path.join(main_directory, 'sub_directory')
file_path = os.path.join(sub_directory, 'file.txt')
image_path = 'example_image.png'

os.makedirs(main_directory, exist_ok=True)

os.makedirs(sub_directory, exist_ok=True)

with open(file_path, 'w') as file:
    file.write("This is a sample text.")

shutil.move(image_path, sub_directory)

for file_name in os.listdir(sub_directory):
    if file_name.endswith('.txt'):
        full_file_path = os.path.join(sub_directory, file_name)
        shutil.move(full_file_path, main_directory)



#---------------------------------------------------------------------------------------------------------------------------------
xallar = [5, 3, 4, 2, 1]
sorted_xallar = sorted(xallar)

for i in range(len(xallar)):
    tutdugu_yer = str(len(xallar) - sorted_xallar.index(xallar[i]))

    sonluq = 'ci'
    if tutdugu_yer.endswith(('1', '2', '5', '7', '8', '20', '50', '70', '80')):
        sonluq = 'ci'
    elif tutdugu_yer.endswith(('3', '4', '9', '10', '30')):
        sonluq = 'cu'
    elif tutdugu_yer.endswith(('6', '40', '60', '90')):
        sonluq = 'cı'
    xallar[i] = tutdugu_yer + sonluq

print(xallar)