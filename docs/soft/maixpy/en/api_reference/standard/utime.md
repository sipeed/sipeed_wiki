---
title: utime-time related functions
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: utime-time related functions
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [time](https://docs.python.org/3.5/library/time.html#module-time).

The `utime` module provides functions for obtaining the current time and date, measuring time intervals and delays.

**Time Epoch**: The Unix ported version uses the POSIX system era of 1970-01-01 00:00:00 UTC. However, the embedded port version uses the epoch of 2000-01-01 00:00:00 UTC.

**Maintain actual calendar date/time**: This requires a real-time clock (RTC). On systems with underlying OS (including some RTOS), RTC may be implicit. Setting and maintaining the actual calendar time is the responsibility of the OS/RTOS and is done outside of MicroPython, it only uses the OS API to query the date/time. On bare metal porting, the system time depends on the `machine.RTC()` object. You can use `machine.RTC(). The datetime (tuple)` function sets the current calendar time and maintains it in the following ways:

* Through a backup battery (may be an additional optional component on a specific circuit board).
* Use network time protocol (need to be set by transplantation/user).
* It is manually set by the user each time it is powered on (many boards maintain the RTC time during hard reset, but some may need to be set again in this case).
If the system/MicroPython RTC is not used to maintain the actual calendar time, the functions that refer to the current absolute time below this requirement may not match expectations.

## Function

### utime.localtime([secs])

Convert the time in seconds since the epoch (see above) into an 8-tuple containing: (year, month, day, hour, minute, second, weekday, late) If seconds are not provided or none, then Used for the current time from RTC.

* The year includes the century (for example, 2014).
* Month is 1-12
* mday is 1-31
* Hours are 0-23
* Minutes are 0-59
* The second is 0-59
Working days from Monday to Sunday are 0-6
* yearday is 1-366


### utime.mktime()

This is the inverse function of local time. Its parameter is a complete 8-tuple, representing the time expressed in local time. It returns an integer, which is the number of seconds since January 1, 2000.

### utime.sleep(seconds)

Sleep for the given number of seconds. Some circuit boards may accept seconds as floating point numbers to sleep for a few seconds. Please note that other boards may not accept floating-point parameters because of their compatibility using `sleep_ms()` and `sleep_us()` functions.

### utime.sleep_ms(ms)

The delay for a given number of milliseconds should be positive or 0.

### utime.sleep_us(us)

The delay for a given number of microseconds should be positive or zero.

### utime.ticks_ms()

Returns an incremental millisecond counter with an arbitrary reference point, which wraps around after a certain value.

The wraparound value is not explicitly disclosed, but we will call it TICKS_MAX to simplify the discussion. The period of the value is TICKS_PERIOD = TICKS_MAX + 1. TICKS_PERIOD is guaranteed to be a power of 2, but it may be different between different hardware migrations. The same period value is used for all `ticks_ms()`, `ticks_us()`, `ticks_cpu()` functions (for simplicity). Therefore, these functions will return values ​​in the range [0 .. TICKS_MAX], including the total TICKS_PERIOD value. Note that only non-negative values ​​are used. In most cases, you should treat the values ​​returned by these functions as opaque. The only operations available are the `ticks_diff()` and `ticks_add()` functions, as described below.

> Note: Performing standard mathematical operations (+,-) or relational operators (<, <=, >,> =) directly on these values ​​will result in invalid results. Performing mathematical operations and then passing the result as a parameter to ticks_diff() or ticks_add() will also cause invalid results of the latter function.

### utime.ticks_us()

Just like'ticks_ms()` above, but within a few microseconds.

### utime.ticks_cpu()

Similar to `ticks_ms()` and `ticks_us()`, but with the highest resolution in the system. This is usually the CPU clock, which is why the function is named this way. But it does not have to be the CPU clock, but can use some other timing sources available in the system (for example, high-resolution timers). The exact time unit (resolution) of this function is not specified at the'utime' module level, but the documentation for specific hardware may provide more specific information. This function is used for very detailed benchmarks or very tight real-time loops. Avoid using it in portable code.


### utime.ticks_add(ticks, delta)

The offset value is calculated according to the given number, which can be positive or negative. Given a ticks value, this function allows the ticks value delta ticks to be calculated after or after the module arithmetic definition of the tick value (see `ticks_ms()` above). The ticks parameter must be the direct result of calling the `ticks_ms()`, `ticks_us()` or `ticks_cpu()` function (or calling `ticks_add()` from before). However, delta can be any integer or numeric expression. ticks_add() is very useful for calculating the deadline of events/tasks. (Note: You must use the `ticks_diff()` function to handle the deadline.)

example:

```python
# Find out what ticks value there was 100ms ago
print(ticks_add(time.ticks_ms(), -100))

# Calculate deadline for operation and test for it
deadline = ticks_add(time.ticks_ms(), 200)
while ticks_diff(deadline, time.ticks_ms())> 0:
    do_a_little_of_something()

# Find out TICKS_MAX used by this port
print(ticks_add(0, -1))
```

### utime.ticks_diff(ticks1, ticks2)


Measure the difference between the values ​​returned from the `ticks_ms()`, `ticks_us()`, or `ticks_cpu()` functions as a signed value that can be wrapped.

The order of the parameters is the same as the subtraction operator. `ticks_diff(ticks1, ticks2)` has the same meaning as `ticks1-ticks2`. However, the value returned by functions such as `ticks_ms()` may wrap around, so using subtraction directly will produce incorrect results. This is why `ticks_diff()` is needed, which implements modular (or more specifically, ring) arithmetic and produces correct results even for surrounding values ​​(as long as they are not too far apart, see below). This function returns a **signed** value in the range [-TICKS_PERIOD / 2 .. TICKS_PERIOD / 2-1] (this is the typical range definition for twos complement signed binary integers). If the result is negative, it means that ticks1 is earlier than ticks2 in time. Otherwise, it means ticks1 occurs after ticks2. If ticks1 and ticks2 are separated from each other by no more than TICKS_PERIOD / 2-1 ticks, only ** is retained. If it is not true, an incorrect result will be returned. Specifically, if two scale values ​​are separated by TICKS_PERIOD / 2-1 scale, the value will be returned by this function. However, if the real-time ticking TICKS_PERIOD/2 has been passed between them, the function will return -TICKS_PERIOD/2, that is, the result value will wrap around to the negative range of possible values.

Unofficial reason for the above restriction: Suppose you are locked in a room and cannot monitor the passage of time except for the standard 12-speed clock. Then, if you look at the watch face now and no longer look at it for 13 hours (for example, if you sleep for a long time), then once you read it again, you may feel that only 1 hour has passed. To avoid this error, please check the clock regularly. Your application should do the same. The metaphor of "sleeping too long" also directly maps to application behavior: don't let your application run any single task for too long. Run the task step by step and time between the two.

`ticks_diff()` is designed to adapt to various usage patterns, including:

* Timeout polling. In this case, the sequence of events is known, and you will only deal with the positive results of `ticks_diff()`:

```python
# Wait for GPIO pin to be asserted, but at most 500us
start = time.ticks_us()
while pin.value() == 0:
    if time.ticks_diff(time.ticks_us(), start)> 500:
        raise TimeoutError
```

* Scheduling events. In this case, if the event expires, the ticks_diff() result may be negative:

```python
# This code snippet is not optimized
now = time.ticks_ms()
scheduled_time = task.scheduled_time()
if ticks_diff(scheduled_time, now)> 0:
    print("Too early, let's nap")
    sleep_ms(ticks_diff(scheduled_time, now))
    task.run()
elif ticks_diff(scheduled_time, now) == 0:
    print("Right at time!")
    task.run()
elif ticks_diff(scheduled_time, now) <0:
    print("Oops, running late, tell task to run faster!")
    task.run(run_faster=true)
```
> Note: Do not pass `time()` values ​​to `ticks_diff()`, you should use regular mathematical operations on them. But please note that `time()` may (also) overflow. This is called https://en.wikipedia.org/wiki/Year_2038_problem.

### utime.time()

Returns the integer number of seconds since the epoch, assuming the basic RTC is set and maintained as described above. If RTC is not set, this function returns the number of seconds since the specific hardware migration reference time point (for embedded circuit boards without battery-powered RTC, usually since power-on or reset). If you want to develop portable MicroPython applications, you should not rely on this function to provide a higher precision than the second. If you need higher precision, use the `ticks_ms()` and `ticks_us()` functions. If you need calendar time, `localtime()` without parameters is a better choice.

#### Difference with CPython

In CPython, this function returns the number of seconds since the Unix epoch (1970-01-01 00:00 UTC), as a floating point number, usually with microsecond precision. With MicroPython, only the Unix port uses the same epoch, and if floating-point precision allows, it returns sub-second precision. Embedded hardware usually does not have floating-point precision to represent long time ranges and sub-second precision, so they use integer values ​​with second precision. Some embedded hardware also lacks a battery-powered RTC, so it returns the number of seconds since the last power-on or other relative hardware specific point (such as reset).


### time.ticks()

Equivalent to `time.ticks_ms`


### time.clock()

Get the `clock` object

#### return value

`clock` object

## clock object

Returned by `time.clock()`
### clock.tick()

Recording start time (ms), used with `clock.fps()` to calculate `fps`

#### return value

None

### clock.fps()

Calculate the frame rate (`fps`) based on the time from the previous call to `clock.tick()`

such as:

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

Reset all flags

### clock.avg()

Calculate the time consumed per frame based on the time from the previous call to `clock.tick()`
