# 玄铁多媒体AI软硬件融合平台

## 平台简介

XTAI（XuanTie AI）是基于玄铁处理器与无剑芯片平台面向多媒体AI增强场景的全栈软硬件平台。该平台对RISC-V vector、matrix及异构硬件引擎进行OpenCV、CSI-NN算子库和TMedia接口的融合抽象，深度融合多媒体处理流程，形成面向业务的流水线设计，为用户在流水线不同环节实现AI增强优化。平台内置物体检测、分类、超分、大语言模型等各类应用算法。



## 平台优势

![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4maOgdPd2WPjlWNX/img/c9db2034-5400-40cc-bcb0-b0ce8842f61d.png)



## 平台功能

cxVision视频视觉应用pipeline引擎

*   视频流水线分布式串接
    
*   插件式算法开发，支持脚本描述定义流水线应用
    
*   40+通用插件库，支持采集、编解码、图像处理、AI推理等功能
    
*   支持插件动态加载及热更新
    



TMedia媒体库

*   高性能多媒体组件，支持Camera/AVCodec/VPSS/AIE等功能
    
*   多种流媒体协议，支持Http/RTSP/RTMP等
    
*   系统级视频帧存池管理
    



弹性算力抽象库

*   支持40+常用CV算子加速，兼容OpenCV接口，软硬协同优化
    
*   200+RISCV Vector优化算子，全链路算子覆盖
    
*   CSI-NN芯片对接抽象，方便生态伙伴二次开发
    



HHB AI编译部署工具

*   支持ONNX、Caffe、Pytorch、TensorFlow等主流模型转换
    
*   支持算子融合、算子拆分、常量折叠、量化信息传播、零点合并等计算图优化
    
*   支持多种对称和非对称定点量化，支持通道量化
    
*   支持代码生成、异构执行
    

*   [HBB 产品页](https://xuantie.t-head.cn/soft-tools/tools/4197795688228130816?spm=a2cl5.29101270.0.0.f056tR3JtR3JWW)



功能性能诊断工具

*   针对RISC-V指令特性的自动插桩
    
*   系统性能及视频流水线插件的可视化诊断分析
    
*   模型模拟运行及算力分析统计
    



算法生态

*   AI模型和应用例程一站式体验
    
*   检测、分类、分割、超分、手势等各类视觉AI模型支持
    
*   大模型支持（LLM、多模态等）
    



## 平台框图

![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4maOgdPd2WPjlWNX/img/0fa09641-a6ee-4e4e-93d7-e90c19fa422d.png)



## 资源下载

[SDK及手册](https://www.xrvm.cn/soft-tools/application/mediaAI?spm=a2cl5.14300690.0.0.28b0aUwbaUwbU0)



## 已支持的开发板

[矽速·LicheePi 4A](https://wiki.sipeed.com/licheepi4a)
