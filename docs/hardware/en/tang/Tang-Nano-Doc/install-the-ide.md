# Install the IDE

> Edit on 2022.07.14

- Educational edition is not recommended because it supports little chip
- **Float license only suits IDE version before 1.9.8**
- All docs can be found here https://www.gowinsemi.com/en/support/database/

## Install the IDE

- The IDE can be downloaded on this page http://www.gowinsemi.com.cn/faq.aspx

![](./assets/install-ide.png)

> Because of the IDE updating, the screenshot is created on 2022.04.06

Download the software and install it. This is not a difficult work.

Make sure you have installed all components.

<html>
<div class="imbox">
    <img src="./../../../zh/tang/Tang-Nano-Doc/get_started/assets/IDE-2.png" width=350>
    <img src="./../../../zh/tang/Tang-Nano-Doc/get_started/assets/IDE-4.png" width=350>
<style>
.imbox{
     display:flex;
     flex-direction: row;
     }
</style>
</div>
</html>

- Once finishing installing, there are 2 drivers to be installed.

![](./assets/ide-install-driver.png)

After installing all, there is an IDE icon is like this shown on your desktop.

![](./assets/ide-icon.png)

## Activate the IDE

Here are two ways to activate the IDE 

### Using local license

Here are two ways to apply for local license

#### Get license from gowin official website

Visit this page and fill those blanks, then just wait.
https://www.gowinsemi.com/en/support/license/

#### Get license from Sipeed

> Don't reapply for license from Sipeed if you have asked Gowin for license.

Normally the license email will be replied on Tuseday or Friday (GMT+8)

Send the applying license email to support@sipeed.com to get a local license.

The title of the email is `[Apply Tang Lic]MAC: xx-xx-xx-xx-xx-xx` , The content template is as follows :

```txt
Company name:
Company website:
Department:
Contact person:
Phone number:
Email :
PC MAC address:
license type: local shared (choose one)
Operating system: Windows Linux (choose one)
Country or Region:
```

It's suggested to use local MAC to apply for license, not the virtual MAC or wireless MAC

### Verify license

When you run GOWIN IDE first time, there is a license manager and you should add your license file into it correctly

![](./assets/lic-manager.png)

#### Using Float license

**Float license is only support IDE version before 1.9.8**

- Using the Float license requires the network

The server ip and port are shown below

![](./assets/using-float-lic.png)]


## Other

It may take a time to receive license. During this time we can read GOWIN official documents, which can easily be found after installing IDE.

There are three contents in the IDE installation path : IDE folder, Programmer folder, uninst.exe

![ide_folder](./../../../zh/tang/Tang-Nano-Doc/get_started/assets/ide_folder.png)

**IDE** folder：Here I suggest you view the **doc** folder, many GOWIN official documents are set in it like showing below.

![IDE](./../../../zh/tang/Tang-Nano-Doc/get_started/assets/doc-folder.png)

Programmer folder: There are also many documents

![IDE](./../../../zh/tang/Tang-Nano-Doc/get_started/assets/programmer-folder.png)

We suggest you delete the Programmer folder installed with IDE and use this version [Click me](https://dl.sipeed.com/shareURL/TANG/programmer)，which can reduse many troubles

uninst.exe：remove IDE


### Burn in linux

Here is a way to Flash the development board in linux [click me](./flash-in-linux.md)
 