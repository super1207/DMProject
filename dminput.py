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
@Description: 大漠插件7.1904[键鼠]API部分的python实现
@FilePath: dminput.py
'''

import ctypes
import ctypes.wintypes
import time
import random

class DMInput():
    winKernel32 = ctypes.windll.kernel32
    winuser32 = ctypes.windll.LoadLibrary('user32.dll')
    key_table = {"1":49,
                "2":50,
                "3":51,
                "4":52,
                "5":53,
                "6":54,
                "7":55,
                "8":56,
                "9":57,
                "0":48,
                "-":189,
                "=":187,
                "back":8,
                "a":65,
                "b":66,
                "c":67,
                "d":68,
                "e":69,
                "f":70,
                "g":71,
                "h":72,
                "i":73,
                "j":74,
                "k":75,
                "l":76,
                "m":77,
                "n":78,
                "o":79,
                "p":80,
                "q":81,
                "r":82,
                "s":83,
                "t":84,
                "u":85,
                "v":86,
                "w":87,
                "x":88,
                "y":89,
                "z":90,
                "ctrl":17,
                "alt":18,
                "shift":16,
                "win":91,
                "space":32,
                "cap":20,
                "tab":9,
                "~":192,
                "esc":27,
                "enter":13,
                "up":38,
                "down":40,
                "left":37,
                "right":39,
                "option":93,
                "print":44,
                "delete":46,
                "home":36,
                "end":35,
                "pgup":33,
                "pgdn":34,
                "f1":112,
                "f2":113,
                "f3":114,
                "f4":115,
                "f5":116,
                "f6":117,
                "f7":118,
                "f8":119,
                "f9":120,
                "f10":121,
                "f11":122,
                "f12":123,
                "[":219,
                "]":221,
                "\\":220,
                ";":186,
                "'":222,
                ":":188,
                ".":190,
                "/":191}
    

    @staticmethod
    def EnableMouseAccuracy(enable) -> bool:
        SPI_SETMOUSE = 0x0004
        SPI_GETMOUSE = 0x0003
        SPIF_SENDCHANGE = 0x0002
        aMouseInfo=(ctypes.c_uint32*3)(6,10,1)
        DMInput.winuser32.SystemParametersInfoA(SPI_GETMOUSE,0,ctypes.pointer(aMouseInfo),0)
        last = aMouseInfo[2]
        if enable:
            aMouseInfo=(ctypes.c_uint32*3)(6,10,1)
        else:
            aMouseInfo=(ctypes.c_uint32*3)(0,0,0)
        retnum = DMInput.winuser32.SystemParametersInfoA(SPI_SETMOUSE,0,ctypes.pointer(aMouseInfo),SPIF_SENDCHANGE)
        return last == 1
    @staticmethod
    def GetCursorPos() -> tuple:
        class POINT(ctypes.Structure):
            _fields_ = [
                ("x",ctypes.wintypes.LONG),
                ("y",ctypes.wintypes.LONG)
            ]
        point = POINT()
        DMInput.winuser32.GetCursorPos(ctypes.byref(point))
        return (point.x,point.y)
    @staticmethod
    def GetCursorShape() -> int:
        class POINT(ctypes.Structure):
            _fields_ = [
                ("x",ctypes.wintypes.LONG),
                ("y",ctypes.wintypes.LONG)
            ]
        hCursor = None
        point = POINT()
        DMInput.winuser32.GetCursorPos(ctypes.byref(point))
        hWnd = DMInput.winuser32.WindowFromPoint(point)
        dwThreadID = DMInput.winuser32.GetWindowThreadProcessId(hWnd, 0)
        dwCurrentThreadID = DMInput.winKernel32.GetCurrentThreadId()
        if dwCurrentThreadID != dwThreadID:
            if DMInput.winuser32.AttachThreadInput(dwCurrentThreadID, dwThreadID, True):
                hCursor = DMInput.winuser32.GetCursor()
                DMInput.winuser32.AttachThreadInput(dwCurrentThreadID, dwThreadID, False)
        else:
            hCursor = DMInput.winuser32.GetCursor()
        return hCursor
    @staticmethod
    def GetCursorShape(type_) -> int:
        return GetCursorShape()
    @staticmethod
    def GetCursorSpot() -> tuple:
        return GetCursorPos()
    @staticmethod
    def GetKeyState(vk_code) -> bool:
        return (DMInput.winuser32.GetKeyState(vk_code)>>15) == 1
    @staticmethod
    def GetMouseSpeed() -> int:
        SPI_GETMOUSESPEED = 0x0070
        speed = ctypes.c_int32()
        DMInput.winuser32.SystemParametersInfoA(SPI_GETMOUSESPEED,0,ctypes.pointer(speed),0)
        return int((speed.value+2)/2)
    @staticmethod
    def KeyDown(vk_code) -> None:
        DMInput.winuser32.keybd_event(vk_code,0,0,0)
    @staticmethod
    def KeyDownChar(key_str) -> None:
        DMInput.winuser32.keybd_event(DMInput.key_table[key_str],0,0,0)
    @staticmethod
    def KeyPress(vk_code) -> None:
        KEYEVENTF_KEYUP = 0x0002
        DMInput.winuser32.keybd_event(vk_code,0,0,0)
        DMInput.winuser32.keybd_event(vk_code,0,KEYEVENTF_KEYUP,0)
    @staticmethod
    def KeyPressChar(key_str) -> None:
        KEYEVENTF_KEYUP = 0x0002
        DMInput.winuser32.keybd_event(DMInput.key_table[key_str],0,0,0)
        DMInput.winuser32.keybd_event(DMInput.key_table[key_str],0,KEYEVENTF_KEYUP,0)
    @staticmethod
    def KeyPressStr(key_str,delay) -> None:
        for ch in key_str:
            DMInput.KeyPressChar(ch)
            time.sleep(delay/1000)
    @staticmethod
    def KeyUp(vk_code) -> None:
        KEYEVENTF_KEYUP = 0x0002
        DMInput.winuser32.keybd_event(vk_code,0,KEYEVENTF_KEYUP,0)
    @staticmethod
    def KeyUpChar(key_str) -> None:
        KEYEVENTF_KEYUP = 0x0002
        DMInput.winuser32.keybd_event(DMInput.key_table[key_str],0,KEYEVENTF_KEYUP,0)
    @staticmethod
    def LeftClick() -> None:
        DMInput.LeftDown()
        DMInput.LeftUp()
    @staticmethod
    def LeftDoubleClick() -> None:
        DMInput.LeftClick()
        time.sleep(0.01)
        DMInput.LeftClick()
    @staticmethod
    def LeftDown() -> None:
        MOUSEEVENTF_LEFTDOWN = 0x0002
        DMInput.winuser32.mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    @staticmethod
    def LeftUp() -> None:
        MOUSEEVENTF_LEFTUP = 0x0004
        DMInput.winuser32.mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
    @staticmethod
    def MiddleClick() -> None:
        DMInput.MiddleDown()
        DMInput.MiddleUp()
    @staticmethod
    def MiddleDown() -> None:
        MOUSEEVENTF_MIDDLEDOWN = 0x0020
        DMInput.winuser32.mouse_event(MOUSEEVENTF_MIDDLEDOWN,0,0,0,0)
    @staticmethod
    def MiddleUp() -> None:
        MOUSEEVENTF_MIDDLEUP = 0x0040
        DMInput.winuser32.mouse_event(MOUSEEVENTF_MIDDLEUP,0,0,0,0)
    def MoveR(rx,ry) -> None:
        MOUSEEVENTF_MOVE = 0x0001
        DMInput.winuser32.mouse_event(MOUSEEVENTF_MOVE,rx,ry,0,0)
    def MoveTo(x,y) -> None:
        MOUSEEVENTF_MOVE = 0x0001
        MOUSEEVENTF_ABSOLUTE  = 0x8000
        SM_CXSCREEN = 0
        SM_CYSCREEN = 1
        cx_screen = DMInput.winuser32.GetSystemMetrics(SM_CXSCREEN)
        cy_screen = DMInput.winuser32.GetSystemMetrics(SM_CYSCREEN)
        real_x = round(65535 * x / cx_screen)
        real_y = round(65535 * y / cy_screen)
        DMInput.winuser32.mouse_event(MOUSEEVENTF_ABSOLUTE|MOUSEEVENTF_MOVE,real_x,real_y,0,0)
    def MoveToEx(x,y,w,h) -> None:
        DMInput.MoveTo(x + random.randint(0,w),y + random.randint(0,h))
    @staticmethod
    def RightClick() -> None:
        DMInput.RightDown()
        DMInput.RightUp()
    @staticmethod
    def RightDown() -> None:
        MOUSEEVENTF_RIGHTDOWN = 0x0008
        DMInput.winuser32.mouse_event(MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    @staticmethod
    def RightUp() -> None:
        MOUSEEVENTF_RIGHTUP = 0x0010
        DMInput.winuser32.mouse_event(MOUSEEVENTF_RIGHTUP,0,0,0,0)
    @staticmethod
    def SetMouseSpeed(speed) -> None:
        setspeed = ctypes.c_int32([0,1,2,4,6,8,10,12,14,16,18,20][speed])
        DMInput.winuser32.SystemParametersInfoA(113, 0,setspeed, 2 | 1)
    @staticmethod
    def WaitKey(vk_code,time_out) -> bool:
        intm = time.time()
        while True:
            if((time.time() - intm)*1000>time_out):return False
            if vk_code != 0:
                if(bool(DMInput.winuser32.GetAsyncKeyState(vk_code)&0x8000)):
                    return True
            else:
                for (k,v) in DMInput.key_table.items():
                    if DMInput.GetKeyState(v):
                        return True
        return True
    @staticmethod
    def WheelDown() -> None:
        MOUSEEVENTF_WHEEL = 0x0800
        DMInput.winuser32.mouse_event(MOUSEEVENTF_WHEEL,0,0,-20,0)
    @staticmethod
    def WheelUp() -> None:
        MOUSEEVENTF_WHEEL = 0x0800
        DMInput.winuser32.mouse_event(MOUSEEVENTF_WHEEL,0,0,20,0)
