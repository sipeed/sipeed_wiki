---
title: maix_asr（语音识别模块）
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: maix_asr（语音识别模块）
---


## class（类）

### maix_asr

maix_asr 构造参数如下：

- `address` 烧写声学模型的 Flash 地址。
- `i2s` 录音设备，默认使用 I2S.DEVICE_0 。
- `dmac` 录音所使用的 DMA 通道，默认使用 `通道 3`。
- `shift` 声道选择，Maix 系列的硬件录音设备通常为单声道输入，设置 0 为左声道，所以 1 为右声道。

```python
from speech_recognizer import asr
class maix_asr(asr):
  def config(self, sets):
    pass
t = maix_asr(0x500000, I2S.DEVICE_0, 3, shift=0)
```

该 maix_asr 模块由继承内部 asr 模块而来的拓展配置接口辅助类，实现如下：

```python

from speech_recognizer import asr

class maix_asr(asr):

  asr_vocab = ["lv", "shi", "yang", "chun", "yan", "jing", "da", "kuai", "wen", "zhang", "de", "di", "se", "si", "yue", "lin", "luan", "geng", "xian", "huo", "xiu", "mei", "yi", "ang", "ran", "ta", "jin", "ping", "yao", "bu", "li", "liang", "zai", "yong", "dao", "shang", "xia", "fan", "teng", "dong", "she", "xing", "zhuang", "ru", "hai", "tun", "zhi", "tou", "you", "ling", "pao", "hao", "le", "zha", "zen", "me", "zheng", "cai", "ya", "shu", "tuo", "qu", "fu", "guang", "bang", "zi", "chong", "shui", "cuan", "ke", "shei", "wan", "hou", "zhao", "jian", "zuo", "cu", "hei", "yu", "ce", "ming", "dui", "cheng", "men", "wo", "bei", "dai", "zhe", "hu", "jiao", "pang", "ji", "lao", "nong", "kang", "yuan", "chao", "hui", "xiang", "bing", "qi", "chang", "nian", "jia", "tu", "bi", "pin", "xi", "zou", "chu", "cun", "wang", "na", "ge", "an", "ning", "tian", "xiao", "zhong", "shen", "nan", "er", "ri", "zhu", "xin", "wai", "luo", "gang", "qing", "xun", "te", "cong", "gan", "lai", "he", "dan", "wei", "die", "kai", "ci", "gu", "neng", "ba", "bao", "xue", "shuai", "dou", "cao", "mao", "bo", "zhou", "lie", "qie", "ju", "chuan", "guo", "lan", "ni", "tang", "ban", "su", "quan", "huan", "ying", "a", "min", "meng", "wu", "tai", "hua", "xie", "pai", "huang", "gua", "jiang", "pian", "ma", "jie", "wa", "san", "ka", "zong", "nv", "gao", "ye", "biao", "bie", "zui", "ren", "jun", "duo", "ze", "tan", "mu", "gui", "qiu", "bai", "sang", "jiu", "yin", "huai", "rang", "zan", "shuo", "sha", "ben", "yun", "la", "cuo", "hang", "ha", "tuan", "gong", "shan", "ai", "kou", "zhen", "qiong", "ding", "dang", "que", "weng", "qian", "feng", "jue", "zhuan", "ceng", "zu", "bian", "nei", "sheng", "chan", "zao", "fang", "qin", "e", "lian", "fa", "lu", "sun", "xu", "deng", "guan", "shou", "mo", "zhan", "po", "pi", "gun", "shuang", "qiang", "kao", "hong", "kan", "dian", "kong", "pei", "tong", "ting", "zang", "kuang", "reng", "ti", "pan", "heng", "chi", "lun", "kun", "han", "lei", "zuan", "man", "sen", "duan", "leng", "sui", "gai", "ga", "fou", "kuo", "ou", "suo", "sou", "nu", "du", "mian", "chou", "hen", "kua", "shao", "rou", "xuan", "can", "sai", "dun", "niao", "chui", "chen", "hun", "peng", "fen", "cang", "gen", "shua", "chuo", "shun", "cha", "gou", "mai", "liu", "diao", "tao", "niu", "mi", "chai", "long", "guai", "xiong", "mou", "rong", "ku", "song", "che", "sao", "piao", "pu", "tui", "lang", "chuang", "keng", "liao", "miao", "zhui", "nai", "lou", "bin", "juan", "zhua", "run", "zeng", "ao", "re", "pa", "qun", "lia", "cou", "tie", "zhai", "kuan", "kui", "cui", "mie", "fei", "tiao", "nuo", "gei", "ca", "zhun", "nie", "mang", "zhuo", "pen", "zun", "niang", "suan", "nao", "ruan", "qiao", "fo", "rui", "rao", "ruo", "zei", "en", "za", "diu", "nve", "sa", "nin", "shai", "nen", "ken", "chuai", "shuan", "beng", "ne", "lve", "qia", "jiong", "pie", "seng", "nuan", "nang", "miu", "pou", "cen", "dia", "o", "zhuai", "yo", "dei", "n", "ei", "nou", "bia", "eng", "den", "_"]

  def get_asr_list(string='xiao-ai-fas-tong-xue'):
    return [__class__.asr_vocab.index(t) for t in string.split('-') if t in __class__.asr_vocab]

  def get_asr_string(listobj=[117, 214, 257, 144]):
    return '-'.join([__class__.asr_vocab[t] for t in listobj if t < len(__class__.asr_vocab)])

  def unit_test():
    print(__class__.get_asr_list('xiao-ai'))
    print(__class__.get_asr_string(__class__.get_asr_list('xiao-ai-fas-tong-xue')))

  def config(self, sets):
    self.set([(sets[key], __class__.get_asr_list(key)) for key in sets])

  def recognize(self):
    res = self.result()
    # print(tmp)
    if res != None:
      sets = {}
      for tmp in res:
        sets[__class__.get_asr_string(tmp[1])] = tmp[0]
        #print(tmp[0], get_asr_string(tmp[1]))
      return sets
    return None

```

### function（方法）

#### config

可以配置语音识别的所需要的词汇列表，最大不超过 6 个音符，超了会忽略，参数为 `'xiao-ai-ya' : 0.3` 对应的 中文拼音字符串 和 匹配的最低概率（门限），且注意它不区分音调，所以 `你-好-鸭` 和 `尼-浩-雅` 没有区别，所以设计的时候要注意词汇的语调是否会形成新词。

用例如下：

```python
  t.config({
    'xiao-ai-ya' : 0.3,
    'hao-de-ya' : 0.2,
    'ni-hao-ya' : 0.3,
  })
```

#### recognize

将会识别 config 函数中所配置的词汇。

用例如下：

```python
tmp = t.recognize()
# print(tmp)
if tmp != None:
    print(tmp)
```

返回结果：

```python
{
    'xiao-ai-ya' : 0.9,
    'xiao-ai' : 0.2,
}
```

跟 config 时的参数一样，只是作为返回值给出，可以见到此处出现 `小-爱-鸭` 和 `小-爱` 两个匹配结果。

#### state

期望保持在 100ms 内能够执行 asr 模块，它会返回当前模块状态，可以忽略返回结果，用法如下：

```python
from machine import Timer

def on_timer(timer):
  #print("time up:",timer)
  #print("param:",timer.callback_arg())
  timer.callback_arg().state()

# default: maix dock / maix duino set shift=0
t = maix_asr(0x500000, I2S.DEVICE_0, 3, shift=0) # maix bit set shift=1
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=64, callback=on_timer, arg=t)
tim.start()
```

可见 on_timer 会在 64 ms 的周期内执行 timer.callback_arg().state() 函数，其中 timer.callback_arg() 为 maix_asr 类的实例。

#### run

控制模块运行（录音）。

#### stop

控制模块停止（录音）。

#### __del__

主动调用可释放模块，可被 gc.collect() 主动回收。
