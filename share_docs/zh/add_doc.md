# 分享文档

## 准备环境

- wiki 网站是使用 teedoc 构建的。因此需要先准备环境

### teedoc 说明

关于网站框架，使用时有疑问的话可以参考 https://teedoc.github.io/

### 本地构建网站

- 安装teedoc

```python
pip3 install teedoc --upgrade
```

- 获取网站源码

```bash
git clone https://github.com/sipeed/sipeed_wiki.git
```

- 安装对应插件
 
```bash
cd sipeed_wiki
teedoc install
```
- 本地构建网站

```bash
teedoc serve
```

然后访问 [http://127.0.0.1:2333](http://127.0.0.1:2333) 可以查看构建的网页

## 添加文档

一般来说文档都位于根目录下面的 docs 文件夹里面。

对于想要添加的文档在合适的对应目录下面编写完毕后，再在对应目录的 sidebar 文件中合适的位置添加后，可在网页中相应的位置看到相关的文档

然后可以在本地构建的网站中查看效果。

如果自己觉得已经完成的话可以提交 PR ，我们看到后会及时合并进去。