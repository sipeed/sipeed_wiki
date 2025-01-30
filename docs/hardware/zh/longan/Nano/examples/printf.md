串口打印
==========

很多时候，串口打印都是一个非常方便的调试手段，通过串口打印的信息，可以方便的定位程序错误位置

本文基于 longan nano 演示如何实现 printf 通过串口打印

本文选择串口0作为串口打印信息的端口，外设使用前，自然需要进行初始化

```c
void init_uart0(void)
{	
	/* enable GPIO clock */
    rcu_periph_clock_enable(RCU_GPIOA);
    /* enable USART clock */
    rcu_periph_clock_enable(RCU_USART0);

    /* connect port to USARTx_Tx */
    gpio_init(GPIOA, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ, GPIO_PIN_9);
    /* connect port to USARTx_Rx */
    gpio_init(GPIOA, GPIO_MODE_IN_FLOATING, GPIO_OSPEED_50MHZ, GPIO_PIN_10);

	/* USART configure */
    usart_deinit(USART0);
    usart_baudrate_set(USART0, 115200U);
    usart_word_length_set(USART0, USART_WL_8BIT);
    usart_stop_bit_set(USART0, USART_STB_1BIT);
    usart_parity_config(USART0, USART_PM_NONE);
    usart_hardware_flow_rts_config(USART0, USART_RTS_DISABLE);
    usart_hardware_flow_cts_config(USART0, USART_CTS_DISABLE);
    usart_receive_config(USART0, USART_RECEIVE_ENABLE);
    usart_transmit_config(USART0, USART_TRANSMIT_ENABLE);
    usart_enable(USART0);

    usart_interrupt_enable(USART0, USART_INT_RBNE);
}
```

这里首先的开启了端口时钟和串口时钟，在初始化完管脚后，就进行了串口的功能配置

我们一般比较关心的就是串口的波特率，这里设置成了 115200

然后我们还需要重新实现 _put_char ，将 printf 重映射

```c
int _put_char(int ch)
{
    usart_data_transmit(USART0, (uint8_t) ch );
    while ( usart_flag_get(USART0, USART_FLAG_TBE)== RESET){
    }

    return ch;
}
```

这样就可以快乐的使用 printf 了
