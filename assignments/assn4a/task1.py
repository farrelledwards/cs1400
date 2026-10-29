def make_number_pyramid(rows):
    output = ""
    center = rows * (len(str(rows))+1) / 2
    for i in range(rows):
        line = ""
        for j in range(i+1):
            if j > 0:
                line += " "
            line += str(i+1)

        output += " " * int((center - (len(line)) / 2))
        output += line + "\n"
    return output

def main():
    rows = int(input("Number of rows:  "))
    output = make_number_pyramid(rows)
    print(output)

main()
