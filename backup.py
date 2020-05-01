from_folder = 'D:\\Blog\\source\\_posts'
to_folder = 'D:\\Blog\\backup'


import os
import time
def backup():
    localtime = time.localtime(time.time())
    foder_name = to_folder + '\\' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    
    os.mkdir(foder_name)
    os.system('copy ' + from_folder + ' ' + foder_name)

