Digital I/O
=====


Maixduino supports basic arduino input and output functions. You can use them like other arduino boards.

In Maixduino, you can configure up to 32 pins into digital IO using any of the 48 FPIOs.

-----
## digitalRead()

### Description

Reads the value from a specified digital pin, either `HIGH` or `LOW` .

### Syntax

`digitalRead(pin)`

### Parameters

`pin` : the number of the digital pin you want to read.

### Returns

`HIGH` or `LOW`

### Notes and Warnings

Only pins that are set to the input function by the `pinMode()` can be read.

-----
## digitalWrite()

### Description

Write a `HIGH` or a `LOW` value to a digital pin.

### Syntax

`digitalWrite(pin, value)`

### Parameters

`pin`: the pin number

`value`: `HIGH` or `LOW`

### Returns

Nothing

### Notes and Warnings

Only pins that are set to the output function by the `pinMode()` can be write.

-----
## pinMode()

### Description

Configures the specified pin to behave either as an input or an output.

### Syntax

`pinMode(pin, mode)`

### Parameters

`pin`: the number of the pin whose mode you wish to set.

`mode`: `INPUT`, `OUTPUT`, `INPUT_PULLDOWN` or `INPUT_PULLUP`. 

### Returns

Nothing

### Notes and Warnings

This function must be called to set the pin state before calling digitalRead() or digitalWrite().

## Example Code

The code makes the digital pin 13 OUTPUT and Toggles it HIGH and LOW.

```
void setup() {
  pinMode(13, OUTPUT);    // sets the digital pin 13 as output
}

void loop() {
  digitalWrite(13, HIGH); // sets the digital pin 13 on
  delay(1000);            // waits for a second
  digitalWrite(13, LOW);  // sets the digital pin 13 off
  delay(1000);            // waits for a second
}
```
Sets pin 13 to the same value as pin 16, declared as an input.

```
int ledPin = 13;  // LED connected to digital pin 13
int inPin = 16;    // pushbutton connected to digital pin 16
int val = 0;      // variable to store the read value

void setup() {
  pinMode(ledPin, OUTPUT);  // sets the digital pin 13 as output
  pinMode(inPin, INPUT);    // sets the digital pin 16 as input
}

void loop() {
  val = digitalRead(inPin);   // read the input pin
  digitalWrite(ledPin, val);  // sets the LED to the button's value
}
```

