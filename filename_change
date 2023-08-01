import os
from datetime import datetime
dir_path = R'C:\Users\xxxxxx' // R
dir_list = os.listdir(dir_path)
for i in range(len(dir_list)):
  today= date.today()
  date = today.strftime('%Y%m%d')
  newname = "{}_memo.txt".format(today+i)
  os.rename(os.path.join(dir_path,dir_list[i]),os.path.join(dir_path,newname))
