# grade_helper_buggy.py
#
# This program analyzes a list of quiz scores.
# It has several bugs. Your job: find them and fix them.
#
# When it is working, it should print exactly this:
#
#   Scores: [88, 92, 75, 64, 100]
#   Average: 83.8
#   Highest: 100
#   Passing: 4
#   Letter grade for average: B
#
# Tips:
#   - Run the program, read the error message, and fix one bug at a time.
#   - Some bugs crash the program. Others run but give the wrong answer.
#   - Keep a list of each bug you found and how you fixed it.


def main():
    scores = [88, 92, 75, 64, 100]
    print("Scores:", scores)

    avg = average(scores)
    print("Average:", avg)

    print("Highest:", highest(scores))

    # "Passing" means a score of 75 or higher
    print("Passing:", count_passing(scores))

    print("Letter grade for average:", letter_grade(avg))

main()


def average(scores)
    total = 0
    for s in scores:
        total = total + s
        return total / len(score)


def highest(scores):
    best = scores[0]
    for s in scores:
        if s > best:
            best = s
    print(best)


def count_passing(scores, cutoff):
    count = 0
    for s in scores:
        if s > cutoff:
            count = count + 1
    return count


def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"
