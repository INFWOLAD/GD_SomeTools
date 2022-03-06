"""
label、image、traintxt、testtxt verification
only use for testing
cosz
"""

import shutil
import os


def inputfilepath():
    oldpath = input("请输入扫描文件夹路径\n")
    topath = input("请输入目标文件目录（请预先创建好文件夹）\n")
    pathtxt = input("请输入txt所在位置\n")
    return oldpath, topath, pathtxt


def labelcheckinput():
    imagespath = input("请输入images所在文件夹\n")
    labelpath = input("请输入label所在文件夹\n")
    checktopath = input("请输入输出位置(请预先创建好主文件夹，并生成images和labels文件夹）\n")
    return imagespath, labelpath, checktopath


def comparefile(oldpath, txtpath1):
    if oldpath == txtpath1:
        print("目录匹配，开始转移文件")
    else:
        print("目录不匹配，请检查或者调整")


def movefile(oldpath, topath, oldname):
    shutil.move(oldpath, topath)
    print(f"已完成{oldname}转移")


def main():
    mode = input("请输入选择的模式数字：\n0.校验filetxt和images匹配程度并生成新filetxt\n1.校验label和images对应情况并生成新目录\n")
    if mode == "0":
        oldpath, topath, pathtxt = inputfilepath()
        with open(pathtxt, "r+", encoding="utf-8") as txt:
            for lines in txt.readlines():
                lines = lines.strip("\n")
                txtpath1, oldname = os.path.split(lines)
                scanfile = os.path.join(oldpath,oldname)
                if not os.path.exists(scanfile):
                    print(f"该文件不存在{oldname}")
                else:
                    comparefile(oldpath, txtpath1)
                    movefile(scanfile, topath, oldname)
                    outputfile = topath + "\\output.txt"
                    with open(outputfile, "a+", encoding="utf-8") as outfile:
                        new = topath + "\\" + oldname + "\n"
                        outfile.write(new)
            print("已完成")
    elif mode == "1":
        imagespath, labelpath, checktopath = labelcheckinput()
        labelexit = os.listdir(labelpath)
        for lines in labelexit:
            imageline = lines.strip(".txt") + ".jpg"
            # print(lines)
            imagescheck = os.path.join(imagespath, imageline)
            if not os.path.exists(imagescheck):
                print("{lines}label对应图片未找到")
            else:
                newimagespath = checktopath + "\\images"
                oldlabelpath = os.path.join(labelpath, lines)
                newlabelpath = checktopath + "\\labels"
                movefile(imagescheck, newimagespath, imageline)
                movefile(oldlabelpath, newlabelpath, lines)
        print("已完成")
    else:
        print("输入错误")


if __name__ == '__main__':
    main()
