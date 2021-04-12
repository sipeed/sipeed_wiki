---
title: FPGA点灯
---

源码下载
-----------------

请到github下载，地址为
[\<<https://github.com/Lichee-Pi/Tang_FPGA_Examples/tree/master/0.LED>\>](<https://github.com/Lichee-Pi/Tang_FPGA_Examples/tree/master/0.LED>)

代码简析
========

\> module led
\> (
\>  input wire CLK\_IN, //时钟输入，24MHz
\>  input wire RST\_N, //复位按键输入，低有效
\>  output wire [2:0]RGB\_LED //RGB led输出
\> ); \> \> parameter time1 =
24'd24\_000\_000;//晶振为24Mhz，这里表示计数一秒 \> \> reg [2:0]rledout;
\> reg [23:0] count;
\> reg [1:0]shift\_cnt; \> \> initial
\> begin
\>   count=24'b0;
\>   rledout=3'b1;
\>   shift\_cnt=2'b0;
\> end \> \> always @(posedge CLK\_IN)begin
\>   if(RST\_N==0)begin //复位按键按下就清空计数并清空输出
\>     count \<= 24'b0;
\>     rledout \<= 3'b1;
\>     shift\_cnt \<=2'b0;
\>   end \> \>   if(count == time1) //计数时间到
\>   begin
\>     count\<= 24'd0; //清空计数值 \> \>     if(shift\_cnt==2'b10)begin
//移位3次
\>       rledout \<= 3'b1;
\>       shift\_cnt \<=2'b0;
\>     end
\>     else begin
\>       rledout \<= {rledout[1:0],1'b0}; //led输出移位
\>       shift\_cnt \<= shift\_cnt + 1'b1;
\>     end
\>   end
\>   else
\>     count \<= count + 1'b1; //计数累加
\> end \> \> assign RGB\_LED = rledout;
\> endmodule

将代码综合，下载码流到fpga，可以看到板上的rgb
led会移位闪烁。（emmm，闪烁效果太差，如果你有更好的可以发过来。(╯︵╰)
