CS1400 - Thursday, January 15 - Lecture 4 - Module 1

# Topics:
* [🟥Assn 1a - What is CS & Snowman](#assn-1a---what-is-cs--snowman)
* [Responsible AI Use](#responsible-ai-use)
* [Code Lab Challenge 0 - The Bob Rossinator](#code-lab-challenge-0---the-bob-rossinator)


------------------------------------------------------------
# Announcements

## Cache Tech Community - RAM Fundamentals & Community Projects Showcase

*   **When**  1:30-3:30 PM Saturday, January 24th
*   **Where** Bridgerland Technical College, West Building, Room 1860, 1410 N 1000 W, Logan, UT 84321
*   **Discord** https://discord.gg/YNkqmVGZbS
In this presentation, you’ll learn about the fundamentals of how RAM works, why we use it, and how systems depend on it. We will also have a community project showcase where our community members are invited to showcase their personal projects! Projects can be anything that interests you and is related to technology!

https://www.cachevalley.co/posts/cache-tech-community-ram-fundementals-community-projects-showcase-january-2026/


## Global Game Jam 2026

*   **When**  Friday, January 30th - Saturday January 31st
*   **Where** Merrill-Cazier Library
*   **It's free!**  Plus, **we'll feed you!**
*   **Register** https://engineering.usu.edu/cs/game-jam/2026-ggj


## HackUSU 2026

*   **When**  February 27th-28th, 2026.
*   **Where** Huntsman Hall
*   [Registration](https://huntsman.usu.edu/hackusu/) is open to all college students and high school seniors.
    *   Register with the code `USU26` to save $5!

HackUSU is Utah's largest collegiate 24-hour innovation challenge and hackathon. Participants create innovative applications while networking with industry professionals and attending educational workshops.


# Action Items

*   I have office hours this afternoon from 1 PM to 4 PM
    -   Find me in SER 301E or on [Zoom](https://usu-edu.zoom.us/my/erik.falor?pwd=ZE4zNXRpNVl4VVhHNkN5Q2wwV3VrUT09)


# [🟥Assn 1a - What is CS & Snowman](https://usu.instructure.com/courses/794745/assignments/5122781)

Task/Day           | **Thursday**       | **Friday**                       | **Saturday** | **Sunday**                             | **Monday**                                   | **Tuesday**
-------------------|--------------------|----------------------------------|--------------|----------------------------------------|----------------------------------------------|-----------------
**Classroom Time** | Classroom Lab Time |                                  |              |                                        | 1.4: Input and Variables, 1.5: On Data Types | Classroom Lab Time
**Items Due**      |                    | Exercise 1.3.2<br/>Quiz 1.2, 1.3 |              | Assignment 1a<br/>Reflection Survey 1a | MLK Jr. Holiday<br/>**NO SCHOOL**            | Code Reviews for <br/>Assn 1a begin



## Upload Several Versions Of Your Assignments

*   You **do not** need to wait until you are completely finished to submit an assignment
*   There is **no penalty** for uploading multiple times
    -   We typically only look at the last one uploaded before the due date
    -   You will notice that Canvas adds a numbered suffix to each file name after the first (`-1`, `-2`, etc.)
    -   This is perfectly normal and does not pose any problems to your grader
*   It is a **good idea** to upload your progress at the end of each work period
    -   This way you can receive partial credit in case something happens to you or your computer before you are able to complete the assignment

Part of submitting homework is to *download* and *verify* your submission. **You will be graded on whatever is submitted, not on what you intended to submit.**



## How To Schedule Your Code Review

0.  Look at the queue to see how busy the Coaching Center is: https://elearn.usu.edu/tutor/queue/index.php?topic=NDIxMw
0.  Browse to https://elearn.usu.edu/tutor/request/
0.  Select **Computer Science**
0.  Choose our course **CS 1400**
0.  Enter your name
0.  Wait for your name to be called


# Responsible AI Use


### Do This

*   Ask for advice, not finished code: get explanations, pseudocode, debugging help
*   Get targeted help: explanations, suggestions, and error clarification
*   Strive to understand: rewrite AI code in your own style with comments; test and tweak
*   Test smarter: use AI to suggest edge cases, then run them yourself
*   Explain it: be ready to justify AI-assisted lines in plain English
*   Disclose use: state what AI helped with in your submission
*   Keep history: save your original work, AI suggestions, and final version

### Don't do this

*   Don't paste the whole assignment and submit AI's code
*   Don't submit AI-generated work as your own without understanding
*   Don't rely on AI to pass reviews - you must explain every line
*   Don't apply this AI policy to your other classes! Respect each professor's own boundaries.


# Code Lab Challenge 0 - The Bob Rossinator

In this challenge you will design and write a Python program using Drawly to create a Bob Ross-style landscape scene. The focus is on **program design**, **decomposition**, and **parameterized drawing**, not artistic perfection.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4*


### Program Requirements

Every good program begins with a *plan*.  This is something that my professors always told me, but it took many wasted hours before I really took this advice to heart.

I have sketched out how I would like this image to come together.


0.  Draw a grid in the background at 100px intervals
    *   Label the lines located at odd multiples of one-hundred 
0.  Title the drawing with two adjectives (á là "happy little trees")
    *   One adjective should describe an emotion
    *   The other one describes a size
0.  Choose a color to paint the sky
    *   Use colors from the [Pygame colors list](https://www.pygame.org/docs/ref/color_list.html)
    *   Draw the sky as a large rectangle that encompasses the entire canvas
    *   Draw a dark green rectangle of grass in the foreground (at a lower X coordinate)
0.  Choose X and Y coordinates for the sun
    *   Draw the sun as a yellow circle
0.  Choose X and Y coordinates for two clouds: a high cloud and a low cloud that appear in front of the mountain peaks
    *   Draw clouds as white ellipses at each X,Y coordinate pairs
    *   Make the high cloud appear before the low cloud
0.  Import the Drawly library
0.  Print the message `"Behold, my masterpiece!  [title of the drawing]"` to the terminal at the end of the program
0.  Draw mountains as a complex grey polygon
    *   Choose X,Y coordinates for each vertex of the polygon
    *   Take care that the penultimate point ends on the same Y coordinate as the very first point,
    *   And that the final point has X,Y coordinates equal to the first point
0.  Sign the painting as "Bob Rossinator" in black text in the lower-right corner of the image
0.  Choose a shade of blue for the lake
    *   Draw a lake (two overlapping ellipses) on top of the grass
0.  Choose a shade of green for the trees
    *   Draw 5 happy little triangles at carefully chosen points around the lake


### Phase 0 - Verify My Plan

You should verify that my ideas make sense before writing any code.  This will prevent you from painting yourself into a corner partway through the project.

Take a few minutes with your study buddy to review my plan.  Look for omissions or contradictions that will get you stuck.  You might do this by following my instructions while sketching the scene on a piece of paper.  If you catch yourself doing something out of order, so too will the Python program!

Answer each of these questions in today's Wooclap:

0. What is the user experience of this program?
0. What objects exist in the scene?
0. What should the final drawing look like when the program finishes?
0. What problems, contradictions, or omissions can you spot?


### Phase 1 - Pseudocode It

Using the answers to the above questions as your guide, write *pseudocode* as a block of comments in your program.

Start by describing the flow of the program in plain English:

- What order should everything happen?
- What happens when the program reaches the end?

Refine your pseudocode until it is as specific as Python code.


### Phase 2 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.  Work incrementally:

- Draw one element correctly
- If the object is repeated, copy the code that repeats it and adjust the coordinates
- Like a real artist, sign the painting when finished


### Phase 3 - Reflect On It

Answer these debrief questions in comments in today's Wooclap:

* Did my pseudocode line up with the code I wrote, or did I change course while coding? Why?
* What part of the program was hardest to design?
* What would I change if I had to start over?


### Phase 4 - Stretch Challenges

Did you finish early? Was this still too easy for you? Here are some more features to implement:

0. Add more details to the picture elements
    -   Tufts on clouds
    -   Waves on the lake
    -   Crags and gorges on the mountain faces
    -   Snow caps on the highest mountain peaks
    -   Leaves and branches on trees
    -   Texture to the grass
0. Introduce randomness to parts of the scene, such that the image comes out a little different each 
0. If you already know about loops and functions, group repeated blocks of code for reuse
    -   (If you don't know about these things, just wait, we'll get there!)


