import re
import os
import time
import upload

postion = 'D:\Blog\source\_posts'

uploader = upload.smms()
uploader.login()


def change_md(filename):
    f = open(filename, 'rb')
    article_content = f.read().decode()
    pic_block = re.findall(r'!\[.*?\)', article_content)  # 获取所有图片路径
    pic_local = []
    for i in range(len(pic_block)):
        path = re.findall(r'\((.*?)\)', pic_block[i])[0]
        if 'https' not in path:  # 只获取本地图片路径
            pic_local.append(path)
    if len(pic_local) != 0: print("There are " + str(len(pic_local)) + ' pics need uploaded')
    for i in range(len(pic_local)):
        pic_new_url = uploader.upload(pic_local[i])  # upload !
        if pic_new_url != "Error":
            article_content = article_content.replace(
                pic_local[i], pic_new_url)
            print(str(i + 1) + '/' + str(len(pic_local)), "Done")
    f.close()
    if len(pic_local) != 0:
        with open(filename, 'wb') as f:
            f.write(str(article_content).encode())
def change_mds():
    dirlist = os.listdir(postion)
    for i in dirlist:
        path = postion + '\\' + i
        change_md(path)





