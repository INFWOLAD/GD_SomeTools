"""该脚本用于将所有的分开的文件夹下同文件名的文件转移到唯一文件夹下"""
import os.path
import shutil


def inputfilepath():
    oldpath = input("请输入要进行整理的文件夹路径")
    newpath = input("请输入目标文件夹位置")
    return oldpath, newpath


def movefile(imagespath, newimagespath):
    shutil.copy(imagespath, newimagespath)
    print(f"已完成{imagespath}的移动")


def main():
    oldpath, newpath = inputfilepath()
    oldpathall = os.listdir(oldpath)
    for i in range(len(oldpathall)):
        print(len(oldpathall))
        oldfileall = os.listdir(os.path.join(oldpath, oldpathall[i]))
        for j in range(len(oldfileall)):
            print(len(oldfileall))
            nowpath = os.path.join(os.path.join(oldpath, oldpathall[i]),oldfileall[j])
            nowpath1, nowname = os.path.split(nowpath)
            nowpath11, nowpath12 = os.path.split(nowpath1)
            newname = str(nowpath12 + "_" + nowname)
            movefile(nowpath, os.path.join(newpath, newname))
    print("已完成所有文件迁移")

if __name__ == '__main__':
    main()
