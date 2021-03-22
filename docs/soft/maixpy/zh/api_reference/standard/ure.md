---
title: ure – 简单的正则表达式
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: ure – 简单的正则表达式
---



该模块实现了相应CPython模块的子集，如下所述。 有关更多信息，请参阅原始CPython文档：[re](https://docs.python.org/3.5/library/re.html#module-re).

该模块实现了正则表达式操作。 支持的正则表达式语法是CPython`re`模块的子集（实际上是POSIX扩展正则表达式的子集）。

## 支持的运算符和特殊序列

* `.` : 匹配任何字符。

* `[...]` : 匹配字符集。 支持单个字符和范围，包括否定集（例如`[^ a-c]`）。

* `^` : 匹配字符串的开头。

* `$` : 匹配字符串的结尾。

* `?` : 匹配零个或前一个子模式之一。

* `*` : 匹配前一个子模式的零个或多个。

* `+` : 匹配前一个子模式中的一个或多个。

* `??` : 非贪婪版的`？`，匹配零或一，偏好为零。

* `*?` : `*`的非贪婪版本，匹配零或更多，优先选择最短匹配。

* `+?` : 非贪婪的“+”版本，匹配一个或多个，优先匹配最短。

* `|` : 匹配此运算符的左侧或右侧子模式。

* `(...)` : 分组。 每个组都在捕获（它捕获的子字符串可以使用`match.group（）方法访问）。

* `\d` : 匹配数字。 相当于`[0-9]`。

* `\D` : 匹配非数字。 相当于`[^ 0-9]`。

* `\s` : 

* `\S` : 匹配空白。 相当于 `[^ \t-\r]`.

* `\w` : 匹配“单词字符”（仅限ASCII）。 相当于 `[A-Za-z0-9_]`.

* `\W` : 匹配非“单词字符”（仅限ASCII）。 相当于 `[^A-Za-z0-9_]`.

* `\` : 转义字符。 除了上面列出的那些之外，反斜杠后面的任何其他字符都是字面意思。 例如，`\*`等同于文字`*`（不被视为`*`运算符）。 请注意，`\r`，`\n，`等不是专门处理的，并且相当于文字字母`r`，`n`等。因此，不建议使用原始Python字符串（`r“”`）用于正则表达式。 例如，`r“\r \n”`用作正则表达式时相当于`“rn”`。 要匹配CR后跟LF的字符，请使用`"\r\n"`。

## 不支持的表达式

* 重复计算 (`{m,n}`)
* 命名组 (`(?P<name>...)`)
* 非捕获组 (`(?:...)`)
* 更高级的断言 (`\b, \B`)
* 像`\r`，`\n`这样的特殊字符转义 - 使用Python自己的转义
* 其它


例子：

```python
import ure

# As ure doesn't support escapes itself, use of r"" strings is not
# recommended.
regex = ure.compile("[\r\n]")

regex.split("line1\rline2\nline3\r\n")

# Result:
# ['line1', 'line2', 'line3', '', '']
```
## 方法

### ure.compile(regex_str[, flags])

编译正则表达式， 返回[regex](http://docs.micropython.org/en/latest/library/ure.html?highlight=ure#regex) 对象。

### ure.match(regex_str, string)

编译regex_str并匹配字符串。 匹配始终从字符串中的起始位置开始。

### ure.search(regex_str, string)

编译regex_str并在字符串中搜索它。 与`match`不同，这将搜索字符串以匹配正则表达式的第一个位置（如果正则表达式被锚定，它仍然可以是0）。

### ure.sub(regex_str, replace, string, count=0, flags=0)

编译regex_str并在字符串中搜索它，用replace替换所有匹配项，并返回新字符串。

replace可以是字符串或函数。 如果它是一个字符串，那么`\<number>`和`\g<number>`形式的转义序列可用于扩展到相应的组（或不匹配组的空字符串）。 如果replace是一个函数，那么它必须采用一个参数（匹配）并且应该返回一个替换字符串。

如果指定了count并且非零，那么在进行许多替换之后，替换将停止。 flags参数被忽略。

注意：此函数的可用性取决于`MicroPython port`。

### ure.DEBUG

标记值，显示有关已编译表达式的调试信息。 （可用性取决于`MicroPython 移植实现`。）


## Regex 对象

编译了的正则表达式。 使用`ure.compile()`创建此类的实例。

### regex.match(string) regex.search(string) regex.sub(replace, string, count=0, flags=0)

类似于模块级函数`match（）`，`search（）`和`sub（）`。 如果将相同的正则表达式应用于多个字符串，则使用方法会更高效。

### regex.split(string, max_split=-1)

使用正则表达式拆分字符串。 如果给出 max_split，则指定要执行的最大拆分数。 返回字符串列表（如果指定了，则最多可以有 max_split + 1 个元素）。


## Match 对象

匹配`match（）`和`search（）`方法返回的对象，并传递给sub（）中的替换函数。

### match.group(index)

返回匹配（子）字符串。 整个匹配的索引为0，每个捕获组的索引为1和更高。 仅支持数字组。

### match.groups()

返回包含匹配组的所有子串的元组。

注意：此方法的可用性取决于`MicroPython 移植实现`。

### match.start([index]) match.end([index])

返回匹配的子字符串组的开头或结尾的原始字符串中的索引。 index默认为整个组，否则将选择一个组。

注意：这些方法的可用性取决于`MicroPython 移植实现`。

### match.span([index])


返回2元组`（match.start（index），match.end（index））`。

注意：此方法的可用性取决于`MicroPython 移植` 是否实现。


