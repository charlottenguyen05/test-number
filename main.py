from distutils.dir_util import copy_tree
import os
import xlsxwriter

INPUT_FILE_PATH = input("Your input file path: ")
OUTPUT_FILE_PATH = input("Your output file path: ")  # Ask for your desirable file path for your output (it mustn't already exists)
x = input("What number do you like to add up: ")

copy_tree(INPUT_FILE_PATH, OUTPUT_FILE_PATH) # Copy everything from folder INPUT -> folder OUTPUT

new_name_list = []  
path = os.listdir(path=OUTPUT_FILE_PATH) # List contains the names of the subfolders in the "ID number" folder
for i in path:
    # Rename folders from format G123 to format P(123+x)
    tuple_ = i.rpartition("G")
    a = int(tuple_[2])+int(x)
    new_name_list.append(f"P{str(a).zfill(3)}")

for fn in range(len(new_name_list)):
    # Rename all subfolders in the output folder to the correct format
    os.rename(os.path.join(OUTPUT_FILE_PATH, path[fn]),
              os.path.join(OUTPUT_FILE_PATH, new_name_list[fn]))

# --------------------- CREATE AND WRITE TO EXCEL --------------------- #
workbook = xlsxwriter.Workbook("id-alter-score.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ID Number')
worksheet.write('B1', 'Code')
worksheet.write('C1', 'Score')

row = 1
column = 0
for item in path:
    worksheet.write(row, column, item)
    row += 1

row = 1
column = 1
for item in new_name_list:
    worksheet.write(row, column, item)
    row += 1

workbook.close()
