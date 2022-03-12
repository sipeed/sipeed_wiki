---
title: Install on Linux
date: 2019-02-15T19:16:47+05:30
draft: false
---

Once you have downloaded the installer archive, open Terminal and cd into that directory.

```
cd <path to installer archive directory>
```

{{% notice note %}}
In this section, you will need **sudo** privileges.
{{% /notice %}}

The /opt directory is reserved for all the software and add-on packages that are not part of the default installation. Create a directory for your TD IDE installation.

```
sudo mkdir /opt/TD_DECEMBER2018
```

and extract TD into the /opt/TD_DECEMBER2018 directory:

```
sudo tar -xvf TD_DECEMBER2018_GOLDEN_RHEL.tar.gz -d /opt/TD_DECEMBER2018/
```

Create an ``/usr/bin/td`` executable by creating a new symbolic link from the ``/opt/TD_DECEMBER2018/bin/td``

```
sudo ln -s /opt/TD_DECEMBER2018/bin/td /usr/bin/td
```

Run TD IDE in GUI mode

```
$ td -gui
```
![TD GUI Mode](./../installing-USB-Driver/linux/87078310026779781.jpg "Tang Dynasty SDK in GUI Mode.")

Congratulations, you have installed the TD IDE on Linux.