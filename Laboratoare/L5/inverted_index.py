import re

def inverted_index(documents: list[str]) -> dict[str, set[int]]:
    index = {}

    for i, doc in enumerate(documents):
        words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿĂÂÎȘȚăâîșț]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿĂÂÎȘȚăâîșț]+)*",
                           doc.lower())

        for w in set(words):  # o singură dată per document
            if w not in index:
                index[w] = set()
            index[w].add(i)

    return index


# exemplu
documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]
print(inverted_index(documents))

