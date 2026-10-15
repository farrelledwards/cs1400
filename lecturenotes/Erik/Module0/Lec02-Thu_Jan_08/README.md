CS1400 - Thursday, January 08 - Lecture 2 - Module 0

# Topics:
* [🟥Assn 0 - PyCharm Setup](#assn-0---pycharm-setup)
* [Assignment 0 - PyCharm Setup](#assignment-0---pycharm-setup)
* [Setting Up PyCharm](#setting-up-pycharm)
* [How To Create Projects And Python Files In PyCharm](#how-to-create-projects-and-python-files-in-pycharm)
* [Test the ShowYourWork Plugin](#test-the-showyourwork-plugin)
* [How To Submit Assignments](#how-to-submit-assignments)
* [Python vs. PyCharm](#python-vs-pycharm)
* [How Code Reviews Will Work](#how-code-reviews-will-work)
* [Statement on Academic Integrity](#statement-on-academic-integrity)


------------------------------------------------------------
# Announcements

*   I have office hours today from 1 to 3 PM
    -   Need help getting your computer set up?  Have questions about programming in Python?
    -   Find me in SER 301E or on [Zoom](https://usu-edu.zoom.us/my/erik.falor?pwd=ZE4zNXRpNVl4VVhHNkN5Q2wwV3VrUT09)


## USU Spring STEM Career Fair

![](./00-spring-stem-career-fair-2026.png)

*   **When**  January 21st 3:00 PM-7:00 PM
*   **Where** TSC Lounge

Career Fairs are one of the most important events a student can attend while going to school. It is one of the most personable ways students and employers can network with each other for career opportunities.

The USU STEM Career Fair is open to all majors but is targeted towards Science, Technology, Engineering and Mathematics majors.  The STEM Fair provides students with the opportunity to network/recruit with technology-based companies.


## HackUSU 2026

HackUSU is Utah's largest collegiate 24-hour innovation challenge and hackathon. Participants create innovative applications while networking with industry professionals and attending educational workshops.

[Registration](https://huntsman.usu.edu/hackusu/) is open to all college students and high school seniors.

Register with the code `USU26` to save $5!

*   **When**  February 27th-28th, 2026.
*   **Where** Huntsman Hall
*   **24-hr Hackathon**
    -   Craft a software, or business proposal project to compete against other teams. All college students and high school seniors are invited!
*   **Networking**
    -   Come network with our sponsors and potential employers. There will be many industry experts to learn from and learn more about their companies!
*   **Workshops**
    -   We'll have many great workshops and tech talks on a variety of topics. Check back closer to the event for a complete list!
*   **Food**
    -   We'll provide dinner on Friday, and breakfast, lunch, and dinner on Saturday. There will also be plenty of snacks available the entire event!


# Action Items

0.  Take the [Get to Know You](https://usu.instructure.com/courses/794745/quizzes/1417463) survey on Canvas
    *   Please introduce yourself so I can get to know you as a person
    *   This is due **Friday, Jan 9th at 11:59 PM**
1.  Begin [Assn 0](https://usu.instructure.com/courses/794745/assignments/5122780) on Canvas
    *   This is due **Sunday, Jan 11th at 11:59 PM**
    *   After every assignment there is a [post-assignment reflection survey](https://usu.instructure.com/courses/794745/quizzes/1417469)
    *   These surveys are worth **5 points** and help me improve the course


# [🟥Assn 0 - PyCharm Setup](https://usu.instructure.com/courses/794745/assignments/5122780)

Task/Day           | **Thursday**             | **Friday** | **Saturday** | **Sunday**                           | **Monday**
-------------------|--------------------------|------------|--------------|--------------------------------------|---------------------------------------------
**Classroom Time** | Classroom Lab Time       |            |              |                                      | 1.2: Computer Science & Computer Programming
**Items Due**      | _Get To Know You Survey_ |            |              | Assignment 0<br/>Reflection Survey 0 |


# [Assignment 0 - PyCharm Setup](https://usu.instructure.com/courses/794745/assignments/5122780)

Welcome to the ~~first~~ zeroth assignment of the class.

This is really a pre-course assignment to make sure everything is set up and ready to go. Thus, the name, Assignment 0. Future assignment numbers correspond to the unit the assignment goes with.

You will be ready to do this after watching and reading these lessons in Canvas:

*   1.1: Computer Setup
*   1.1.1: Install Programs
*   1.1.2: Configure and Your First Assignment
*   1.1.3: Import Settings
*   1.1.4: Submitting Assignments

I'll walk through the steps you'll need to take to complete this assignment on your own.  **This will be the only assignment that I completely do for you in class.**


# Setting Up PyCharm

*This corresponds to lesson 1.1.2 in Canvas*

0.  You **do not** need to enable the Pro subscription
    *   PyCharm will nag you about it whether you enable it or not
    *   Pro has nothing that you can't live without
0.  [Import CS 1400 default PyCharm settings](https://usu.instructure.com/courses/794745/pages/1-dot-1-3-import-settings)
0.  Install the `Drawly` package for Python **v1.1.6**
    *   Open the "Python Packages" panel in PyCharm (looks like a cube with a Python logo)
    *   Click the chevron/down arrow symbol ︾ and select **PyPI**
    *   Type `drawly` into the text box and click **Install** next to its name
    *   This will simultaneously install the `pygame` package
0.  Install the `ShowYourWork` plugin for PyCharm **v4.0.2**
    *   You must be using the most recent version of PyCharm available *(see previous slide)*
    *   Open the Hamburger menu in the upper-left corner and go to **File** > **Settings**
    *   Find the **Plugins** item in the navigation tree on the left
    *   Click the **Marketplace** tab
    *   Search for `ShowYourWork`
        *   Look for the name *John Edwards* and the version number shown above
        *   The description will mention Utah State University Computer Science
    *   When you're on the right plugin, click **Install**, then **Apply**
    *   In the navigation tree to the left, expand the **Tools** item, then choose **ShowYourWork Settings**
    *   Enable the **Show File History Tab** checkbox
    *   Click **OK** to dismiss the settings dialog
0.  After installing **ShowYourWork** you may need to restart PyCharm for it to become active

This [short video](https://youtu.be/faCfXM6nwao) will walk you through the installation process and plugin features.  The appearance of the plugin may differ from the video, but the process should be the same.


# How To Create Projects And Python Files In PyCharm

0.  Launch PyCharm
0.  If it opens to a previous project, **File** → **Close Project**
0.  From the main screen create a **New Project**
    *   **Location:** Select a folder that you will be able to find later, and name this project with your own name and the assignment number
    *   ex. `Falor-Erik-Assn0`
    *   Uncheck the **Create Git Repository** box
    *   Uncheck the **Create a welcome script** box
0.  Set up the Python interpreter
    *   **Interpreter type:** Choose *Custom Environment*
    *   **Environment:** Choose *Select existing*
    *   **Type:** Choose *Python*
    *   **Python path:** Choose the one that matches the version you most recently installed
0.  Click **Create**, sit back and relax while PyCharm updates its skeletons


# Test the ShowYourWork Plugin

0.  Look for two tabs at the bottom of code editor windows:
    -   `Text`
    -   `File History`
0.  Write something in the editor
0.  Then change your mind and erase it and write something else
0.  Click `File History` and drag the scrubber to the left until your original text appears
0.  Click the curved **revert** button to undo your changes up to that point
0.  Click `Text` and behold the original text

*TL;DR this is a neat way to fix a broken program when you get stuck*

## Troubleshooting

*   This feature must be manually enabled in PyCharm's settings - installing the ShowYourWork plugin alone is not enough
    *   After installing the plugin, Open the Hamburger menu in the upper-left corner and go to **File** > **Settings**
    *   In the navigation tree to the left, expand the **Tools** item, then choose **ShowYourWork Settings**
    *   Enable the **Show File History Tab** checkbox
    *   Click **OK** to dismiss the settings dialog
*   The `Text` and `File History` tabs will not appear on any editor windows that were already open when **File History** was enabled
    *   Close and re-open them
*   Sometimes this plugin makes PyCharm freeze or otherwise misbehave.  If this happens to you:
    -   Close PyCharm
    -   Locate your project in your computer's file browser (Finder on macOS or Explorer on Windows)
    -   Delete the `_showyourwork.sqlite` file
    -   Restart PyCharm

If you have any trouble with the software, you can reach out to the Coaching Center or the instructor for help


# How To Submit Assignments

*This corresponds to lesson 1.1.2 in Canvas*

2.  Make the standard banner a code template in PyCharm so you'll never forget it
    *   `File` → `Settings` → `Editor` → `File and Code Templates`
    *   Select `Python Script` and input text like this:
    *   ```
        # CS 1400 - TR 10:30
        # Erik Falor

        ```
    *   Notice the blank line at the bottom. That is there on purpose!
3.  Create a new Python file and write `print("Hello World")`
    *   Look! Your standard banner is already there!
4.  Run this script with the green "run" button
    *   A black and white text terminal should pop up at the bottom of PyCharm full of text
    *   Look for the words `Hello World` along with `Process finished with exit code 0`; those are both indications of success
5.  Zip up the project for submission on Canvas
    *   **Windows Users**
        *   Locate the folder in File Explorer
        *   Right-click the folder → `Compressed to Zip File`
        *   *Older versions of Windows:* Right-click the folder → `Send To` → `Compressed Zip`
    *   **macOS Instructions**
        *   Locate the folder in Finder
        *   Right-click/Control-click the folder → `Compress "Folder Name"`
6.  Navigate to the assignment page on Canvas
    *   Click the blue **Submit Assignment** button in the bottom-right corner of the page
    *   Click **Choose a file to upload**
    *   Navigate to your Zip file in the file browser and select it
7.  Download the Zip file to verify that no files are missing
    *   Extract the Zip file into a fresh location - don't overlap with your original project
    *   Close PyCharm and re-open it at the new location
    *   Test this copy of your program.  If it works exactly the same as the original version, then you can be confident that it will run just as well on your grader's computer.


## What Happens If I Turn Something In Late?

See [Due Dates/Late Policy/Accommodations](https://usu.instructure.com/courses/794745/pages/due-dates-slash-late-policy-slash-accommodations)


# Python vs. PyCharm

During our last lecture we installed several programs, many with similar-sounding `Py` names. If that left you puzzled, let's unpack it.

*   **Python** is a *programming language*
    *   `python3` is a program that translates text files written in the Python language to instructions that your computer can follow
    *   `drawly` is like a plugin for Python - it can be included to enhance your Python programs
*   **PyCharm** is a tool that *helps you write and run Python programs*
    *   Strictly speaking, you don't need PyCharm to write or run Python programs; but it does make it easier
    *   On the other hand, PyCharm is useless without Python
    *   `ShowYourWork` is a plugin for PyCharm

It's okay if this distinction is still unclear for you now.  As you spend more time with these tools you will begin to understand their roles and how they work together.


# How Code Reviews Will Work

Always keep in mind my goal for you: **You will have a profound learning experience and become a thoughtful problem solver.**

If you want to do well, read this, follow it, and show up prepared.

[Syllabus: This is a Flipped Classroom](https://usu.instructure.com/courses/794745/assignments/syllabus#dp-syllabus-nav_link_7)


# Statement on Academic Integrity
*And how to use AI responsibly*

See the [Statement on Academic Integrity](https://usu.instructure.com/courses/794745/pages/statement-on-academic-integrity)

If you want to disable PyCharm's Machine Learning-Assisted Code Completion, do this:

*   Go to `File` → `Settings` → `Editor` → `General` → `Inline Completion`
*   Uncheck the box labeled `Enable local Full Line completion suggestions`
*   Click `OK` to dismiss the dialog


