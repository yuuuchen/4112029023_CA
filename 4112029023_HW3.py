import os
os.mkdir("CS")

file = open("homework.txt","w+")
with open("homework.txt") as file:
    file.close()
    
with open("homework.txt","w") as file:
    file.write("4112029023_陳又瑜")
    
import shutil
shutil.move("homework.txt","CS")


import time
file_size = os.path.getsize("CS\homework.txt")
print(f'文件大小:{file_size}字節')

modification_time = os.path.getmtime("CS\homework.txt")
print(f'最後修改時間:{modification_time}')

formatted_time = time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')



if os.path.exists("homework.txt"):
    os.remove("homework.txt")
    
import os
shutil.rmtree("CS")




