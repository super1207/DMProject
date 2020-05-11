'''
/*
 * Copyright 2020 DMProject and contributors.
 *
 * 此源代码的使用受 GNU AFFERO GENERAL PUBLIC LICENSE version 3 许可证的约束, 可以在以下链接找到该许可证.
 * Use of this source code is governed by the GNU AGPLv3 license that can be found through the following link.
 *
 * https://github.com/super1207/DMProject/blob/master/LICENSE
 */
'''

'''
@Description: 大漠插件7.1904[文件]API部分的python实现
@FilePath: dmfile.py
'''

import shutil
import os
import urllib.request
import tkinter
import tkinter.filedialog


class DMFile():
    # winKernel32 = ctypes.windll.kernel32
    # winuser32 = ctypes.windll.LoadLibrary('user32.dll')
    # wingdi32 = ctypes.windll.LoadLibrary('gdi32.dll')
    # winntdll = ctypes.windll.LoadLibrary('ntdll.dll')
    # winwinmm = ctypes.windll.LoadLibrary('winmm.dll')
    @staticmethod
    def CopyFile(src_file,dst_file,over)->None:
        if over:
            shutil.copyfile(src_file, dst_file)
        else:
            if not IsFileExist(dst_file):
                shutil.copyfile(src_file, dst_file)
    @staticmethod
    def CreateFolder(folder)->None:
        os.makedirs(folder)
    @staticmethod
    def DeleteFile(file)->None:
        os.remove(file)
    @staticmethod
    def DeleteFolder(folder)->None:
        os.removedirs(folder)
    @staticmethod
    def DownloadFile(url,save_file,timeout)->None:
        urllib.request.urlretrieve(url, save_file,timeout = timeout / 1000)
    @staticmethod
    def GetFileLength(file) -> int:
        return os.path.getsize(file)
    @staticmethod
    def IsFileExist(file) -> bool:
        return os.path.isfile(file)
    @staticmethod
    def IsFolderExist(folder) ->bool:
        return os.path.isdir(folder)
    @staticmethod
    def MoveFile(src_file,dst_file) -> None:
        shutil.move(src_file,dst_file)
    @staticmethod
    def ReadFile(file) -> str:
        with open(file,'r',encoding='GB2312') as f:
            return f.read()
    @staticmethod
    def SelectDirectory() ->str:
        root = tkinter.Tk()
        root.withdraw()
        return tkinter.filedialog.askdirectory()
    @staticmethod
    def SelectFile() -> str:
        root = tkinter.Tk()
        root.withdraw()
        return tkinter.filedialog.askopenfilename()
    @staticmethod
    def WriteFile(file,content) -> None:
        with open(file,'a',encoding="GB2312") as f:
            f.write(content)
