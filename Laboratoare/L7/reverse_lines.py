def reverse_lines(input_file: str, output_file: str) -> None:
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            # eliminăm newline-ul, inversăm caracterele, apoi adăugăm newline
            reversed_line = line.rstrip("\n")[::-1]
            outfile.write(reversed_line + "\n")


# exemplu de utilizare
reverse_lines("input.txt", "output.txt")
