def word_frequency(text):
    freq = {}  # hashmap

    text = text.lower()
    words = text.split()

    for word in words:
        # remove basic punctuation
        word = word.strip(".,!?;:'\"()[]{}")

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


# example
text = "AI is great. AI is powerful, and AI is the future!"
print(word_frequency(text))
