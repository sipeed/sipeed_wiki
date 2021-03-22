---
title: ure-simple regular expression
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: ure-simple regular expression
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [re](https://docs.python.org/3.5/library/re.html#module-re).

This module implements regular expression operations. The supported regular expression syntax is a subset of the CPython `re` module (actually a subset of POSIX extended regular expressions).

## Supported operators and special sequences

* `.`: matches any character.

* `[...]`: Match character set. Single characters and ranges are supported, including negative sets (eg `[^ a-c]`).

* `^`: Match the beginning of the string.

* `$`: match the end of the string.

* `?`: Match zero or one of the previous subpatterns.

* `*`: Match zero or more of the previous subpattern.

* `+`: Match one or more of the previous subpatterns.

* `??`: The non-greedy version of `? `, matches zero or one, and the preference is zero.

* `*?`: A non-greedy version of `*`, matching zero or more, preferring the shortest match.

* `+?`: Non-greedy "+" version, matching one or more, first matching the shortest.

* `|`: Match the left or right sub-pattern of this operator.

* `(...)`: grouping. Each group is capturing (the substring it captures can be accessed using the `match.group() method).

* `\d`: match numbers. Equivalent to `[0-9]`.

* `\D`: match non-digits. Equivalent to `[^ 0-9]`.

* `\s`:

* `\S`: matches whitespace. Equivalent to `[^ \t-\r]`.

* `\w`: ​​match "word characters" (ASCII only). Equivalent to `[A-Za-z0-9_]`.

* `\W`: match non-"word characters" (ASCII only). Equivalent to `[^A-Za-z0-9_]`.

* `\`: escape character. Except for those listed above, any other characters after the backslash are literal. For example, `\*` is equivalent to the literal `*` (not considered as the `*` operator). Please note that `\r`, `\n,`, etc. are not specially processed, and are equivalent to the text letters `r`, `n`, etc. Therefore, it is not recommended to use raw Python strings (`r""`) for regular expressions. For example, `r"\r \n"` is equivalent to `"rn"` when used as a regular expression. To match the characters of CR followed by LF, use `"\r\n"`.

## Unsupported expression

* Repeated calculation (`(m,n)`)
* Named group (`(?P<name>...)`)
* Non-capturing group (`(?:...)`)
* More advanced assertions (`\b, \B`)
* Escaping special characters like `\r`, `\n`-use Python's own escape
* Other


example:

```python
import ure

# As ure doesn't support escapes itself, use of r"" strings is not
# recommended.
regex = ure.compile("[\r\n]")

regex.split("line1\rline2\nline3\r\n")

# Result:
# ['line1','line2','line3','','']
```
## Method

### ure.compile(regex_str[, flags])

Compile the regular expression and return the [regex](http://docs.micropython.org/en/latest/library/ure.html?highlight=ure#regex) object.

### ure.match(regex_str, string)

Compile regex_str and match the string. The match always starts from the starting position in the string.

### ure.search(regex_str, string)

Compile regex_str and search for it in the string. Unlike `match`, this will search the string to match the first position of the regular expression (if the regular expression is anchored, it can still be 0).

### ure.sub(regex_str, replace, string, count=0, flags=0)

Compile regex_str and search for it in the string, replace all matches with replace, and return the new string.

replace can be a string or a function. If it is a string, then escape sequences of the form `\<number>` and `\g<number>` can be used to expand to the corresponding group (or an empty string that does not match the group). If replace is a function, then it must take one parameter (match) and should return a replacement string.

If count is specified and non-zero, then the replacement will stop after many replacements. The flags parameter is ignored.

Note: The availability of this function depends on the `MicroPython port`.

### ure.DEBUG

The tag value displays debugging information about the compiled expression. (Availability depends on the `MicroPython port implementation`.)


## Regex Object

The compiled regular expression. Use `ure.compile()` to create an instance of this class.

### regex.match(string) regex.search(string) regex.sub(replace, string, count=0, flags=0)

Similar to the module-level functions `match()`, `search()` and `sub()`. If the same regular expression is applied to multiple strings, the usage method will be more efficient.

### regex.split(string, max_split=-1)

Use regular expressions to split the string. If max_split is given, specify the maximum number of splits to perform. Returns a list of strings (if specified, there can be at most max_split + 1 elements).


## Match Object

Match the objects returned by the `match()` and `search()` methods and pass them to the substitution function in sub().

### match.group(index)

Returns the matching (sub)string. The index of the entire match is 0, and the index of each capture group is 1 and higher. Only number groups are supported.

### match.groups()

Return a tuple containing all substrings of the matched group.

Note: The availability of this method depends on the `MicroPython port implementation`.

### match.start([index]) match.end([index])

Returns the index in the original string of the beginning or end of the matched substring group. The index defaults to the entire group, otherwise a group will be selected.

Note: The availability of these methods depends on the `MicroPython port implementation`.

### match.span([index])


Return the 2-tuple `(match.start(index), match.end(index))`.

Note: The availability of this method depends on the implementation of `MicroPython port`.
