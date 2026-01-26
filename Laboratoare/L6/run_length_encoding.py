def run_length_encoding(text: str) -> str:
    if not text:
        return ""

    result = []
    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            current = ch
            count = 1

    result.append(f"{current}{count}")
    return "".join(result)


# exemplu
text = "aaabbbbcccdde"
print(run_length_encoding(text))  # a3b4c3d2e1
