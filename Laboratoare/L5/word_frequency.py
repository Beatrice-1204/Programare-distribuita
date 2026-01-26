import re

def word_frequency(text: str) -> dict:
    # litere (inclusiv diacritice) + cratimă/apostrof în interior (ex: s-au)
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿĂÂÎȘȚăâîșț]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿĂÂÎȘȚăâîșț]+)*",
                       text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


# exemplu
text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))
