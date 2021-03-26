uboot下gpio操作
=============================

.. code-block:: c

    #define endtick(seconds) (get_ticks() + (uint64_t)(seconds) * get_tbclk())

arch/arm/mach-sunxi/cpu_info.c

arch/arm/lib/bootm.c

.. code-block:: c

    #include <asm/arch/cpu.h>
    #include <asm/arch/clock.h>
    #include <cli.h>

    unsigned int * cfg_reg=(unsigned int *)(0x01C20800+1*0x24+0);
    unsigned int * data_reg=(unsigned int *)(0x01C20800+1*0x24+0x10);
    unsigned int tmp,tmp0,tmp1;
    uint64_t t1;
    int i;

    tmp = *cfg_reg;
    tmp &= ~0x0f00;
    tmp |= 0x0100;
    *cfg_reg = tmp;

    tmp=*data_reg;
    tmp0 = tmp&(~0x04);
    tmp1 = tmp|0x04;

    t1=get_ticks()+get_tbclk()/12;
    for(i=0;i<3;i++)
    {
    *data_reg=tmp0;
    puts("beep 0\n");
    while(get_ticks()<t1);
    t1=get_ticks()+get_tbclk()/10;
    *data_reg=tmp1;
    puts("beep 1\n");
    while(get_ticks()<t1);
    t1=get_ticks()+get_tbclk()/10;
    }
    *data_reg=tmp0;
