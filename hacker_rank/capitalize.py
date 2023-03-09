def capitalize(text: str) -> str:
    len_s = len(text)

    if len_s == 0:
        return text

    words = text.split()

    for i, w in enumerate(words):
        words[i] = w.capitalize()

    output = " ".join(words)

    return output


input = "charlie bowman"
output = "Charlie Bowman"

assert capitalize(input) == output
