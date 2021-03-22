---
title: uctypes-access to binary data in a structured way
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: uctypes-access to binary data in a structured way
---


This module implements "external data interface" for MicroPython. The idea behind it is similar to CPython's `ctypes` module, but the actual API is different, streamlined and optimized for small size. The basic idea of ​​this module is to define a data structure layout with data roughly the same as the functions allowed by the C language, and then use the familiar dot syntax to access it to reference subfields.

> **Warning**
>
> The uctypes module allows access to any memory address of the machine (including I/O and control registers). Using it carelessly may cause crashes, data loss, and even hardware failure.

> **Also refer to**
>
> **[ustruct](ustruct.md) module**
>
> Standard Python methods for accessing binary data structures (does not scale well to large and complex structures).


Routine:

```python
import uctypes

# Example 1: Subset of ELF file header
# https://wikipedia.org/wiki/Executable_and_Linkable_Format#File_header
ELF_HEADER = {
    "EI_MAG": (0x0 | uctypes.ARRAY, 4 | uctypes.UINT8),
    "EI_DATA": 0x5 | uctypes.UINT8,
    "e_machine": 0x12 | uctypes.UINT16,
}

# "f" is an ELF file opened in binary mode
buf = f.read(uctypes.sizeof(ELF_HEADER, uctypes.LITTLE_ENDIAN))
header = uctypes.struct(uctypes.addressof(buf), ELF_HEADER, uctypes.LITTLE_ENDIAN)
assert header.EI_MAG == b"\x7fELF"
assert header.EI_DATA == 1, "Oops, wrong endianness. Could retry with uctypes.BIG_ENDIAN."
print("machine:", hex(header.e_machine))


# Example 2: In-memory data structure, with pointers
COORD = {
    "x": 0 | uctypes.FLOAT32,
    "y": 4 | uctypes.FLOAT32,
}

STRUCT1 = {
    "data1": 0 | uctypes.UINT8,
    "data2": 4 | uctypes.UINT32,
    "ptr": (8 | uctypes.PTR, COORD),
}

# Suppose you have address of a structure of type STRUCT1 in "addr"
# uctypes.NATIVE is optional (used by default)
struct1 = uctypes.struct(addr, STRUCT1, uctypes.NATIVE)
print("x:", struct1.ptr[0].x)


# Example 3: Access to CPU registers. Subset of STM32F4xx WWDG block
WWDG_LAYOUT = {
    "WWDG_CR": (0, {
        # BFUINT32 here means size of the WWDG_CR register
        "WDGA": 7 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
        "T": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
    }),
    "WWDG_CFR": (4, {
        "EWI": 9 << uctypes.BF_POS | 1 << uctypes.BF_LEN | uctypes.BFUINT32,
        "WDGTB": 7 << uctypes.BF_POS | 2 << uctypes.BF_LEN | uctypes.BFUINT32,
        "W": 0 << uctypes.BF_POS | 7 << uctypes.BF_LEN | uctypes.BFUINT32,
    }),
}

WWDG = uctypes.struct(0x40002c00, WWDG_LAYOUT)

WWDG.WWDG_CFR.WDGTB = 0b10
WWDG.WWDG_CR.WDGA = 1
print("Current counter:", WWDG.WWDG_CR.T)
```


## Define the structure layout

The structure layout is defined by a "descriptor"-a Python dictionary that encodes field names as keys and other attributes needed to access them as associated values:

```python
{
    "field1": <properties>,
    "field2": <properties>,
    ...
}
```

Currently, `uctypes` needs to specify the offset of each field. The offset is given in bytes from the beginning of the structure.

The following are coding examples for various field types:

* Scalar type:

```python
"field_name": offset | uctypes.UINT32
```

In other words, the value is a scalar type identifier and is ORed with the field offset (in bytes) at the beginning of the structure.

* Recursive structure:

```python
"sub": (offset, {
    "b0": 0 | uctypes.UINT8,
    "b1": 1 | uctypes.UINT8,
})
```

That is, the value is a 2-tuple, the first element is the offset, and the second is the structure descriptor dictionary (note: the offset in the recursive descriptor is related to the structure it defines). Of course, the recursive structure can be specified not only through the literal dictionary, but also by referring to the structure descriptor dictionary (defined above) by name.

* Array of primitive type:

```python
"arr": (offset | uctypes.ARRAY, size | uctypes.UINT8),
```

That is, the value is a 2-tuple, the first element is the ARRAY flag and the offset are ORed, and the second is the number of elements in the scalar element type ORed array.

*Aggregate type array:

```python
"arr2": (offset | uctypes.ARRAY, size, {"b": 0 | uctypes.UINT8}),
```

That is, the value is a 3-tuple, the first element of which is the ARRAY flag, which is related to the offset, the second is the number of elements in the array, and the third is the element type descriptor.

*Pointers to primitive types:

```python
"ptr": (offset | uctypes.PTR, uctypes.UINT8),
```

That is, the value is a 2-tuple, the first element is the PTR flag and the offset is ORed, and the second element is the scalar element type.

*Pointer to aggregate type:

```python
"ptr2": (offset | uctypes.PTR, {"b": 0 | uctypes.UINT8}),
```

That is, the value is a 2-tuple, the first element of which is the OR operation of the PTR flag and the offset, and the second element is the descriptor of the pointed type.

*Bitfield:

```python
"bitf0": offset | uctypes.BFUINT16 | lsbit << uctypes.BF_POS | bitsize << uctypes.BF_LEN,
```

That is, value is a scalar value that contains a given positioning field (the type name is similar to a scalar type, but the prefix is ​​"BF"), which is ORed with the offset of the scalar value containing the bit field, and further compared with the bit position And the value of bit length is "OR" operation. The bit fields within the scalar value are shifted by BF_POS and BF_LEN bits respectively. The bit field position counts from the least significant bit (position with 0) of the scalar, and is the number of rightmost bits of the field (in other words, it is the number of bits that the scalar needs to be shifted to the right to extract the bit field).

In the above example, first extract the UINT16 value at offset 0 (this detail may be important when accessing hardware registers, requiring specific access size and alignment), and then the rightmost bit is the lsbit bit of this UINT16 The bit field, and length is bitsize bits, will be extracted. For example, if lsbit is 0 and bitsize is 8, then it will effectively access the least significant byte of UINT16.

Note that bit field operations are independent of the target byte order, especially the above example will access the least significant byte of UINT16 in little-endian and big-endian structures. But it depends on the least significant bit being numbered as 0. Some targets may use a different number in their native ABI, but "uctypes" always uses the standardized number described above.

## Module content

### class uctypes.struct(addr, descriptor, layout_type=NATIVE)

Instantiate the "external data structure" object based on the address of the structure in memory, the descriptor (encoded as a dictionary) and the layout type (see below).

### uctypes.LITTLE_ENDIAN

The layout type of the little-endian compression structure. (Packing means that each field occupies the number of bytes defined in the descriptor, that is, the alignment is 1).

### uctypes.BIG_ENDIAN

The layout type of big-endian compression structure.

### uctypes.NATIVE

The layout type of the native structure-data byte order and alignment conform to the ABI of the system running MicroPython.

### uctypes.sizeof(struct, layout_type=NATIVE)

Returns the size of the data structure in bytes. The struct parameter can be a structure class or a specific instantiated structure object (or its aggregate field).

### uctypes.addressof(obj)

Returns the address of the object. The parameters should be bytes, byte arrays or other objects that support the buffer protocol (the address of the buffer is actually returned).

### uctypes.bytes_at(addr, size)

Capture memory as bytes object with given address and size. Since the bytes object is immutable, the memory is actually copied and copied into the bytes object, so if the memory content changes later, the created object will retain the original value.

### uctypes.bytearray_at(addr, size)

Capture the memory of the given address and size as a bytearray object. Unlike the bytes_at() function above, the memory is captured by reference, so it can also be written, and you will access the current value at the given memory address.

### uctypes.UINT8 uctypes.INT8 uctypes.UINT16 uctypes.INT16 uctypes.UINT32 uctypes.INT32 uctypes.UINT64 uctypes.INT64

The integer type of the structure descriptor. Provides 8, 16, 32, and 64-bit constants, including signed and unsigned.

### uctypes.FLOAT32 uctypes.FLOAT64

The floating-point type of the structure descriptor.

### uctypes.VOID

VOID is an alias of UINT8, used to conveniently define the void pointer of C: (uctypes.PTR, uctypes.VOID).
### uctypes.PTR uctypes.ARRAY

Enter constants for pointers and arrays. Please note that the structure has no explicit constants, it is implicit: the aggregation type without the PTR or ARRAY flag is a structure.

## Structure descriptors and instantiated structure objects

Given a structure descriptor dictionary and its layout type, you can use the `uctypes.struct()` constructor to instantiate a specific structure instance at a given memory address. Memory addresses usually come from the following sources:

*The predefined address when accessing the hardware registers on the bare metal system. Look up these addresses in the data sheet of the specific MCU/SoC.

*As the return value of calling some FFI (foreign function interface) functions.

*From uctypes.addressof(), when you want to pass parameters to the FFI function, or access certain data of I/O (for example, data read from a file or network socket).


## Structure Object

Structure objects allow access to a single field using standard dot notation: `my_struct.substruct1.field1. If the field is a scalar type, getting it will produce the original value (Python integer or floating point number) corresponding to the value contained in the field. Scalar fields can also be assigned to.

If a field is an array, you can use the standard subscript operator [] to access its individual elements-read and assign at the same time.

If a field is a pointer, it can be dereferenced using the [0] syntax (corresponds to the C * operator, although [0] also applies to C). It also supports subscribing to pointers with other integer values ​​(but 0), with the same semantics as in C.

All in all, access to structure fields usually follows C syntax, except for pointer dereference, when you need to use the [0] operator instead of *.

## Limit


* Access to non-scalar fields will cause intermediate objects to be allocated to represent them. This means that special attention should be paid to the layout of structures that need to be accessed when memory allocation is disabled (for example from interrupts). suggestions below:
  * Avoid access to nested structures. For example, instead of mcu_registers.peripheral_a.register1, a separate layout descriptor is defined for each peripheral and accessed as peripheral_a.register1. Or just cache specific peripherals: peripheral_a = mcu_registers.peripheral_a. If the register consists of multiple bit fields, you need to cache the reference to a specific register: reg_a = mcu_registers.peripheral_a.reg_a.
  * Avoid using other non-scalar data, such as arrays. For example, use peripheral_a.register0 instead of peripheral_a.register[0]. Similarly, another method is to cache intermediate values, such as register0 = peripheral_a.register [0].
* The offset range supported by the `uctypes` module is limited. The exact range of support is considered an implementation detail, and the general recommendation is to split the structure definition into a maximum value from a few kilobytes to tens of kilobytes. In most cases, this is a natural situation. For example, it does not make sense to define all MCU registers in a structure (expanded to 32-bit address space), but to define peripheral blocks through peripheral blocks. In some extreme cases, you may need to manually divide the structure of several parts (for example, if you access a native data structure with a multi-megabyte array in the middle, although this will be a very synthetic situation). )
