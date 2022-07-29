---
title: Why need firmware customization
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: why need firmware customization
---



Mainly to save memory.

The memory of the chip is `6MiB` general purpose memory + `2MiB` AI dedicated memory, which is really very large compared to ordinary single-chip microcomputers. If AI function is not used, we can use the entire `8MiB` memory.
But because many times we need to run a model, a model may reach `3MiB` or even larger, and the firmware also needs to take up memory.
So in order to run a larger model, we need to compromise and cut some unnecessary functions.

In the previous chapter of firmware update, many firmware versions were introduced and compiled, including `minimum`, `with_v4_support`, `with_ide_support`, and `with_lvgl`,
These firmwares may be used in different situations. such as:

* Cut IDE code, if you don't need to connect MaixPy IDE, you can cut IDE part to save memory.

* Cut the OpenMV function, the firmware is compatible with some functions of OpenMV, if you use the model, these functions may not be needed, you can cut it out.

* Tailoring multithreading support, if you don't need multithreading support, you can trim this part to get more memory space.

Therefore, if you are using a certain function, and you find the prompt `ImportError: no module named'XXX'`, it may be that you are using a firmware that does not include this function. For example, the `minimum` firmware does not include IDE and `image.find_blobs` Function, if this firmware is burned, it will be unable to connect for a long time if you connect to the `IDE` again. Using the function `image.find_blobs` will also prompt that the function definition cannot be found.
