CS1400 - Tuesday, January 06 - Lecture 1 - Module 0

# Topics:
* [Get To Know Your Professor](#get-to-know-your-professor)
* [Let's Get To Know Each Other](#lets-get-to-know-each-other)
* [How To Find These Lecture Notes](#how-to-find-these-lecture-notes)
* [What To Expect From This Course](#what-to-expect-from-this-course)
* [Installing Python and PyCharm on macOS](#installing-python-and-pycharm-on-macos)
* [Installing Python and PyCharm on Windows](#installing-python-and-pycharm-on-windows)


------------------------------------------------------------
# Get To Know Your Professor

Hi, I'm Erik Falor, your professor this semester.

I was fascinated by computers from a young age, but it wasn't until I was in eighth grade that my family got our first computer. In High School I considered myself to be "good with computers," but I didn't begin programming until I was 21. I did not fit in with my peers who could truly call themselves "computer nerds": I am bad at math and I don't particularly enjoy *Star Trek*, *Dungeons and Dragons*, or *Magic: The Gathering*.

I started college as a Communications major but shifted to Computer Science after taking a two-year break from school. My late start meant that I had to play catch-up with classmates who had been programming from a very young age. This is how I learned I wasn't as good at computers as I thought. I remember being intimidated by my classmates who had programmers for parents, went to programming summer camps, made their own video games, and generally understood the jargon words my professor spoke. It felt so humiliating to be shown up by kids who were 2 or 3 years younger than me!

I stuck with the program and earned my Bachelor's degree. I went on to spend 13 years as a software engineer at Spillman Technologies, Inc. (now Motorola Solutions) and Automated Products Group. Midway through my career I began studying for my Master's Degree part-time here at USU, and graduated in the fall of 2016. After teaching as an adjunct the following spring, I found a love for education and have been a teacher ever since.

As a person, these are...

<details>
<summary>some things that I <em>don't</em> like</summary>

0.  Counting from `1`
0.  Bloated normie OSes (such as Microsoft® Windows™, Apple® macOS™, etc.)
0.  Desktop Environments
0.  Office Suites with their pretentious "rich" file formats
0.  Mainstream music

</details>


<details>
<summary>some things that I <em>do</em> like</summary>

0.  Counting from `0`
0.  Linux
0.  Tiling window managers
0.  OG plain-text files, Markdown, and $`\LaTeX`$
0.  Lately I've been listening to shoegaze & dream pop. These are some of the bands I like the most:
    *   Deftones
    *   Hum
    *   Pure Hex
    *   Slowwves
    *   She's Green
    *   Keep
    *   Blossom
    *   Whirr

</details>


### There is no such thing as a stupid question in this classroom...

![Ten Thousand - https://xkcd.com/1053/](./10-ten-thousand.png)

...though some questions are not germane to the lecture.  You are always welcome to stay after class or come to my office to ask off-topic questions.


# Let's Get To Know Each Other

Now that you know a little bit about me, let's get introduced to each other on [Wooclap](https://app.wooclap.com/TYRMDZ)


# How To Find These Lecture Notes

These lecture notes contain supplementary material presented in class.  Demos, code examples written in class, and other important resources are published here.

You can easily locate them from Canvas 

0.  Navigate to the course homepage on Canvas
1.  Beneath the picture of Old Main is a navigation bar
2.  Click on the link labeled **Lecture Notes**

![](./14-canvas-homepage.png)

Once you've arrived, scroll down the main page until you locate the **Table of Contents**.  Lecture topics are organized chronologically.


### Important! Use the Eduroam WiFi network

To access this website while on campus you **must** use the **Eduroam** WiFi network.  You *cannot* reach my lecture notes from the **USU Guest** network.

![](./14-use-eduroam.png "Use Eduroam")

*Ironically, you can freely access the lecture notes from anywhere else on the net.*


# What To Expect From This Course

> Why isn't this introductory course called "CS 1010" like all of the other introductory courses on campus?

This course stands apart for its reputation of being challenging and time-consuming. The number **1400** signals that this course is a step up in difficulty from a typical 1010 class.

> What's up with this course being 4 credit hours? All of my other "introduction to ..." courses are only 3 hours.

If you browse the university catalog you will discover other 4 credit hour introductory courses. Interestingly, they all have something in common: they are about *foreign languages*.  Programming languages may be the most foreign of all, since they are for communicating with artificial minds!

Consider this analogy: Suppose that you want to learn the philosophy of Plato, which is a different way of thinking.  You'll need a good teacher.  If you had a time machine, you could go back to Ancient Greece and learn from Plato himself.

![](./16-plato-quote-english.webp)

<details>
<summary>There is just one problem: <em>you will need to learn Ancient Greek at the same time!</em></summary>

![](./16-plato-quote-greek.webp)

</details>

This class poses a similar challenge:

0.  You must learn to *think* like a computer...
1.  ...by communicating with a computer in *its language*

Believe it or not, learning the language is not the hard part; you'll be comfortable with Python by the end of the semester.  Retraining your mind to *think* like a computer is a lifelong pursuit.  Learning both things at once is the unique challenge of Computer Science.  The subject is not inherently more difficult than others, but the need to do it in a foreign language will slow your progress.  For this reason, you should plan to spend *more* time on this class than others.

**TL;DR - Don't procrastinate! Start assignments early and expect to get stuck from time to time.**


![](./16-peanut-butter-jelly-time.webp)

To help you understand what you've signed up for, let's find out if you can tell a robot how to make a PB&J.


# Installing Python and PyCharm on macOS

*This corresponds to lesson 1.1.1 in Canvas*

*Note: these version numbers are current as of this lecture*

0.  Python **v3.13.11** from https://www.python.org
    *   You should install the latest *active* version of Python, even if your computer already has another version installed
    *   Avoid *pre-release* or *release candidate* versions.  These versions are still being tested and may have bugs!
1.  PyCharm **v2025.3.1** from https://www.jetbrains.com/pycharm/download/?section=mac
    *   Be sure to download an installer that is compatible with your CPU
        1.  Press Command + Space to open Spotlight Search
        2.  Type `terminal` in the search bar
        3.  Click on the Terminal app icon or press **Enter** to open it
        4.  Type `uname -m` and press **Enter**
            *   If the output is `x86_64`, your Mac has an *Intel* processor - download the **.dmg (Intel)** installer
            *   If the output is `arm64`, your Mac has an *Apple Silicon* processor (M3, M4, etc.) - download the **.dmg (Apple Silicon)** installer


# Installing Python and PyCharm on Windows

*This corresponds to lesson 1.1.1 in Canvas*

*Note: these version numbers are current as of this lecture*

0.  Python **v3.13.11** from https://www.python.org
    *   You should install the latest *active* version of Python, even if your computer already has another version installed
        -   I haven't had much luck with the version of Python from the Windows App Store
        -   If it gives you trouble, I'll tell you to replace it with the official version
    *   Avoid *pre-release* or *release candidate* versions.  These versions are still under test and may have bugs!
1.  PyCharm **v2025.3.1** from https://www.jetbrains.com/pycharm/download/?section=windows
    *   This only works on Windows 10 and above
    *   It is not compatible with 32-bit versions of Windows

If your computer does not meet the requirements to run these programs, you can work in many of the on-campus computer labs.  *Not all labs have our software already installed,* so you should check with the facilitators to see if your favorite lab can meet your needs: https://it.usu.edu/labs/computer-labs/

*   The lab on the 3rd floor of the ENGR building is particularly nice.  Their computers already have Python and PyCharm ready to go.
*   If you use a lab, be sure to **frequently** zip and submit your partial assignments to Canvas.


# Action Items

## Get Ready For The Semester

0.  Read and understand these Canvas resources:
    *   [Getting Help](https://usu.instructure.com/courses/794745/pages/getting-help)
    *   [Getting Ready](https://usu.instructure.com/courses/794745/pages/getting-ready)
    *   [How to be Successful in this Course](https://usu.instructure.com/courses/794745/pages/how-to-be-successful-in-this-course)
    *   [CS Coaching Center](https://usu.instructure.com/courses/794745/pages/cs-coaching-center)
    *   [Statement on Academic Integrity](https://usu.instructure.com/courses/794745/pages/statement-on-academic-integrity)
    *   [Due Dates/Late Policy/Accommodations](https://usu.instructure.com/courses/794745/pages/due-dates-slash-late-policy-slash-accommodations)
0.  Take the [Get to Know You](https://usu.instructure.com/courses/794745/quizzes/1417463) survey on Canvas to introduce yourself to me
    *   This is due at *11:59 PM, Thursday, January 8*
0.  Begin [🟥Assn 0 - PyCharm Setup](https://usu.instructure.com/courses/794745/assignments/5122780)
    *   Assignments are typically due at 11:59 PM on Sundays
    *   Start working through the steps in the [1.1: Computer Setup](https://usu.instructure.com/courses/794745/pages/1-dot-1-computer-setup) lesson on Canvas
        *   If you encounter **any** trouble with your computer, reach out to me immediately!
    *   After every assignment there is a **post-assignment reflection survey** that is worth points


Task/Day           | **Tuesday**         | **Wednesday**        | **Thursday**             | **Friday** | **Saturday** | **Sunday**                           | **Monday**
-------------------|---------------------|----------------------|--------------------------|------------|--------------|--------------------------------------|---------------------------------------------
**Classroom Time** | Classroom Lab Time  | 1.1 - Computer Setup | Classroom Lab Time       |            |              |                                      | 1.2: Computer Science & Computer Programming
**Items Due**      |                     |                      | _Get To Know You Survey_ |            |              | Assignment 0<br/>Reflection Survey 0 |


# Announcements

## [Free Software and Linux Club](https://linux.usu.edu)  

I advise the Free Software and Linux Club (FSLC).  I was in this club more than 20 years ago as an undergrad, and am pleased that it is still helping students grow their skills.  The club is a great place to meet like-minded nerds, explore topics that aren't covered in classrooms, and to build your résumé.

* Work on real projects with Free and Open-Source Software  
* Build technical experience that stands out on your résumé  
* Practice leadership, collaboration, and presentation skills  
* Explore advanced Linux and software topics not covered in class  
* Connect with a network of peers passionate about technology  
* **Discord**: https://discord.gg/PvgG6N2hsU

If you're serious about leveling up your skills and showcasing more than just coursework, this is the place to be!



## Global Game Jam 2026

*   **When**  Friday, January 30th - Saturday January 31st
*   **Where** Merrill-Cazier Library

Come test your skills and make a game in 24 hours!  All kinds of games are possible:

*   Video Games
*   Board Games
*   Card Games
*   Yard Games

**It's free!**  Plus, **we'll feed you!**

https://engineering.usu.edu/cs/game-jam/2026-ggj

![](./ff-ggj.png)



## *RIGHT NOW* First Tuesday Thing

*   **When**  11:30-12:30 (right after this class)
*   **Where** in The Loop (SER Lounge)

Learn where to find my office, and join us for cake, soda, and games! Bring your Smash Bros skills to show who's boss!

![](./ff-ftt.png)


