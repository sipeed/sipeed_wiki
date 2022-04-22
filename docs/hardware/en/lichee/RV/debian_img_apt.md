---
title: Problems
keywords: debian, Rv, Problam, apt, img, sipeed
---

## Apt problem

- When execute apt command in debian system it may show error as follows
  
> GPG error: http://ftp.ports.debian.org/debian-ports sid InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY E852514F5DF312F6

This means built-in key expires and need updating manually, here are two ways to download key.

 - Doanload from web page：https://packages.debian.org/sid/all/debian-ports-archive-keyring/download
 - wget : `wget http://ftp.cn.debian.org/debian/pool/main/d/debian-ports-archive-keyring/debian-ports-archive-keyring_2022.02.15_all.deb`
  
Copy doanloaded key (usr scp or lrzsz tool) into LicheeRV board, then run following command to update key:

> sudo dpkg -i debian-ports-archive-keyring_2022.02.15_all.deb

Then run `sudo apt-get update` to update apt.

