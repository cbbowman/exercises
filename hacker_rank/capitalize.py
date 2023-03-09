def capitalize(text: str) -> str:
    len_s = len(text)

    if len_s == 0:
        return text

    words = text.split(" ")

    for i, w in enumerate(words):
        words[i] = w.capitalize()

    output = " ".join(words)

    return output


input = "charlie bowman"
output = "Charlie Bowman"

assert capitalize(input) == output

input = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"
output = "Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"

assert capitalize(input) == output
