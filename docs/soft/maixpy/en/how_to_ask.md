---
title: How to ask questions gracefully
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: how to ask questions gracefully
---


## When asking questions in various places, you will find several phenomena:

* No one answered after asking the question
* It took a long time for the question to be answered
* The other party always dislikes himself too much


## Before asking questions, make sure that you have already studied Getting Started Guide

The **Getting Started** chapter of this document is the basis of the basics of using `MaixPy`, no matter whether you have development experience, a big man or a novice, please be sure to read and operate it from front to back.

Many problems will be solved in this process. Don’t ask questions in QQ groups, forums, issues, or emails at the beginning. Many problems explained in the document at the beginning may not receive timely answers from the community, which saves everyone’s attention. Time, but also for a better community environment, everyone grows better together, please understand each other


## When asking questions, try to do the following points, which will greatly increase the probability of the problem being solved quickly:

### Clear the problem, figure out what happened and what I did, including:

* What effect and function do I want to achieve?

* In order to achieve this effect, how did I do it, and what is the detailed process?

* During the implementation process, what error occurred and what was the phenomenon (for example, what error was reported, what was the **complete** error content?)

* Have I read the error message carefully? Does the error message indicate the cause and solution of the error?

* Based on these error messages and careful thinking, can the problem be solved?

* Search for documents, issues, and whether you can find solutions to problems with search engines

### If the problem cannot be solved by yourself, you need to ask others for advice, and you need to consider:

* Who to ask, where to ask, who will be more likely to answer my question? And how about real-time?

* What data and phenomena should I provide him to be willing to help me solve the problem quickly?
  * Provide my purpose (to let the respondent know what you are doing)
  * Provide a complete implementation process, as well as the phenomena that occurred in the process (it is convenient for the respondent to follow your process to do it again, that is, the problem reproduces)
  * Give the wrong place and indicate where the phenomenon or result is different from what you expected! (Let the respondent know where it did not meet expectations)
  * Provide the error information that appears, it needs to be complete, as many screenshots as possible, more logs, don't cut a small picture stingly, or give a part of the log (because the respondent may not have done this for a long time , Forget some details, you need to quickly recall the screenshots and complete logs; and according to the detailed logs, you can quickly locate the problem)

* How can I be more sincere when asking questions? Even if I am noob, everyone is willing to answer



### Question template


Ask the question as elegant as possible, without adding extra modal particles, complaining vocabulary, consider every word and punctuation, and think about the question from the perspective of the answerer, how to let the answerer help him solve the problem quickly, the number of words is too few The description is unclear, too many words make people impatient

#### Title

Wherever you ask (including `QQ group`), draw up a title of about `30` for your question to clarify the central idea of ​​the question, including:
* Question category, is it asking questions, submitting bugs, sharing experience, etc. Let everyone know what you want to do on the screen full of text
* One sentence to clarify the central idea of ​​the problem, such as `Run the camera sample program, report an error reset fail, it may be a hardware problem`

So the title after synthesis can look like this:
* `[MaixPy question] Run the camera sample program and report an error reset fail. Could it be a hardware problem?

Such a title must **not** appear:
* `Ah ah ah ah why my board is not working again`
* `Why my code can't run anymore`
* `Why is my screen black?`
* `[MaixPy question] I received the development board, the development board screen is red, a line of small characters, why? `
* `I run the xxx program and something went wrong`

You can ask:
* `[MaixPy question] My board cannot be started after I connected the power reversely. How can I tell where the board is burned? If so, how can I save it?`~
* `[MaixPy BUG] pix_to_ai did not convert the last pixel`

#### Content

First of all, from the perspective of the answerer, if the question is asked:
* First of all, we must know what the other party is going to do and what goals to achieve
* In order to achieve this goal, where did he refer to the steps to do it
* What specific steps were actually taken, and then there was a problem at that step, so I can follow his steps to try to reproduce the phenomenon. If this problem seems to be difficult to solve and there are no steps to reproduce, it may take a lot of time to reproduce. Let’s put it aside and solve other problems first.
* What is the specific problem? If he only tells the problem, how do I know what is wrong with him, maybe it is unwell? So this is very important. He needs to explain the phenomenon when the problem occurred, and indicate what is different from the expectation. Otherwise, I have to guess what is the difference between the comparison and the expectation. The time to solve the problem has increased.
* If something goes wrong, I may need his log file so that I can look at the source code based on the log for analysis, otherwise it may be difficult to solve the problem, then this problem can be seen later

In summary, you can ask questions like this:

* Explain in detail your goals, what you want to do, and what the phenomenon should look like
* Do I refer to any documents, codes or teaching?
* How to reproduce the error: how to do it, write each step in detail until the problem occurs
* Explain in detail the phenomenon when the error occurs, and how it is different from what was expected, it is necessary to prove that the problem does occur
* Attached log files, screenshots, and even videos. The logs and screenshots must be complete. Don’t just take a small part. The answerer may find some problems you haven’t noticed from your complete logs and screenshots. This is very important !
* In addition, pay attention to the format of the pasted code, don’t display it messy after pasting, and it won’t enter your eyes. Try to copy and run it
* Finally, I would like to express my gratitude to the community friends who answered the question
