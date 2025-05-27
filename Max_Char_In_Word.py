
from typing import Tuple
from collections import defaultdict


def max_char_in_word(word: str) -> Tuple[str, int]:
    if not word and word.strip == "":
        return ("", 0)

    char_dic = defaultdict(int)
    for char in word:
        char_dic[char] += 1
    max_char = ("", 0)

    for key, value in char_dic.items():
        if max_char[1] < value:
            max_char = (key, value)

    return max_char


words = ["", "Hello World", "Test Case 2",
         "Test Case 4", "A vey long word for Testing"]

outputs = [max_char_in_word(word) for word in words]

print(outputs)
