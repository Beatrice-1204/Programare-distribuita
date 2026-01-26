def reverse_words(sentence: str) -> str:
    # split() fără argument elimină automat spațiile multiple și cele de la început/sfârșit
    words = sentence.split()
    words.reverse()
    return " ".join(words)


# exemplu
sentence = "soricel   un cu  joaca se   pisica"
print(reverse_words(sentence))  # pisica se joaca cu un soricel
