def is_palindrome(text: str) -> bool:
    # ignoră litere mari și spațiile
    cleaned = "".join(ch.lower() for ch in text if ch != " ")
    return cleaned == cleaned[::-1]


# exemplu
text = "A man a plan a canal Panama"
print(is_palindrome(text))  # True
