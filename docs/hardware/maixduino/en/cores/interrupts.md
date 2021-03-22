Interrupts
=====

In Maixduino, you can use up to 32 digital pins of the 48 FPIOs as external interrupts.

-----

## attachInterrupt()

### Description

Set Digital Pins With Interrupts.

### Syntax

`attachInterrupt(pin, ISR, mode)`

### Parameters

`pin`: the pin number

`ISR`: the ISR to call when the interrupt occurs; this function must take no parameters and return nothing. This function is sometimes referred to as an interrupt service routine.

`mode`: defines when the interrupt should be triggered. Five constants are predefined as valid values:

* `LOW` to trigger the interrupt whenever the pin is low,

* `CHANGE` to trigger the interrupt whenever the pin changes value

* `RISING` to trigger when the pin goes from low to high,

* `FALLING` for when the pin goes from high to low.

* `HIGH` to trigger the interrupt whenever the pin is high.

### Returns

Nothing

###  Example Code
```
#include <Arduino.h>

// constants
// PIN_KEY_PRESS = KEY0 = 15

// Key
volatile byte pressed = HIGH;
byte keyState = HIGH;

void keyPressChange()
{
  pressed = !pressed;
}

void setup()
{
  Serial.begin(115200);

  attachInterrupt(15, keyPressChange, CHANGE);
}

void loop()
{
  // if the button state has changed:
  if (pressed != keyState)
  {
    keyState = pressed;

    Serial.print("pressed key ");

    boolean isPressing = (keyState == LOW);
    if (isPressing) {
      Serial.println("is pressing");
    } else {
      Serial.println("is pressed");
    }
  }
}
```

###  Example Code with debounce
```
#include <Arduino.h>

// constants
// PIN_KEY_PRESS = KEY0 = 15
// PIN_KEY_DOWN         = 16
// PIN_KEY_UP           = 17

// Key
byte keys[] = {15, 16, 17};
#define NUMKEYS sizeof(keys)
volatile byte pressed[NUMKEYS];
byte keyState[NUMKEYS];
byte lastKeyState[NUMKEYS];

// Debounce
unsigned long lastDebounceTime[NUMKEYS];  // the last time the output pin was toggled
unsigned long debounceDelay = 50;         // the debounce time; increase if the output flickers

void keyPressChange()
{
  pressed[0] = !pressed[0];
}

void keyDownChange()
{
  pressed[1] = !pressed[1];
}

void keyUpChange()
{
  pressed[2] = !pressed[2];
}

void setup()
{
  for (byte i = 0; i < NUMKEYS; ++i)
  {
    pressed[i] = HIGH;
    keyState[i] = HIGH;
    lastKeyState[i] = HIGH;
    lastDebounceTime[i] = 0;
  }

  Serial.begin(115200);

  attachInterrupt(keys[0], keyPressChange, CHANGE);
  attachInterrupt(keys[1], keyDownChange, CHANGE);
  attachInterrupt(keys[2], keyUpChange, CHANGE);
}

void loop()
{
  unsigned long now = millis();

  for (byte i = 0; i < NUMKEYS; ++i)
  {
    // If the switch changed, due to noise or pressing:
    // reset the debouncing timer
    if (pressed[i] != lastKeyState[i])
    {
      lastDebounceTime[i] = millis();
    }

    // filter out any noise by setting a time buffer
    if ((now - lastDebounceTime[i]) > debounceDelay)
    {
      // if the button state has changed:
      if (pressed[i] != keyState[i])
      {
        keyState[i] = pressed[i];

        // react only when a key is released
        if (keyState[i] == HIGH)
        {
          switch (i)
          {
          case 0:
            Serial.println("pressed");
            break;

          case 1:
            Serial.println("down");
            break;

          case 2:
            Serial.println("up");
            break;
          }
        }
      }
    }
    
    lastKeyState[i] = pressed[i];
  }
}
```

-----

## detachInterrupt()

### Description

Turns off the given interrupt.

### Syntax

`detachInterrupt(pin)` 

### Parameters

`pin`: the pin number of the interrupt to disable

### Returns
Nothing
