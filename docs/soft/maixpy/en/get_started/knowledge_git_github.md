---
title: Introduction to git and github
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: introduction to git and github
---


Because in the process of learning MaixPy, git and github are used in many places, so here is a brief explanation of what they are and what are the differences.


## What is git

Git is a code hosting **software**, used to manage the version of the code.
such as:
I changed the code today, and then I changed the code tomorrow. From now on, I can see the history of these two changes, and what content was changed, which line can be accurate to find problems later;
Or I find that there is a problem with the code submitted for the second time, and I need to go back to the version after the first submission, which can be achieved with this tool;
In addition, it is convenient for multiple people to modify the same code, can manage the code submitted by everyone, and it is not easy to cause confusion.

No longer have to copy countless folders to back up changes!

Git will create a hidden folder `.git` in the directory, all changes are stored in it, and this folder cannot be deleted.

But it should be noted that the current git is mainly used to manage text files. It is not suitable to manage binary files, such as picture PDFs, etc., which will make the space occupied by the folder become large.

For specific tutorials, you can see [here](https://git-scm.com/), and Chinese tutorials can be viewed [here](https://www.liaoxuefeng.com/wiki/896043488029600/896067008724000)


## What is github

[github](http://github.com/) is a **website** for sharing code.

You can register on this website, then create a repository, put the code in this repository for public sharing, so that more people can use it, and even modify and optimize the code together. This is **open source**.

Each warehouse can be managed separately using the software `git`, you can modify the code on your computer, then use `git` to submit, and then use `git` to push to the website of `github`, you can See the new content.

The source address of MaixPy is: [https://github.com/sipeed/maixpy](https://github.com/sipeed/maixpy), which is a `git repository`.


[Help](https://docs.github.com/en/free-pro-team@latest/github), Chinese [Help](https://docs.github.com/cn/free-pro- team@latest/github)


In addition, there are several websites similar to `github` in China, such as [gitee](https://gitee.com/)


## The difference between git and github

One is a software, the other is a website.
It's just that this website uses git technology to manage the warehouse.

## Why can't I access github, or the access speed is very slow

Github is a foreign website. Because of the long distance and line problems, some lines of some operators may be slow or even inaccessible.
For example, the domain name `https://raw.githubusercontent.com/` used by github to store source files may not be accessible

Solution:
* Change the line, that is, change the network. For example, if you use a telecommunications network, you can change to China Mobile or China Unicom, change the mobile phone traffic, or change the location, etc.
* Use VPN software, not taught here, please pay attention to legal use



## What is star

On github, everyone can like and collect every public warehouse, that is, star, in the upper right corner of github ⭐ shaped button

![](../../assets/other/github_star.jpg)

If you think the project is good, please give it a star. This will encourage developers to spend more time maintaining the warehouse, and also tell first-time visitors that this is a good project and deserves attention.

After star, you can find your star warehouse in your profile, so you can find it next time

Having said that, everyone thinks that [MaixPy](https://github.com/sipeed/maixpy) is good, you can star one~

## What is the master branch

In each warehouse, there can be many branches, different branches can have different codes, and different branches can be merged with each other, which is convenient to save different versions of the code and facilitate teamwork. The master branch refers to the main branch. That is the most important branch, usually the master branch is displayed by default in the warehouse.


## What is submission

Submit, called `commit` in English, means that every time you change the code of the warehouse, you submit it once and it will be recorded in the submission history. You can see what was submitted this time at any time later, or you can roll back the code here. Commits

Each commit has an independent `commit ID`, such as `d28cb7ac7db5ad61c0738df95d733717deefda1d`, abbreviated as `d28cb7a`

## What is a submodule

Submodule, called `submodule` in English, means that other warehouses can be referenced in the warehouse, which is equivalent to a soft link. You don't need to put actual code in the warehouse, just put a link.
The advantage of this is that multiple warehouses can be managed separately. For example, `Warehouse 1` references `Warehouse 2` as a submodule. If the code of `Warehouse 2` is updated, `Warehouse 1` can choose to continue to use the old version of `Warehouse 2` Code, you can also choose to use the latest code of `Warehouse 2`, just update the submodule link

For example, `MaixPy` uses `kendryte-standalone-sdk` as a submodule, see [here](https://github.com/sipeed/MaixPy/tree/master/components/kendryte_sdk)
![submodule](../../assets/get_started/github_submodule.jpg)

You can see that the icon of the folder here is not the same, it is just a link, click will jump to the corresponding warehouse instead of opening the folder directly

So **MaixPy uses submodules**



## What is cloning

In the repository on `github`, if you need to download it locally, you need to use clone, use
```
git clone address
```
Just clone the warehouse locally. The cloned local warehouse is actually a clone on github, which is exactly the same, and keeps historical records, etc.

Of course, you don’t need to clone. The webpage has a download button, but the defect of downloading is that it will not include the history of the submitted code. Choose according to your own situation.

It should be noted that when cloning a repository that contains submodules, because cloning will only clone the link of the submodule by default, the code of the submodule is not cloned locally, you need to clone like this
```
git clone address --recursive
```

or
```
git clone address project_name
cd project_name
git submodule update --init --recursive
```

such as:
```
git clone https://github.com/sipeed/MaixPy --recursive
```



## What is issue

That is the meaning of the question. On github, each warehouse has a special place for asking questions, such as [MaixPy's issue](https://github.com/sipeed/MaixPy/issues)
Everyone asks questions here, similar to forums, they will be recorded for easy reference

## What is fork

On github, there is a fork button in the upper right corner of the warehouse page
![](/assets/other/github_star.jpg)
Click to fork the warehouse to your own warehouse, which is equivalent to a copy. The reason why it is called fork is that after you fork into your own warehouse, you can modify your own warehouse at will, which is regarded as a development branch of the original fork warehouse. Derived from it but not the same as it


## What is PR

That is, the pull request function on github is to participate in the code update of a warehouse. It is to fork into its own warehouse, then modify it, and submit and merge it into the forked source warehouse. The specific method can be learned by yourself
