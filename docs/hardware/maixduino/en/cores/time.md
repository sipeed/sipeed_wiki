Time
=====

## delay()

### Description
Pauses the program for the amount of time (in milliseconds) specified as parameter. (There are 1000 milliseconds in a second.)

### Syntax

`delay(ms)`

### Parameters

`ms`: the number of milliseconds to pause (`unsigned long`)

### Returns

Nothing

-----

## delayMicroseconds()

### Description

Pauses the program for the amount of time (in microseconds) specified as parameter. There are a thousand microseconds in a millisecond, and a million microseconds in a second.

### Syntax

`delayMicroseconds(us)`

### Parameters

`us`: the number of microseconds to pause (`unsigned int`)

### Returns

Nothing

-----

## micros()

### Description

Returns the number of microseconds since the Arduino board began running the current program. 

### Syntax

`time = micros()`

### Parameters

Nothing

### Returns

Returns the number of microseconds since the Maixduino board began running the current program.(`unsigned long`)

-----

## millis()

### Description

Returns the number of milliseconds passed since the Maixduino board began running the current program. This number will overflow (go back to zero), after approximately 50 days.

### Syntax

`time = millis()`

### Parameters

None

### Returns

Number of milliseconds passed since the program started (`unsigned long`)
