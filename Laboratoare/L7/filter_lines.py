def filter_lines(input_file: str, output_file: str, keyword: str) -> None:
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            if keyword in line:
                outfile.write(line)


# exemplu de utilizare
filter_lines("input2.txt", "filtered.txt", "Python")
