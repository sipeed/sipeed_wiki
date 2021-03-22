---
title: utime – 时间相关的功能
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: utime – 时间相关的功能
---



该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档： [time](https://docs.python.org/3.5/library/time.html#module-time).

`utime`模块提供获取当前时间和日期，测量时间间隔和延迟的功能。

**时间纪元**: Unix移植版本使用标准为1970-01-01 00:00:00 UTC的POSIX系统时代。但是，嵌入式移植版本使用的是2000-01-01 00:00:00 UTC的纪元。

**维护实际日历日期/时间**: 这需要实时时钟（RTC）。在具有底层OS（包括一些RTOS）的系统上，RTC可能是隐含的。设置和维护实际日历时间是OS / RTOS的责任，并且在MicroPython之外完成，它只使用OS API来查询日期/时间。在裸机移植上，系统时间依赖于`machine.RTC（）`对象。可以使用`machine.RTC（）。datetime（tuple）`函数设置当前日历时间，并通过以下方式维护：

* 通过备用电池（可能是特定电路板的附加可选组件）。
* 使用联网时间协议（需要由移植/用户设置）。
* 每次上电时由用户手动设置（许多电路板在硬复位时保持RTC时间，但有些可能需要在这种情况下再次设置）。
如果未使用系统/ MicroPython RTC维护实际日历时间，则低于此要求参考当前绝对时间的函数可能与预期不符。

## 函数

### utime.localtime([secs])

将自纪元（见上文）以秒为单位的时间转换为8元组，其中包含:(年，月，日，小时，分钟，秒，工作日，晚期）如果未提供秒数或无，则为当前时间来自RTC使用。

* 年份包括世纪（例如2014年）。
* 月是1-12
*  mday是1-31
* 小时是0-23
* 分钟是0-59
* 秒是0-59
周一至周日的工作日为0-6
* yearday是1-366


### utime.mktime()

这是本地时间的反函数。它的参数是一个完整的8元组，表示按当地时间表示的时间。它返回一个整数，它是自2000年1月1日以来的秒数。

### utime.sleep(seconds)

睡眠给定的秒数。有些电路板可能会接受秒作为浮点数来休眠几秒钟。请注意，其他板可能不接受浮点参数，因为与它们的兼容性使用 `sleep_ms()` 和 `sleep_us()` 函数。

### utime.sleep_ms(ms)

给定毫秒数的延迟应为正或0。

### utime.sleep_us(us)

给定微秒数的延迟应为正或0。

### utime.ticks_ms()

返回一个带有任意参考点的递增毫秒计数器，它在某个值之后回绕。

环绕值未明确公开，但我们将其称为TICKS_MAX以简化讨论。值的周期为TICKS_PERIOD = TICKS_MAX + 1. TICKS_PERIOD保证为2的幂，但在不同硬件的移植之间可能不同。相同的句点值用于所有`ticks_ms（）`，`ticks_us（）`，`ticks_cpu（）`函数（为简单起见）。因此，这些函数将返回范围[0 .. TICKS_MAX]中的值，包括总TICKS_PERIOD值。请注意，仅使用非负值。在大多数情况下，您应该将这些函数返回的值视为不透明。可用的唯一操作是`ticks_diff（）`和`ticks_add（）`函数，如下所述。

> 注意：直接对这些值执行标准数学运算（+， - ）或关系运算符（<，<=，>，> =）将导致无效结果。执行数学运算然后将其结果作为参数传递给ticks_diff（）或ticks_add（）也将导致后者函数的无效结果。

### utime.ticks_us()

就像上面的'ticks_ms（）`一样，但是在几微秒内。

### utime.ticks_cpu()

类似于`ticks_ms（）`和`ticks_us（）`，但系统中的分辨率最高。这通常是CPU时钟，这就是函数以这种方式命名的原因。但它不必是CPU时钟，而是可以使用系统中可用的一些其他定时源（例如，高分辨率定时器）。在'utime`模块级别没有指定此函数的确切时间单位（分辨率），但特定硬件的文档可能提供更具体的信息。此功能用于非常精细的基准测试或非常紧凑的实时循环。避免在便携式代码中使用它。


### utime.ticks_add(ticks, delta)

偏移值按给定数字计算，可以是正数也可以是负数。给定一个ticks值，该函数允许在tick值的模块算术定义之后或之后计算ticks值delta ticks（参见上面的`ticks_ms（）`）。 ticks参数必须是调用`ticks_ms（）`，`ticks_us（）`或`ticks_cpu（）`函数（或从之前调用`ticks_add（）`）的直接结果。但是，delta可以是任意整数或数字表达式。 ticks_add（）对于计算事件/任务的截止日期非常有用。 （注意：你必须使用`ticks_diff（）`函数来处理截止日期。）

例子:

```python
# Find out what ticks value there was 100ms ago
print(ticks_add(time.ticks_ms(), -100))

# Calculate deadline for operation and test for it
deadline = ticks_add(time.ticks_ms(), 200)
while ticks_diff(deadline, time.ticks_ms()) > 0:
    do_a_little_of_something()

# Find out TICKS_MAX used by this port
print(ticks_add(0, -1))
```

### utime.ticks_diff(ticks1, ticks2)


测量从`ticks_ms（）`，`ticks_us（）`或`ticks_cpu（）`函数返回的值之间的差异，作为可以回绕的有符号值。

参数顺序与减法运算符相同，`ticks_diff（ticks1，ticks2）`与`ticks1  -  ticks2`具有相同的含义。但是，`ticks_ms（）`等函数返回的值可能会回绕，因此直接使用减法会产生不正确的结果。这就是为什么需要`ticks_diff（）`，它实现模块化（或更具体地说，环）算术，即使对于环绕值也能产生正确的结果（只要它们之间不太远，见下文）。该函数返回范围为[-TICKS_PERIOD / 2 .. TICKS_PERIOD / 2-1]的**有符号**值（这是二进制补码有符号二进制整数的典型范围定义）。如果结果是否定的，则意味着ticks1在时间上早于ticks2。否则，这意味着ticks1发生在ticks2之后。如果ticks1和ticks2彼此分开不超过TICKS_PERIOD / 2-1滴答，则仅保留**。如果不成立，将返回不正确的结果。具体来说，如果两个刻度值相隔TICKS_PERIOD / 2-1刻度，则该值将由该函数返回。但是，如果实时滴答的TICKS_PERIOD / 2已在它们之间传递，则该函数将返回-TICKS_PERIOD / 2，即结果值将回绕到可能值的负范围。

上述限制的非正式理由：假设您被锁在一个房间内，除了标准的12档时钟外无法监控时间的流逝。然后，如果你现在看表盘，不再看13个小时（例如，如果你长时间睡觉），那么一旦你再看一遍，你可能觉得只有1个小时过去了。为了避免这个错误，请定期查看时钟。您的应用程序也应该这样做。 “太长时间睡眠”这个比喻也直接映射到应用程序行为：不要让你的应用程序运行任何单个任务太长时间。分步运行任务，并在两者之间进行计时。

`ticks_diff()` 旨在适应各种使用模式，其中包括：

* 超时轮询。在这种情况下，事件的顺序是已知的，你只会处理`ticks_diff（）`的正面结果：

```python
# Wait for GPIO pin to be asserted, but at most 500us
start = time.ticks_us()
while pin.value() == 0:
    if time.ticks_diff(time.ticks_us(), start) > 500:
        raise TimeoutError
```

* 调度事件。 在这种情况下，如果事件过期，则ticks_diff（）结果可能为负：

```python
# This code snippet is not optimized
now = time.ticks_ms()
scheduled_time = task.scheduled_time()
if ticks_diff(scheduled_time, now) > 0:
    print("Too early, let's nap")
    sleep_ms(ticks_diff(scheduled_time, now))
    task.run()
elif ticks_diff(scheduled_time, now) == 0:
    print("Right at time!")
    task.run()
elif ticks_diff(scheduled_time, now) < 0:
    print("Oops, running late, tell task to run faster!")
    task.run(run_faster=true)
```
> 注意：不要将`time（）`值传递给`ticks_diff（）`，你应该对它们使用常规的数学运算。但请注意，`time（）`可能（也会）溢出。这被称为https://en.wikipedia.org/wiki/Year_2038_problem .

### utime.time()

返回自纪元以来的整数秒数，假设如上所述设置和维护基础RTC。如果未设置 RTC，则此函数返回自特定硬件移植参考时间点以来的秒数（对于没有电池供电的 RTC 的嵌入式电路板，通常自上电或复位后）。如果要开发便携式 MicroPython 应用程序，则不应依赖此函数来提供高于第二的精度。如果你需要更高的精度，使用`ticks_ms（）`和`ticks_us（）`函数，如果你需要日历时间，`localtime（）`没有参数是一个更好的选择。

#### 与CPython的区别

在 CPython 中，此函数返回自 Unix 纪元（1970-01-01 00:00 UTC）以来的秒数，作为浮点数，通常具有微秒精度。 使用 MicroPython，只有 Unix 移植版本使用相同的纪元，如果浮点精度允许，则返回亚秒精度。 嵌入式硬件通常没有浮点精度来表示长时间范围和亚秒精度，因此它们使用具有第二精度的整数值。 某些嵌入式硬件也缺少电池供电的 RTC，因此返回自上次上电或其他相对硬件特定点（例如复位）以来的秒数。


### time.ticks()

等同于 `time.ticks_ms` 


### time.clock()

获取 `clock` 对象

#### 返回值

`clock` 对象

## clock 对象

由 `time.clock()` 返回

### clock.tick()

记录开始时间（ms）， 与`clock.fps()`搭配使用可以计算`fps`

#### 返回值

None

### clock.fps()

根据上一个调用`clock.tick()`到现在的时间计算出帧率（`fps`）

比如：

```python
import sensor
import time
clock = time.clock()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
while True:
	clock.tick()
	sensor.snapshot()
	print("fps = ",clock.fps())
```



### clock.reset()

重置所有标记

### clock.avg()

根据上一个调用`clock.tick()`到现在的时间计算出每帧消耗的时间



