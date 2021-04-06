import sys

import os


def rename(pic_path):
    piclist = os.listdir(pic_path)
    i = 1
    print("ok")
    for pic in piclist:
        if pic.endswith(".wav"):   # wave格式的音频文件
            old_path = os.path.join(os.path.abspath(pic_path), pic)
            new_path = os.path.join(os.path.abspath(pic_path), str(
                2000 + (int(i))) + '.wav')  # 这里对当前目录下文件进行排序，第一个我设置成1001、1002、1003这种的

            os.renames(old_path, new_path)
            print("把原命名格式：" + old_path + u"转换为新命名格式：" + new_path)
            i = i + 1


if __name__ == '__main__':
    rename("./文件夹名/")  # 把文件夹名改成对应的文件夹名


