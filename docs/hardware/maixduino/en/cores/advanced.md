Advanced I/O
======


## tone()

### Description

Generates a square wave of the specified frequency (and 50% duty cycle) on a pin. A duration can be specified, otherwise the wave continues until a call to noTone(). The pin can be connected to a piezo buzzer or other speaker to play tones.

### Syntax
`tone(pin, frequency)`

`tone(pin, frequency, duration)`

### Parameters
`pin`: the pin on which to generate the tone

`frequency`: the frequency of the tone in hertz - `unsigned int`

`duration`: the duration of the tone in milliseconds (optional) - `unsigned long`

### Returns

Nothing

### Notes and Warnings
If you want to play different pitches on multiple pins, you need to call `noTone()` on one pin before calling `tone()` on the next pin.

-----
## noTone()

### Description
Stops the generation of a square wave triggered by `tone()`. Has no effect if no tone is being generated.

### Syntax

`noTone(pin)`

### Parameters

`pin`: the pin on which to stop generating the tone

### Returns

Nothing

### Notes and Warnings

If you want to play different pitches on multiple pins, you need to call `noTone()` on one pin before calling `tone()` on the next pin.
