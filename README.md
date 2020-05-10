# DMProject
用最少的依赖实现python版大漠插件(大漠插件v7.1904帮助文档：https://lanzous.com/icguueh)
* 一切开发旨在学习，请勿用于非法用途
## API实现情况
### 系统
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
* [ ] GetDiskSerial 获取本机的硬盘序列号.支持ide scsi硬盘. 要求调用进程必须有管理员权限. 否则返回空串.
* [ ] GetDisplayInfo 获取本机的显卡信息.
* [ ] GetDPI 判断当前系统的DPI(文字缩放)是不是100%缩放.
* [ ] GetLocale 判断当前系统使用的非UNICODE字符集是否是GB2312(不会实现)
* [ ] GetMachineCode 获取本机的机器码.(带网卡). 此机器码用于插件网站后台.(不会实现)
* [ ] GetMachineCodeNoMac 获取本机的机器码.(不带网卡)(不会实现)
* [ ] GetNetTime 从网络获取当前北京时间.
* [ ] GetNetTimeByIp 根据指定时间服务器IP,从网络获取当前北京时间.
* [ ] GetNetTimeSafe 请使用GetNetTimeByIp代替
* [ ] GetOsBuildNumber 得到操作系统的build版本号.  比如win10 16299,那么返回的就是16299. 其他类似.
* [ ] GetOsType 得到操作系统的类型.
* [ ] GetScreenDepth 获取屏幕的色深.
* [ ] GetScreenHeight 获取屏幕的高度. 
* [ ] GetScreenWidth 获取屏幕的宽度. 
* [ ] GetTime 获取当前系统从开机到现在所经历过的时间，单位是毫秒.
* [ ] Is64Bit 判断当前系统是否是64位操作系统
* [ ] Play 播放指定的MP3或者wav文件.
* [ ] RunApp 运行指定的应用程序.
* [ ] SetClipboard 设置剪贴板的内容
* [ ] SetDisplayAcceler 设置当前系统的硬件加速级别.
* [ ] SetLocale 设置当前系统的非UNICOD字符集.(不会实现)
* [ ] SetScreen 设置系统的分辨率 系统色深 
* [ ] SetUAC 设置当前系统的UAC.
* [ ] ShowTaskBarIcon 显示或者隐藏指定窗口在任务栏的图标.(暂不实现)
* [ ] Stop 停止指定的音乐.
### 文件
### 键鼠
### 窗口
### 内存
### 图色
### (待定)
