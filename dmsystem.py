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
import urllib.request
import time
import platform
import uuid
import subprocess



class DMSystem():
    winKernel32 = ctypes.windll.kernel32
    winuser32 = ctypes.windll.LoadLibrary('user32.dll')
    wingdi32 = ctypes.windll.LoadLibrary('gdi32.dll')
    winntdll = ctypes.windll.LoadLibrary('ntdll.dll')
    winwinmm = ctypes.windll.LoadLibrary('winmm.dll')
    @staticmethod
    def Beep(f,duration)->None:
        is_ok:bool = DMSystem.winKernel32.Beep(f,duration)
        if not is_ok:
            raise Exception('Call Beep failed')
    @staticmethod
    def CheckFontSmooth()->bool:
        ret = ctypes.c_bool()
        SPI_GETFONTSMOOTHING = 0x004A
        is_ok:bool = DMSystem.winuser32.SystemParametersInfoW(SPI_GETFONTSMOOTHING,0, ctypes.pointer(ret), 0)
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
        is_ok:bool = (DMSystem.winKernel32.Sleep(mis) == 0)
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
        is_ok:bool = DMSystem.winuser32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE,0, ctypes.pointer(ret), SPIF_SENDWININICHANGE)
        if not is_ok:
            raise Exception('Call DisableCloseDisplayAndSleep failed')
    @staticmethod
    def DisableFontSmooth() -> None:
        SPI_SETFONTSMOOTHING  = 0x004B
        SPIF_SENDWININICHANGE = 0x0002
        is_ok:bool = DMSystem.winuser32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE,0, 0, SPIF_SENDWININICHANGE)
        if not is_ok:
            raise Exception('Call DisableFontSmooth failed')
    @staticmethod
    def DisablePowerSave() -> None:
        SPI_SETLOWPOWERTIMEOUT  = 0x0051
        SPI_SETPOWEROFFTIMEOUT  = 0x0052
        is_ok:bool = DMSystem.winuser32.SystemParametersInfo(SPI_SETLOWPOWERTIMEOUT,0,0,0)  
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
        is_ok:bool = DMSystem.winuser32.SystemParametersInfo(SPI_SETPOWEROFFTIMEOUT,0,0,0)
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
    @staticmethod
    def DisableScreenSave() -> None:
        SPI_SETSCREENSAVEACTIVE  = 0x0011
        is_ok:bool = DMSystem.winuser32.SystemParametersInfo(SPI_SETSCREENSAVEACTIVE,0,0,0)  
        if not is_ok:
            raise Exception('Call DisablePowerSave failed')
    @staticmethod
    def EnableFontSmooth() -> None:
        SPI_SETFONTSMOOTHING  = 0x004B
        SPIF_SENDWININICHANGE = 0x0002
        is_ok:bool = DMSystem.winuser32.SystemParametersInfoW(SPI_SETFONTSMOOTHING,1,0, SPIF_SENDWININICHANGE)
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
            is_ok = DMSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_LOGOFF)
        elif type_ == 1:
            is_ok = DMSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_POWEROFF)
        elif type == 2:
            is_ok = DMSystem.winuser32.ExitWindowsEx(EWX_FORCE | EWX_REBOOT)
        else:
            raise Exception('Call ExitOs failed')
        if not is_ok:
            raise Exception('Call ExitOs failed')
    @staticmethod
    def GetClipboard() -> str:
        CF_UNICODETEXT = 13
        is_ok:bool = DMSystem.winuser32.OpenClipboard(0)
        if not is_ok:
            raise Exception('Call GetClipboard failed')
        hd=DMSystem.winuser32.GetClipboardData(CF_UNICODETEXT)
        if not hd:
            DMSystem.winuser32.CloseClipboard()
            raise Exception('Call GetClipboard failed:Is not UNICODETEXT')
        ss=ctypes.c_wchar_p(hd) 
        DMSystem.winuser32.CloseClipboard()
        return ss.value
    @staticmethod
    def GetCpuType() -> int:
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
        DMSystem.winKernel32.GetNativeSystemInfo(ctypes.byref(lpSystemInfo))
        if(lpSystemInfo.dwProcessorType in [386,486,586,2200]):
            return 1
        elif lpSystemInfo.dwProcessorType == 8664:
            return 2
        else: return 0
    @staticmethod
    def GetDir(type_) -> str:
        if type_ == 0:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = DMSystem.winKernel32.GetCurrentDirectoryA(1000,pathstr)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 1:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = DMSystem.winKernel32.GetSystemDirectoryA(pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 2:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = DMSystem.winKernel32.GetWindowsDirectoryA(pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 3:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = DMSystem.winKernel32.GetTempPathA(1000,pathstr)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        elif type_ == 4:
            pathstr = ctypes.create_string_buffer(''.encode(), 1000)
            loadlen = DMSystem.winKernel32.GetModuleFileNameA(0,pathstr,1000)
            if loadlen <= 0:
                raise Exception('Call GetDir failed')
            return ctypes.string_at(pathstr).decode('GB2312')
        else:raise Exception('Call GetDir failed')
    @staticmethod
    def GetDiskSerial() -> str:
        '''需安装wmi,且winxp无效'''
        import wmi
        disk = [physical_disk.SerialNumber.strip() for physical_disk in wmi.WMI().Win32_DiskDrive()]
        if len(disk) == 0:
            raise Exception('Call GetDiskSerial failed')
        else:
            return disk[len(disk) - 1]
    @staticmethod
    def GetDPI() -> bool:
        ret:bool = True
        DESKTOPHORZRE = 118
        HORZRES = 8
        DESKTOPVERTRES = 117
        VERTRES = 10
        hdc = DMSystem.winuser32.GetDC(0)
        t = DMSystem.wingdi32.GetDeviceCaps(hdc, DESKTOPHORZRE)
        d = DMSystem.wingdi32.GetDeviceCaps(hdc, HORZRES)
        if t != d:ret = False
        t = DMSystem.wingdi32.GetDeviceCaps(hdc, DESKTOPVERTRES)
        d = DMSystem.wingdi32.GetDeviceCaps(hdc, VERTRES)
        if t != d:ret = False
        DMSystem.winuser32.ReleaseDC(0, hdc)
        return ret
    @staticmethod
    def GetMachineCode() -> str:
        '''需安装wmi,且winxp无效'''
        import wmi
        board = [physical_board for physical_board in wmi.WMI().Win32_BaseBoard()]
        if len(board) == 0:
            raise Exception('Call GetMachineCode failed')
        else:
            return board[len(board) - 1].qualifiers['UUID'][1:-1].strip()
    @staticmethod
    def GetNetTime() -> str:
        resp = urllib.request.urlopen('http://www.baidu.com')
        ts = resp.info()['Date']
        ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        ttime=time.localtime(time.mktime(ltime)+8*60*60)
        rettime = "%u-%02u-%02u %02u:%02u:%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday,ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
        return rettime
    @staticmethod
    def GetNetTimeByIp(ip) -> str:
        resp = urllib.request.urlopen("http://"+ip)
        ts = resp.info()['Date']
        ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        ttime=time.localtime(time.mktime(ltime)+8*60*60)
        rettime = "%u-%02u-%02u %02u:%02u:%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday,ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
        return rettime
    @staticmethod
    def GetNetTimeSafe(ip) -> str:
        return DMSystem.GetNetTimeByIp(ip)
    @staticmethod
    def GetOsBuildNumber() -> int:
        dwBuildNumber = ctypes.wintypes.DWORD()
        DMSystem.winntdll.RtlGetNtVersionNumbers(0,0,ctypes.byref(dwBuildNumber))
        return dwBuildNumber.value & 0xffff
    @staticmethod
    def GetOsType() -> int:
        dwMajorVer = ctypes.wintypes.DWORD()
        dwMinorVer = ctypes.wintypes.DWORD()
        DMSystem.winntdll.RtlGetNtVersionNumbers(ctypes.byref(dwMajorVer),ctypes.byref(dwMinorVer),0)
        dwMajorVer = dwMajorVer.value
        dwMinorVer = dwMinorVer.value
        if dwMajorVer == 4:
            return 0
        elif dwMajorVer == 5:
            if dwMinorVer in [0,1]:
                return 1
            else:
                return 2
        elif dwMajorVer == 6 and dwMinorVer == 1:
            return 3
        elif dwMajorVer == 6 and dwMinorVer == 0:
            return 4
        elif dwMajorVer == 6 and dwMinorVer == 2:
            return 5
        elif dwMajorVer == 6 and dwMinorVer == 3:
            return 6
        elif dwMajorVer == 10:
            return 7
        raise Exception('Call GetOsType failed')
    @staticmethod
    def GetScreenDepth() -> int:
        BITSPIXEL = 12
        hdc = DMSystem.winuser32.GetDC(0)
        dmBitDepth  = DMSystem.wingdi32.GetDeviceCaps(hdc,BITSPIXEL)
        DMSystem.winuser32.ReleaseDC(0, hdc)
        return dmBitDepth
    @staticmethod
    def GetScreenHeight() -> int:
        VERTRES = 10
        hdc = DMSystem.winuser32.GetDC(0)
        height  = DMSystem.wingdi32.GetDeviceCaps(hdc,VERTRES)
        DMSystem.winuser32.ReleaseDC(0, hdc)
        return height
    @staticmethod
    def GetScreenWidth() -> int:
        HORZRES = 8
        hdc = DMSystem.winuser32.GetDC(0)
        weight  = DMSystem.wingdi32.GetDeviceCaps(hdc,HORZRES)
        DMSystem.winuser32.ReleaseDC(0, hdc)
        return weight
    @staticmethod
    def GetTime() -> int:
        return DMSystem.winKernel32.timeGetTime()
    @staticmethod
    def Is64Bit() -> bool:
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
        DMSystem.winKernel32.GetNativeSystemInfo(ctypes.byref(lpSystemInfo))
        PROCESSOR_ARCHITECTURE_IA64 = 6
        PROCESSOR_ARCHITECTURE_AMD64 = 9
        if lpSystemInfo.dwOemId in [PROCESSOR_ARCHITECTURE_IA64,PROCESSOR_ARCHITECTURE_AMD64]:
            return True
        else:
            return False
    @staticmethod
    def Play(media_file)->str:
        mp3id = str(uuid.uuid1())
        cmd = "open \""+ media_file + "\" alias " + mp3id
        status = DMSystem.winwinmm.mciSendStringW(cmd,0,0,0)
        if status != 0:
            raise Exception('Call Play failed')
        status = DMSystem.winwinmm.mciSendStringW("play "+ mp3id,0,0,0)
        if status != 0:
            DMSystem.winwinmm.mciSendStringW("close "+ mp3id,0,0,0)
            raise Exception('Call Play failed')
        return mp3id
    @staticmethod
    def RunApp(app_path,mode)->None:
        subprocess.Popen(app_path,shell=mode)
    @staticmethod
    def SetClipboard(value)->None:
        '''需安装pywin32'''
        import win32clipboard
        import win32con
        win32clipboard.OpenClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, value)
        win32clipboard.CloseClipboard()
    @staticmethod
    def SetScreen(width,height,depth) -> None:
        '''需安装pywin32'''
        import win32api
        dm = win32api.EnumDisplaySettings(None, 0)
        dm.PelsHeight = height
        dm.PelsWidth = width
        dm.BitsPerPel = depth
        dm.DisplayFixedOutput = 0
        win32api.ChangeDisplaySettings(dm, 0)
    @staticmethod
    def SetUAC() -> None:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
        return winreg.SetValueEx(key,'EnableLUA',0,winreg.REG_DWORD,0)
    @staticmethod
    def Stop(id_) -> None:
        status = DMSystem.winwinmm.mciSendStringW("stop "+ id_,0,0,0)
        if status != 0:
            raise Exception('Call Stop failed')
        status = DMSystem.winwinmm.mciSendStringW("close "+ id_,0,0,0)
        if status != 0:
            raise Exception('Call Stop failed')
    @staticmethod
    def ShowTaskBarIcon(hwnd,is_show) -> None:
        is_ok = False
        if is_show == 0:
            is_ok = DMSystem.winuser32.SetWindowLongA(67076,-20,0x80)
        else:
            is_ok = DMSystem.winuser32.SetWindowLongA(67076,-20,0x40000)
        if not is_ok:
            raise Exception('call ShowTaskBarIcon failed')
