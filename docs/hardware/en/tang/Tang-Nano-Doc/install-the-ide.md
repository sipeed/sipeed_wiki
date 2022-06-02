# Install the IDE

> Edit on 2022.04.06

- Educational edition is not recommend because it supports few chips
- It's tested that we can use [GAO](Online debug tool Gowin Analysis Oscilloscope) on V1.9.8.1
- **Float license only suits IDE version before 1.9.8**
- All dosc can be found here https://www.gowinsemi.com/en/support/database/

## Install the IDE

- The IDE can be downloaded on this page http://www.gowinsemi.com.cn/faq.aspx

![](./assets/install-ide.png)

> Due to the IDE updating, the screenshot is created on 2022.04.06

Download the software and install it.This is not a difficult work.

Make sure install all components.

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

- When finishing installing, There are 2 drivers need to be installed.

![](./assets/ide-install-driver.png)

After installing all, There ia an IDE icon is like what is shown below on your desktop.

![](./assets/ide-icon.png)

## Other

It may take a time to receive license. During this time we can read GOWIN official documents, which can easily be found after installing IDE.

There are three contents in the IDE installation path : IDE folder, Programmer folder, uninst.exe

- **IDE** folder：Here I suggest you view the **doc** folder, many GOWIN official documents are set in it like showing below.

![IDE](./../../../zh/tang/Tang-Nano-Doc/get_started/assets/doc-folder.png)

- Programmer folder: There are also many documents

![IDE](./../../../zh/tang/Tang-Nano-Doc/get_started/assets/programmer-folder.png)

Normally we suggest you delete this Programmer folder and use this version [Click me](https://dl.sipeed.com/shareURL/TANG/programmer)，this can reduse many troubles

- uninst.exe：remove IDE

## Activate the IDE

- Here are two ways to activate the IDE 

### Using local license

- Here are two ways to apply for local license

#### Get license from gowin official website

Visit this page and fill those blanks, then just wait.
https://www.gowinsemi.com/en/support/license/

#### Get license from sipeed 

- Normally the license email will be replied on Tuseday or Friday (GMT+8)

The license from sipeed can not be used for V1.9.8 and version before V1.9.8

Send an apply license email to support@sipeed.com to get a local license.
The title of the email is [Apply Tang Lic]MAC: xxxxxx , the content should be like below:

```
Company name:
Company website:
Department:
Contact person:
Phone number:
Email :
PC MAC address:
license type: local or shared (choose one)
Operating system: Windows or Linux (choose one)
Country or Region:
```

- After receiving the license files, using the Browser of the license manager application to add the correct license file.

![](./assets/lic-manager.png)

### Using Float license

**Float license is only support IDE version before 1.9.8**

- Using the Float license requires the network

The server ip and port are shown below

![](./assets/using-float-lic.png)]

### Burn in linux

Here is a way to Flash the development board in linux [click me](./flash-in-linux.md)
 