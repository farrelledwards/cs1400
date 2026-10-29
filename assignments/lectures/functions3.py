def average(scores):
    """Return the average of a list of numbers."""
    return sum(scores) / len(scores)

def letter_grade(avg):
    """Convert a numeric average to a letter grade."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"

def format_report(name, scores):
    """Build one line of text summarizing a student."""
    avg = average(scores)
    return name + ": average " + str(avg) + " -> " + letter_grade(avg)

def main():
    student_names = ["Ada", "Grace", "Linus", "Mork"]
    student_scores = [[95, 88, 92, 89], [72, 85, 78, 81], [55, 62, 48, 0], [25, 53, 68, 81]]

    for i in range(4):
        print(format_report(student_names[i], student_scores[i]))

main()