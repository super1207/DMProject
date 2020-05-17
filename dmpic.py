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
@Description: 大漠插件7.1904[图色]API部分的python实现
@FilePath: dmpic.py
'''
import win32gui, win32ui, win32con
from PIL import Image

class DMPIC():

    @staticmethod
    def Capture(x1, y1, x2, y2, file) -> None:
        hwndDC = win32gui.GetWindowDC(0)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, x2-x1, y2-y1)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (x2-x1, y2-y1), mfcDC, (x1, y1), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, file)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(0,hwndDC)
    
    @staticmethod
    def CapturePng(x1, y1, x2, y2, file) -> None:
        hwndDC = win32gui.GetWindowDC(0)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, x2-x1, y2-y1)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (x2-x1, y2-y1), mfcDC, (x1, y1), win32con.SRCCOPY)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        try:
            pil_image = Image.frombuffer('RGB',(bmpinfo['bmWidth'], bmpinfo['bmHeight']),bmpstr,'raw', 'BGRX', 0, 1)
            pil_image.save(file)
        except:
            raise Exception('call CapturePng failed')
        finally:
            win32gui.DeleteObject(saveBitMap.GetHandle())
            saveDC.DeleteDC()
            mfcDC.DeleteDC()
            win32gui.ReleaseDC(0,hwndDC)

    @staticmethod
    def CaptureJpg(x1, y1, x2, y2, file) -> None:
        DMPIC.CapturePng(x1, y1, x2, y2, file) # PIL可以根据拓展名来自动选择保存类型

# test
# import time
# t1 = time.time()
# DMPIC.Capture(0,0,600,600,"aaa.bmp")
# t2 = time.time()
# DMPIC.CapturePng(0,0,600,600,"aaa.png")
# t3 = time.time()
# DMPIC.CaptureJpg(0,0,600,600,"aaa.jpg")
# t4 = time.time()
# print(t2-t1,t3-t2,t4-t3)
