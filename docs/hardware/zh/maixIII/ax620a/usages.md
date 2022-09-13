---
title: 基础使用  

---

基于上文的烧录系统后，

## 准备工作

1. 操作前，先把 网线 路由器 准备好，插入 SD 卡上电测试。
2. 开机时按住 USR 键后上电，系统在 20 秒左右将屏幕会亮起，此时屏幕会显示摄像头画面，测试屏幕与摄像头，用人眼确认是否通过。
3. 这时灯光会开始闪烁，等待 WIFI 和 以太网的连接，如果两个都获得 IP 则灯光会灭。
4. 松开按键灯光会全亮，并播放一段测试音频，此时进入录音回放模式，用纸巾刮蹭测试左右声道有效（要调低音量防止过大噪声），此时再按一下按键摄像头画面会停止，灯光会全灭。

## CPU RAM 压测

 `sudo apt-get install stress` 安装 stress 软件，现已预置。
 `sudo stress -c 2 -t 10000` 执行 CPU 压力测试。2代表核数 10000代表时间
查看系统信息使用 `htop` 即可
 `sudo apt install memtester DDR RAM` 测试需要安装一下。
格式: `memtester 内存数量 次数` 比如测试 512M 使用 `memtester 512M &` 挂后台循环测试。

```bash
juwan@juwan-n85-dls:~$ memtester 8M
memtester version 4.3.0 (64-bit)
Copyright (C) 2001-2012 Charles Cazabon.
Licensed under the GNU General Public License version 2 (only).

pagesize is 4096
pagesizemask is 0xfffffffffffff000
want 8MB (8388608 bytes)
got  8MB (8388608 bytes), trying mlock ...locked.
Loop 1:
  Stuck Address       : ok         
  Random Value        : ok
  Compare XOR         : ok
  Compare SUB         : ok
  Compare MUL         : ok
  Compare DIV         : ok
  Compare OR          : ok
  Compare AND         : ok
  Sequential Increment: ok
  Solid Bits          : ok         
  Block Sequential    : ok         
  Checkerboard        : ok         
  Bit Spread          : ok         
  Bit Flip            : ok         
  Walking Ones        : ok         
  Walking Zeroes      : ok         
  8-bit Writes        : ok
  16-bit Writes       : ok

Loop 2:
  Stuck Address       : ok         
  Random Value        : ok
  Compare XOR         : ok
  Compare SUB         : ok
  Compare MUL         : ok
  Compare DIV         : ok
  Compare OR          : ok
  Compare AND         : ok
  Sequential Increment: ok
  Solid Bits          : ok         
  Block Sequential    : ok         
  Checkerboard        : ok         
  Bit Spread          : ok         
  Bit Flip            : ok         
  Walking Ones        : ok         
  Walking Zeroes      : ok         
  8-bit Writes        : ok
  16-bit Writes       : ok
```
