---
title: maix_asr (voice recognition module)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: maix_asr (speech recognition module)
---


## class (class)

### maix_asr

The maix_asr construction parameters are as follows:

-[address] Flash address for programming the acoustic model.
-[i2s] Recording device, I2S.DEVICE_0 is used by default.
-[dmac] The DMA channel used for recording. [Channel 3] is used by default.
-[shift] Channel selection. Maix series hardware recording devices usually use mono input. Set 0 as the left channel, so 1 is the right channel.

```python
from speech_recognizer import asr
class maix_asr(asr):
  def config(self, sets):
    pass
t = maix_asr(0x500000, I2S.DEVICE_0, 3, shift=0)
```

The maix_asr module is an extended configuration interface auxiliary class that inherits the internal asr module, and is implemented as follows:

```python

from speech_recognizer import asr

class maix_asr(asr):

  asr_vocab = ["lv", "shi", "yang", "chun", "yan", "jing", "da", "kuai", "wen", "zhang", "de", "di" , "se", "si", "yue", "lin", "luan", "geng", "xian", "huo", "xiu", "mei", "yi", "ang", " ran", "ta", "jin", "ping", "yao", "bu", "li", "liang", "zai", "yong", "dao", "shang", "xia" , "fan", "teng", "dong", "she", "xing", "zhuang", "ru", "hai", "tun", "zhi", "tou", "you", " ling", "pao", "hao", "le", "zha", "zen", "me", "zheng", "cai", "ya", "shu", "tuo", "qu" , "fu", "guang", "bang", "zi", "chong", "shui", "cuan", "ke", "shei", "wan", "hou", "zhao", " jian", "zuo", "cu", "hei", "yu", "ce", "ming", "dui", "cheng", "men", "wo", "bei", "dai" , "zhe", "hu", "jiao", "pang", "ji", "lao", "nong", "kang", "yuan", "chao", "hui", "xiang", " bing", "qi", "chang", "nian", "jia", "tu", "bi", "pin", "xi", "zou", "chu", "cun", "wang" , "na", "ge", "an", "ning", "tian", "xiao", "zhong", "shen", "nan", "er", "ri", "zhu", " xin", "wai", "luo", "gang", "qing", "xun", "te", "cong", "gan", "lai", "he", "dan", "wei" , "die ", "kai", "ci", "gu", "neng", "ba", "bao", "xue", "shuai", "dou", "cao", "mao", "bo", "zhou", "lie", "qie", "ju", "chuan", "guo", "lan", "ni", "tang", "ban", "su", "quan", "huan ", "ying", "a", "min", "meng", "wu", "tai", "hua", "xie", "pai", "huang", "gua", "jiang", "pian", "ma", "jie", "wa", "san", "ka", "zong", "nv", "gao", "ye", "biao", "bie", "zui ", "ren", "jun", "duo", "ze", "tan", "mu", "gui", "qiu", "bai", "sang", "jiu", "yin", "huai", "rang", "zan", "shuo", "sha", "ben", "yun", "la", "cuo", "hang", "ha", "tuan", "gong ", "shan", "ai", "kou", "zhen", "qiong", "ding", "dang", "que", "weng", "qian", "feng", "jue", "zhuan", "ceng", "zu", "bian", "nei", "sheng", "chan", "zao", "fang", "qin", "e", "lian", "fa ", "lu", "sun", "xu", "deng", "guan", "shou", "mo", "zhan", "po", "pi", "gun", "shuang", "qiang", "kao", "hong", "kan", "dian", "kong", "pei", "tong", "ting", "zang", "kuang", "reng", "ti ", "pan", "heng", "chi", "lun", "kun", "han", "lei", "zuan", "man", "sen", "duan", "leng", "su i", "gai", "ga", "fou", "kuo", "ou", "suo", "sou", "nu", "du", "mian", "chou", "hen" , "kua", "shao", "rou", "xuan", "can", "sai", "dun", "niao", "chui", "chen", "hun", "peng", " fen", "cang", "gen", "shua", "chuo", "shun", "cha", "gou", "mai", "liu", "diao", "tao", "niu" , "mi", "chai", "long", "guai", "xiong", "mou", "rong", "ku", "song", "che", "sao", "piao", " pu", "tui", "lang", "chuang", "keng", "liao", "miao", "zhui", "nai", "lou", "bin", "juan", "zhua" , "run", "zeng", "ao", "re", "pa", "qun", "lia", "cou", "tie", "zhai", "kuan", "kui", " cui", "mie", "fei", "tiao", "nuo", "gei", "ca", "zhun", "nie", "mang", "zhuo", "pen", "zun" , "niang", "suan", "nao", "ruan", "qiao", "fo", "rui", "rao", "ruo", "zei", "en", "za", " diu", "nve", "sa", "nin", "shai", "nen", "ken", "chuai", "shuan", "beng", "ne", "lve", "qia" , "jiong", "pie", "seng", "nuan", "nang", "miu", "pou", "cen", "dia", "o", "zhuai", "yo", " dei", "n", "ei", "nou", "bia", "eng", "den", "_"]

  def get_asr_list(string='xiao-ai-fas-tong-xue'):
    return [__class__.asr_vocab.index(t) for t in string.split('-') if t in __class__.asr_vocab]

  def get_asr_string(listobj=[117, 214, 257, 144]):
    return'-'.join([__class__.asr_vocab[t] for t in listobj if t <len(__class__.asr_vocab)])

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

### function

#### config

You can configure the vocabulary list required for speech recognition. The maximum number is no more than 6 notes. If it exceeds, it will be ignored. The parameter is `'xiao-ai-ya': 0.3` corresponding Chinese pinyin string and the lowest probability of matching (threshold) And note that it does not distinguish between tones, so there is no difference between `you-hao-ya` and `ni-hao-ya`, so when designing, pay attention to whether the tone of the vocabulary will form new words.

The use case is as follows:

```python
  t.config({
    'xiao-ai-ya': 0.3,
    'hao-de-ya': 0.2,
    'ni-hao-ya': 0.3,
  })
```

#### recognize

The vocabulary configured in the config function will be recognized.

The use case is as follows:

```python
tmp = t.recognize()
# print(tmp)
if tmp != None:
    print(tmp)
```

Return result:

```python
{
    'xiao-ai-ya': 0.9,
    'xiao-ai': 0.2,
}
```

It is the same as the parameter in config, only given as the return value. You can see that there are two matching results of `小-爱-duck` and `小-爱`.

#### state

It is expected that the asr module can be executed within 100ms, it will return the current module status, and the return result can be ignored. The usage is as follows:
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

It can be seen that on_timer will execute the timer.callback_arg().state() function in a 64 ms cycle, where timer.callback_arg() is an instance of the maix_asr class.

#### run

Control module operation (recording).

#### stop

The control module stops (recording).

#### __del__

Actively call the releaseable module, which can be actively collected by gc.collect().
