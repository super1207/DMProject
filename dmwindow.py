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
@Description: 大漠插件7.1904[窗口]API部分的python实现
@FilePath: dmwindow.py
'''

import ctypes.wintypes
import ctypes

class DMWindow():
    winKernel32 = ctypes.windll.kernel32
    winuser32 = ctypes.windll.LoadLibrary('user32.dll')
    wingdi32 = ctypes.windll.LoadLibrary('gdi32.dll')
    winntdll = ctypes.windll.LoadLibrary('ntdll.dll')
    winwinmm = ctypes.windll.LoadLibrary('winmm.dll')
    # @staticmethod
    # def _GetProcessNameById(process_id):
    #     TH32CS_SNAPPROCESS = 0x00000002
    #     hSnapshot = DMWindow.winKernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,process_id)
    #     if not hSnapshot:
    #         raise Exception("call _GetProcessNameById failed")
    #     class PROCESSENTRY32(ctypes.Structure):
    #         _fields_ = [("dwSize", ctypes.c_ulong),
    #         ("cntUsage", ctypes.c_ulong),
    #         ("th32ProcessID", ctypes.c_ulong),
    #         ("th32DefaultHeapID", ctypes.c_ulong),
    #         ("th32ModuleID", ctypes.c_ulong),
    #         ("cntThreads", ctypes.c_ulong),
    #         ("th32ParentProcessID", ctypes.c_ulong),
    #         ("pcPriClassBase", ctypes.c_ulong),
    #         ("dwFlags", ctypes.c_ulong),
    #         ("szExeFile", ctypes.c_char * 260)]
    #     pe32 = PROCESSENTRY32()
    #     pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)
    #     ret = DMWindow.winKernel32.Process32First(hSnapshot,ctypes.byref(pe32))
    #     while ret:
    #         if process_id == pe32.th32ProcessID:
    #             DMWindow.winKernel32.CloseHandle(hSnapshot)
    #             return pe32.szExeFile
    #         ret = DMWindow.winKernel32.Process32Next(hSnapshot,ctypes.byref(pe32))
    #     DMWindow.winKernel32.CloseHandle(hSnapshot)
    #     raise Exception("call _GetProcessNameById failed")

    @staticmethod
    def FindWindow(class_,title)->int:
        return DMWindow.FindWindowEx(None,class_,title)
    @staticmethod
    def FindWindowEx(parent,class_,title)->int:
        retArr = []
        def mycallback(hwnd,extra) -> bool:
            if not DMWindow.winuser32.IsWindowVisible(hwnd):
                return True
            if class_.upper() not in DMWindow.GetWindowClass(hwnd).upper():
                return True
            if title.upper() not in DMWindow.GetWindowTitle(hwnd).upper():
                return True
            retArr.append(hwnd)
            return False
        CMPFUNC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL,ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
        DMWindow.winuser32.EnumChildWindows(parent,CMPFUNC(mycallback),0)
        if len(retArr) == 0:
            raise Exception('call FindWindow failed:Not Found Window')
        return retArr[0]
    @staticmethod
    def FindWindowByProcessId(process_id,class_,title)->int:
        retArr = []
        def mycallback(hwnd,extra) -> bool:
            if not DMWindow.winuser32.IsWindowVisible(hwnd):
                return True
            lProcessId = ctypes.wintypes.LONG()
            DMWindow.winuser32.GetWindowThreadProcessId(hwnd,ctypes.byref(lProcessId))
            if process_id != lProcessId.value:
                return True
            if class_.upper() not in DMWindow.GetWindowClass(hwnd).upper():
                return True
            if title.upper() not in DMWindow.GetWindowTitle(hwnd).upper():
                return True
            retArr.append(hwnd)
            return False
        CMPFUNC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL,ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
        DMWindow.winuser32.EnumChildWindows(None,CMPFUNC(mycallback),0)
        if len(retArr) == 0:
            raise Exception('call FindWindowByProcessId failed:Not Found Window')
        return retArr[0]
    @staticmethod
    def FindWindowByProcess(process_name,class_,title)->int:
        '''需安装psutil'''
        try:
            import psutil
        except:
            raise Exception("called FindWindowByProcess failed:psutil not install")
        retArr = []
        def mycallback(hwnd,extra) -> bool:
            if not DMWindow.winuser32.IsWindowVisible(hwnd):
                return True
            lProcessId = DMWindow.GetWindowProcessId()
            lProcessName = psutil.Process(lProcessId).name()
            if process_name.upper() not in lProcessName.upper():
                return True
            if class_.upper() not in DMWindow.GetWindowClass(hwnd).upper():
                return True
            if title.upper() not in DMWindow.GetWindowTitle(hwnd).upper():
                return True
            retArr.append(hwnd)
            return False
        CMPFUNC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL,ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
        DMWindow.winuser32.EnumChildWindows(None,CMPFUNC(mycallback),0)
        if len(retArr) == 0:
            raise Exception('call FindWindowByProcessId failed:Not Found Window')
        return retArr[0]
    @staticmethod
    def GetProcessInfo(pid):
        '''需安装psutil'''
        try:
            import psutil
        except:
            raise Exception("called GetProcessInfo failed:psutil not install")
        p = psutil.Process(pid)
        return p.name()+'|'+p.exe()+'|'+str(p.cpu_percent())+'|'+str(p.memory_info().rss)
    @staticmethod
    def GetWindowClass(hwnd) -> str:
        classStr = ctypes.create_string_buffer(''.encode(), 1000)
        is_ok:bool = DMWindow.winuser32.GetClassNameA(hwnd,classStr,1000)
        if (not is_ok) and DMWindow.winKernel32.GetLastError() != 0:
            raise Exception("call GetWindowClass failed")
        return ctypes.string_at(classStr).decode('GB2312')
    @staticmethod
    def GetWindowProcessId(hwnd) -> int:
        lProcessId = ctypes.wintypes.LONG()
        is_ok:bool = DMWindow.winuser32.GetWindowThreadProcessId(hwnd,ctypes.byref(lProcessId))
        if (not is_ok) and DMWindow.winKernel32.GetLastError() != 0:
            raise Exception("call GetWindowProcessId failed")
        return lProcessId.value
    @staticmethod
    def GetWindowTitle(hwnd) -> str:
        
        titleStr = ctypes.create_string_buffer(''.encode(), 1000)
        is_ok:bool = DMWindow.winuser32.GetWindowTextA(hwnd,titleStr,1000)
        #print("++"+ctypes.string_at(titleStr).decode('GB2312')+"++")
        if (not is_ok) and DMWindow.winKernel32.GetLastError() != 0:
            raise Exception("call GetWindowTitle failed")
        return ctypes.string_at(titleStr).decode('GB2312')
    @staticmethod
    def GetWindowProcessPath(hwnd) -> str:
        '''需安装psutil'''
        try:
            import psutil
        except:
            raise Exception("called GetWindowProcessPath failed:psutil not install")
        process_id = DMWindow.GetWindowProcessId(hwnd)
        p = psutil.Process(process_id)
        return p.exe()
    @staticmethod
    def GetSpecialWindow(flag) -> int:
        if flag == 0:
            return DMWindow.winuser32.GetDesktopWindow()
        elif flag == 1:
            return DMWindow.winuser32.FindWindowW("Shell_TrayWnd",0)
        else:
            raise Exception('call GetSpecialWindow Failed')
