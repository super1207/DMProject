# DMProject
用最少的依赖实现python版大漠插件(大漠插件v7.1904帮助文档：https://lanzous.com/icguueh)
* 一切开发旨在学习，请勿用于非法用途
## API实现情况
### 系统(dmsystem.py)
* [x] Beep 蜂鸣器
* [x] CheckFontSmooth 检测当前系统是否有开启屏幕字体平滑.  
* [x] CheckUAC 检测当前系统是否有开启UAC.
* [x] Delay 延时指定的毫秒,过程中不阻塞UI操作. 一般高级语言使用.按键用不到.(实现不完整)
* [x] Delays 延时指定范围内随机毫秒,过程中不阻塞UI操作. 一般高级语言使用.按键用不到.(实现不完整)
* [x] DisableCloseDisplayAndSleep 设置当前的电源设置，禁止关闭显示器，禁止关闭硬盘，禁止睡眠，禁止待机. 不支持XP.
* [x] DisableFontSmooth 关闭当前系统屏幕字体平滑.同时关闭系统的ClearType功能.
* [x] DisablePowerSave 关闭电源管理，不会进入睡眠.
* [x] DisableScreenSave 关闭屏幕保护.
* [x] EnableFontSmooth 开启当前系统屏幕字体平滑.同时开启系统的ClearType功能.
* [x] ExitOs 注销、重启、关机 
* [x] GetClipboard 获取剪贴板的内容
* [x] GetCpuType 获取当前CPU类型,intel或者amd.
* [x] GetDir 得到系统的路径
* [x] GetDiskSerial 获取本机的硬盘序列号.支持ide scsi硬盘. 要求调用进程必须有管理员权限. 否则返回空串.
* [ ] GetDisplayInfo 获取本机的显卡信息.(暂不实现)
* [x] GetDPI 判断当前系统的DPI(文字缩放)是不是100%缩放.
* [ ] GetLocale 判断当前系统使用的非UNICODE字符集是否是GB2312(暂不实现)
* [ ] GetMachineCode 获取本机的机器码.(带网卡). 此机器码用于插件网站后台. (暂不实现)
* [x] GetMachineCodeNoMac 获取本机的机器码.(不带网卡)(实现不完整)
* [x] GetNetTime 从网络获取当前北京时间.
* [x] GetNetTimeByIp 根据指定时间服务器IP,从网络获取当前北京时间.
* [x] GetNetTimeSafe 请使用GetNetTimeByIp代替
* [x] GetOsBuildNumber 得到操作系统的build版本号.  比如win10 16299,那么返回的就是16299. 其他类似.
* [x] GetOsType 得到操作系统的类型.
* [x] GetScreenDepth 获取屏幕的色深.
* [x] GetScreenHeight 获取屏幕的高度. 
* [x] GetScreenWidth 获取屏幕的宽度. 
* [x] GetTime 获取当前系统从开机到现在所经历过的时间，单位是毫秒.
* [x] Is64Bit 判断当前系统是否是64位操作系统
* [x] Play 播放指定的MP3或者wav文件.
* [x] RunApp 运行指定的应用程序.(实现不完整)
* [x] SetClipboard 设置剪贴板的内容
* [ ] SetDisplayAcceler 设置当前系统的硬件加速级别.(暂不实现)
* [ ] SetLocale 设置当前系统的非UNICOD字符集.(暂不实现)
* [x] SetScreen 设置系统的分辨率 系统色深 
* [x] SetUAC 设置当前系统的UAC,重启生效.
* [ ] ShowTaskBarIcon 显示或者隐藏指定窗口在任务栏的图标.(暂不实现)
* [x] Stop 停止指定的音乐.
### 文件(dmfile.py)
* [ ] CopyFile 拷贝文件.
* [ ] CreateFolder 创建指定目录.
* [ ] DecodeFile 解密指定的文件.
* [ ] DeleteFile 删除文件.
* [ ] DeleteFolder 删除指定目录. 
* [ ] DeleteIni 删除指定的ini小节.
* [ ] DeleteIniPwd 删除指定的ini小节.支持加密文件
* [ ] DownloadFile 从internet上下载一个文件.
* [ ] EncodeFile 加密指定的文件. 
* [ ] EnumIniKey 根据指定的ini文件以及section,枚举此section中所有的key名
* [ ] EnumIniKeyPwd 根据指定的ini文件以及section,枚举此section中所有的key名.可支持加密文件
* [ ] EnumIniSection 根据指定的ini文件,枚举此ini中所有的Section(小节名)
* [ ] EnumIniSectionPwd 根据指定的ini文件,枚举此ini中所有的Section(小节名) 可支持加密文件
* [ ] GetFileLength 获取指定的文件长度.
* [ ] GetRealPath 获取指定文件或目录的真实路径
* [ ] IsFileExist 判断指定文件是否存在.
* [ ] IsFolderExist 判断指定目录是否存在. 
* [ ] MoveFile 移动文件. 
* [ ] ReadFile 从指定的文件读取内容. 
* [ ] ReadIni 从Ini中读取指定信息.
* [ ] ReadIniPwd 从Ini中读取指定信息.可支持加密文件 
* [ ] SelectDirectory 弹出选择文件夹对话框，并返回选择的文件夹.
* [ ] SelectFile 弹出选择文件对话框，并返回选择的文件.
* [ ] WriteFile 向指定文件追加字符串. 
* [ ] WriteIni 向指定的Ini写入信息.  
* [ ] WriteIniPwd 向指定的Ini写入信息.支持加密文件 
### 键鼠
### 窗口
### 内存
### 图色
### (待定)

