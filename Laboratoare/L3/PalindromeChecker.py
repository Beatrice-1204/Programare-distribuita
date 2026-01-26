def is_palindrome(word):
    return word == word[::-1]


cuvant = input("Introdu un cuvant: ")

if is_palindrome(cuvant):
    print("Cuvantul este palindrom.")
else:
    print("Cuvantul nu este palindrom.")
