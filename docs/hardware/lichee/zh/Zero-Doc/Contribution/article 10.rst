lichee 编译踩坑记录(ilichee ZERO)
================================================

.. contents:: 本文目录

1. 编译环境
------------------------------------------------

编译的时候原来是正常编译过linux内核的，不过buildroot和里面带的程序还需要其他的一些软件包

需要安装的包
    ``bison flex texinfo zlib1g-dev gawk``

填坑方案
    ``sudo apt-get install [包名称]``

2. buildroot源码
------------------------------------------------

由于各种各样的原因buildroot里到处是坑- -有的源码可能对新编译器不适应，需要修改

修改时有两个位置，如果还没有进行编译可以在 ``/buildroot/pakage/[包名称]/`` 里找到对应文件/文件夹

编译时使用的是将上面的源码复制到 ``/out/linux/common/buildroot/build/[包名称]`` 或 ``/out/linux/common/buildroot/build/host-[包名称]`` 下，
所以如果编译的过程中出错除了改buildroot里的源码也需要改后面那两个(如果有)文件夹下的源码

1) host-m4-1.4.15
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

buildroot过程中

.. code-block:: console

   ./stdio.h:456:1:error: 'gets' undeclared here (not in a function)
   _GL_WARN_ON_USE(gets, "gets is a security hole - use fgets instead");

填坑方法：参考链接：http://www.civilnet.cn/talk/browse.php?topicno=78555

找到： ``host-m4-1.4.15/lib/stdio.h`` ，然后对stdio.h文件做出如下改动，必要时连同 ``stdio.in.h`` 一起修改：

.. code-block:: console

   === modified file 'host-m4-1.4.15/lib/stdio.h' 
   @@ -140,8 +140,10 @@ 
   +#if defined gets 
   #undef gets 
   _GL_WARN_ON_USE (gets, "gets is a security hole - use fgets instead"); 
   +#endif

修改后测试通过

2) host-autoconf-2.65
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

buildroot过程中

   ``conftest.c:14625:must be after @defmac' to use@defmacx'``

填坑方法：参考链接：http://gnu-autoconf.7623.n7.nabble.com/compile-error-conftest-c-14625-must-be-after-defmac-to-use-defmacx-td18843.html

找到 ``autoconf-2.65/doc/autoconf.texi`` ,进行修改

.. code-block:: console

   @@ -15,7 +15,7 @@ 
   @c The ARG is an optional argument.  To be used for macro arguments in 
   @c their documentation (@defmac). 
   @macro ovar{varname} 
   -@r{[}@var{\varname}@r{]}@c 
   +@r{[}@var{\varname}@r{]} 
   @end macro 
   @c @dvar(ARG, DEFAULT) 
   @@ -23,7 +23,7 @@ 
   @c The ARG is an optional argument, defaulting to DEFAULT.  To be used 
   @c for macro arguments in their documentation (@defmac). 
   @macro dvar{varname, default} 
   -@r{[}@var{\varname} = @samp{\default}@r{]}@c 
   +@r{[}@var{\varname} = @samp{\default}@r{]} 
   @end macro 
   @c Handling the indexes with Texinfo yields several different problems.

修改后测试通过

3) host-makedevs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

buildroot过程中

.. code-block:: console

   /lichee/out/linux/common/buildroot/build/host-makedevs/makedevs.c:374:6: error: variable ‘ret’ set but not used [-Werror=unused-but-set-variable]
   int ret = EXIT_SUCCESS;
   ^
   cc1: all warnings being treated as errors

找到 ``/makedevs/makedevs.c`` 或 ``/host-makedevs/makedevs.c`` 进行修改

最后一行， ``return 0``; 修改为： ``return ret``;

这也算(╯‵□′)╯︵┻━┻)

3. lichee缺rootfs.cpio.gz
------------------------------------------------

buildroot后

无法定位 **"rootfs.cpio.gz"**

泽畔大大说可以自己包一个 我从H3的SDK里扒了一个出来 目前为止没有出错 放到linux内核目录下

4. awk: line 2: function strtonum never defined
------------------------------------------------

awk版本问题，需要安装gawk

   ``sudo apt-get install gawk``

5. pack finish但无镜像输出
------------------------------------------------

出现 ``Dragon execute image.cfg failed``

lichee默认的对象是编译到nor flash上，但是没找到nor flash的配置文件o(╯□╰)o

修改**/lichee/tools/pack/pack**

.. code-block:: console

    354： -update_mbr	sys_partition_nor.bin 1 > /dev/null
    355： -dragon image.cfg	sys_partition_nor.fex
    354： +update_mbr	sys_partition.bin 1 > /dev/null
    355： +dragon image.cfg	sys_partition.fex

用默认的配置文件 似乎是针对nand的

.. code-block:: bash
   
   sudo ./build.sh
   sudo ./build.sh pack

终于成功〒▽〒
