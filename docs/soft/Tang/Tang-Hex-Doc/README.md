# Tang-Hex-Doc

Documentation for ZYNQ XC7Z020 FPGA Based Tang-Hex Board.

## Build Doc


This documentation site is powered by [Hugo](https://gohugo.io/).

You need Hugo to be able to build the site.

To install Hugo(0.53 or higher):

```
wget -O /tmp/hugo.deb https://github.com/gohugoio/hugo/releases/download/v0.55.5/hugo_0.55.5_Linux-64bit.deb

sudo dpkg -i /tmp/hugo.deb
```

Get Doc source code:
```
sudo apt install git 
git clone https://github.com/sipeed/Tang-Hex-Doc.git
```

Install submodules:

```
cd Tang-Hex-Doc
git submodule init
git submodule update
```

Serve as a website:

```
hugo server
```

Then visit http://localhost:1313