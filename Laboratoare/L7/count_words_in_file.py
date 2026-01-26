def count_words_in_file(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # split() fără argument separă după orice spațiu (spații multiple, newline etc.)
    words = text.split()
    return len(words)


# exemplu de utilizare
print(count_words_in_file("example.txt"))
