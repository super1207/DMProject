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
@Description: 大漠插件7.1904[系统]API部分的python实现
@FilePath: dmsystem.py
'''

import ctypes
import winreg
import random
import traceback
import ctypes.wintypes

class WinSystem():
    winKernel32 = ctypes.windll.kernel32
    winuser32 = ctypes.windll.LoadLibrary('user32.dll')
    @staticmethod
    def Beep(f,duration)->None:
        is_ok:bool = WinSystem.winKernel32.Beep(f,duration)
        if not is_ok:
            raise Exception('Call Beep failed')
    @staticmethod
    def CheckFontSmooth()->bool:
        ret = ctypes.c_bool()
        SPI_GETFONTSMOOTHING = 0x004A
        is_ok:bool = WinSystem.winuser32.SystemParametersInfoW(SPI_GETFONTSMOOTHING,0, ctypes.pointer(ret), 0)
        if not is_ok:
            raise Exception('Call CheckFontSmooth failed')
        return ret.value
    @staticmethod
    def CheckUAC()->bool:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
        value, typee = winreg.QueryValueEx(key, 'EnableLUA')
        return value == 1
    @staticmethod
    def Delay(mis)->bool:
        is_ok:bool = (WinSystem.winKernel32.Sleep(mis) == 0)
        if not is_ok:
            raise Exception('Call Delay failed')
    @staticmethod
    def Delays(mis_min,mis_max)->bool:
        is_ok:bool =  Delay(random.randint(mis_min,mis_max))
        if not is_ok:
            raise Exception('Call Delays failed')
    @staticmethod
    def DisableCloseDisplayAndSleep() -> None:
        ret = ctypes.c_bool()
        SPI_SETSCREENSAVEACTIVE = 0x0011
        SPIF_SENDWININICHANGE = 0x0002
        is_ok:bool = WinSystem.winuser32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE,0, ctypes.pointer(ret), SPIF_SENDWININICHANGE)
        if not is_ok:
            raise Exception('Call DisableCloseDisplayAndSleep failed')
    @staticmethod
    def DisableFontSmooth() -> None:
        SPI_SETFONTSMOOTHING  = 0x004B
        SPIF_SENDWININICHANGE = 0x0002
        is_ok:bool = WinSystem.winuser32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE,0, 0, SPIF_SENDWININICHANGE)
        if not is_ok:
            raise Exception('Call DisableFontSmooth failed')
    @staticmethod
    def DisablePowerSave() -> None:
        SPI_SETLOWPOWERTIMEOUT  = 0x0051
        SPI_SETPOWEROFFTIMEOUT  = 0x0052
        is_ok:bool = WinSystem.winuser32.SystemParametersInfo(SPI_SETLOWPOWERTIMEOUT,0,0,0)  
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
        is_ok:bool = WinSystem.winuser32.SystemParametersInfo(SPI_SETPOWEROFFTIMEOUT,0,0,0)
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
    @staticmethod
    def DisableScreenSave() -> None:
        SPI_SETSCREENSAVEACTIVE  = 0x0011
        is_ok:bool = WinSystem.winuser32.SystemParametersInfo(SPI_SETSCREENSAVEACTIVE,0,0,0)  
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
    @staticmethod
    def EnableFontSmooth() -> None:
        SPI_SETFONTSMOOTHING  = 0x004B
        SPIF_SENDWININICHANGE = 0x0002
        is_ok:bool = WinSystem.winuser32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE,1,0, SPIF_SENDWININICHANGE)
        if not is_ok:
            raise Exception('Call EnableFontSmooth failed')
    @staticmethod
    def ExitOs(type_) -> None:
        EWX_LOGOFF = 0x0000
        EWX_POWEROFF = 0x0008
        EWX_REBOOT = 0x0002
        EWX_FORCE = 0x0004
        is_ok:bool = False
        if type_ == 0:
            is_ok = WinSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_LOGOFF)
        elif type_ == 1:
            is_ok = WinSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_POWEROFF)
        elif type == 2:
            is_ok = WinSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_REBOOT)
        else:
            raise Exception('Call ExitOs failed')
        if not is_ok:
            raise Exception('Call ExitOs failed')
    @staticmethod
    def GetClipboard() -> str:
        CF_UNICODETEXT = 13
        is_ok:bool = WinSystem.winuser32.OpenClipboard(0)
        if not is_ok:
            raise Exception('Call GetClipboard failed')
        hd=WinSystem.winuser32.GetClipboardData(CF_UNICODETEXT)
        if not hd:
            raise Exception('Call GetClipboard failed:Is not UNICODETEXT')
        ss=ctypes.c_wchar_p(hd) 
        WinSystem.winuser32.CloseClipboard()
        return ss.value
    @staticmethod
    def GetCpuType():
        class _SYSTEM_INFO(ctypes.Structure):
            _fields_ = [
                ("dwOemId",ctypes.wintypes.DWORD),
                ("dwProcessorType",ctypes.wintypes.DWORD),
                ("lpMinimumApplicationAddress",ctypes.wintypes.LPVOID),
                ("lpMaximumApplicationAddress",ctypes.wintypes.LPVOID),
                ("dwActiveProcessorMask",ctypes.wintypes.LPVOID),
                ("dwNumberOfProcessors",ctypes.wintypes.DWORD),
                ("dwProcessorType",ctypes.wintypes.DWORD),
                ("dwAllocationGranularity",ctypes.wintypes.DWORD),
                ("wProcessorLevel",ctypes.wintypes.WORD),
                ("wProcessorRevision",ctypes.wintypes.WORD),
            ]
        lpSystemInfo = _SYSTEM_INFO()
        WinSystem.winKernel32.GetSystemInfo(ctypes.byref(lpSystemInfo))
        if(lpSystemInfo.dwProcessorType in [386,486,586,2200]):
            return 1
        elif lpSystemInfo.dwProcessorType == 8664:
            return 2
        else: return 0
    @staticmethod
    def GetDir(type_):
        if type_ == 0:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = WinSystem.winKernel32.GetCurrentDirectoryA(1000,pathstr)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 1:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = WinSystem.winKernel32.GetSystemDirectoryA(pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 2:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = WinSystem.winKernel32.GetWindowsDirectoryA(pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 3:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = WinSystem.winKernel32.GetTempPathA(1000,pathstr)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 4:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = WinSystem.winKernel32.GetModuleFileNameA(0,pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        else:raise Exception('Call GetDir failed')

    
