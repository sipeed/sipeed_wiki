内核printk等级设置
=================================

1. 查看当前控制台的打印级别

   ``cat /proc/sys/kernel/printk``

   4 4 1 7

   其中第一个“4”表示内核打印函数printk的打印级别，只有级别比他高的信息才能在控制台上打印出来，既 0－3级别的信息

2. 修改打印

   echo "新的打印级别 4 1 7" >/proc/sys/kernel/printk

3. 不够打印级别的信息会被写到日志中可通过dmesg 命令来查看
4.printk的打印级别

    .. code-block:: c

        #define KERN_EMERG           "<0>" /* system is unusable */
        #define KERN_ALERT           "<1>" /* action must be taken immediately */
        #define KERN_CRIT            "<2>" /* critical conditions */
        #define KERN_ERR             "<3>" /* error conditions */
        #define KERN_WARNING         "<4>" /* warning conditions */
        #define KERN_NOTICE          "<5>" /* normal but significant condition */
        #define KERN_INFO            "<6>" /* informational */
        #define KERN_DEBUG           "<7>" /* debug-level messages */

5. printk函数的使用

   printk(打印级别 “要打印的信息”)

   打印级别 既上面定义的几个宏
