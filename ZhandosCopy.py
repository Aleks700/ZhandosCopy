import os
import pandas as pd
import shutil
from bs4 import BeautifulSoup


# shutil.copy('C:\Users\A.Agadilov\Desktop\Project\ZhandosFinder\List.xlsx')


path_to_input = r"G:\SKO_MAXAR"
path_to_output = r"C:\Users\A.Agadilov\Desktop\Project\ZhandosFinder\A_R_shape"
excel_path = r"C:\Users\A.Agadilov\Desktop\Project\ZhandosFinder\List.xlsx"


dir_name_part = path_to_input.split("\\")
dirName = "shape"
dirPart = path_to_input[-2] + "_" + path_to_input[-1] + "_" + dirName
path_to_output = os.path.join(os.getcwd(), dirPart)


sheet_name = "Kaz"
column_name = "HR_NAME"


df = pd.read_excel(excel_path, 0)
column_data = df[column_name]
# column_data = df .columns[column_name]  [column_name]

new_xlsx = []
# print("column_data", "HR_2212070338027" in column_data)
# print("column_data", column_data["HR_NAME"])
# print("column_data", column_data[0])
for p in column_data:
    # print(p)
    new_xlsx.append(p.lower())


if not os.path.exists(path_to_output):
    os.mkdir(path_to_output)


for root, dirs, files in os.walk(path_to_input):
    for file in files:
        # print(os.path.join(root, file))

        folder_name = root.split("\\")[-1].split("_")
        # hr_name = folder_name[-2] + "_" + folder_name[-1]
        if file.lower() in new_xlsx:
            print(os.path.join(root, file))
            print("started copy of %s", file)
            shutil.copy(
                os.path.join(root, file),
                os.path.join(path_to_output, file),
            )
