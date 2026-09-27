def align_text(words: list[str], max_width: int) -> list[str]:

    result = []
    line = ""
    
    for word in words:

        if not line:
            line = word

        elif len(line) + 1 + len(word) <= max_width:
            line += " " + word

        else:
            result.append(line)
            line = word

    if line:
        result.append(line)

    return result

words = ["The", "quick", "brown", "fox"]
max_width = 10

print(align_text(words,10))