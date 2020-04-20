import os
from reverse import reverse_chat
from change import change_mds
from backup import backup
postion = 'D:\Blog\source\_posts'
os.chdir(postion)
os.system('copy chat.md ..\\..\\')
backup()
change_mds()
reverse_chat()
os.system('hexo g')
os.system('hexo deploy')
os.system('move ..\\..\\chat.md .\\')
