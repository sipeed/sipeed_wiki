---
title: How to read this article correctly
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: how to read this article correctly
---


**Note: Currently the only official document website: [maixpy.sipeed.com](https://maixpy.sipeed.com)**


## First, please read carefully the directory structure on the left sidebar to take a look at the contents of the document

* **Introduction**: MiaxPy's introduction, works display, and development history, etc.
* **Getting Started**: The introductory tutorial for using MaxiPy, including the basic knowledge, must be read to avoid many problems and save a lot of time for subsequent development
* **Hand-in-hand tutorial**: Here is a step-by-step teaching of the use of various functions. It is useful for students who are just getting started and don’t know what to do. Read carefully.
* **API Manual**: API manuals of each functional module, convenient to refer to during programming
  * **Standard Library**: micropython standard library, many APIs are compatible with python3 APIs
  * **machine**: machine related, restart control, machine UID, and various peripheral control
  * **Maix**: Some special modules, such as FPIOA, KPU, FFT, etc.
  * **Built-in class**: Built-in class written in mpy (short for micropython), which can be found in the source code project
  * **Machine Vision**: Some machine vision related modules, image sensor lcd is roughly compatible with OpenMV API, but will not be updated with OpenMV in real time later
  * **Additional Peripheral Modules**: The use of some peripheral modules, such as touch screen, ultrasonic, LED lights, etc.
  * **Built-in applications**: Built-in applications, such as NES game console (FC gamer), pye (built-in document editor)
* **Frequently Asked Questions FAQ**: Summary of frequently asked questions
* **Advanced**: Some advanced gameplay, and how to participate in the modification of the document and the modification of the source code, or the contribution of the routine
* **Community & Sharing**: Collect some good tutorials, works, open source projects, etc. from the community. You can also share your own works or tutorials according to the contribution instructions

## Important must-read part

**Introduction** and **Getting Started Guide**, be sure to read them completely, and you must read it first if you encounter problems **FAQ**


## Start learning

* Just contact, you can read carefully from top to next page according to the table of contents on the left sidebar, just follow along, don’t skip the entry! ! !
* Learn how to update the firmware and how to write code. It is also very important to learn how to use a serial terminal. It is not recommended to rely too much on the IDE, especially when the program dies, the terminal may get more error messages, which is more conducive to solving the problem. When encountering problems and asking questions in the community, try to give complete information about the terminal operation
* Each module/library document is accompanied by a simple routine at the end, or here: [MaixPy_script](https://github.com/sipeed/MaixPy_scripts) to find the examples you need, you can try to run it to see the effect

## Learn to search

* Regarding the interface and parameters of the module, please refer to it according to your needs when using it. **There is a search box** in the upper right corner, which can be used well. At the same time, you can also use the browser's page search function, that is, press the keyboard <kbd> Ctrl +F </kbd>, then enter the content to be searched and press the confirm key
* Please don’t worry if there is anything you can’t find, you can go to the [issue](https://github.com/sipeed/MaixPy/issues) page of github to find (search and search) if anyone has mentioned it , If not, you can create a new issue, or go to [Forum](https://bbs.sipeed.com) to search for the issue, and don’t ask for help anymore, or contact technical support.

## FAQ of this document

* PDF generation is added to the document, but try not to spread the PDF version, because the PDF cannot be updated in time after the content is updated, try to visit this website (`https://maixpy.sipeed.com`) to view the document

* If the web page loads slowly, please try to refresh or wait, or change the line (try using a proxy or changing mobile phone data)

* This document has two domain names: `https://maixpy.sipeed.com` and `https://cn.maixpy.sipeed.com`, you can visit the other if you can’t access one

* The document uses gitbook to automatically generate static pages from markdown. If you encounter some pages that cannot be accessed, please check whether the URL (path) is correct, and you can return to the home page (`maixpy.sipeed.com`) and enter again.

For example, this URL is caused by a poor network condition and a quick click:
```
http://localhost:4000/zh/zh/how_to_read.html
```
The correct URL should be:
```
http://localhost:4000/zh/how_to_read.html
```



## MaixPy FAQ

* For frequently asked questions, please see [FAQ](./others/maixpy_faq.md)


## Other tutorials

* In addition to the documentation, you can also browse [blog](http://blog.sipeed.com), tutorials written by [BBS](https://bbs.sipeed.com) users, or Baidu search, and various developers’ Blogs, there will be many development tutorials, development diaries, etc., you can refer to

## Questioning skills

Ask questions in various places, whether it’s github or QQ groups, forums, or emails. When asking questions, try to provide complete steps to reproduce the problem. You should use the process you have gone through, how the problem occurred, and what the phenomenon is It must be fully explained. Don't be afraid of too many words. Think about the problem from the perspective of the solver. Can the developer solve the problem? It is convenient for developers to test and solve problems during their busy schedule!

For more details, please see the next section [How to ask questions elegantly](./how_to_ask.md)
