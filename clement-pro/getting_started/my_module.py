def censor(text, word):
    result = ""

    i = 0
    while i < len(text):
        if text[i:i + len(word)] == word:
            for k in range(len(word)):
                result += "*"
            i += len(word)
        else:
            result += text[i]
            i += 1
    return result
