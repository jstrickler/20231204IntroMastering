word_count = 0
long_words = []

MINIMUM_LENGTH = 20
MAXIMUM_LENGTH = 2

with open("DATA/words.txt") as words_in:
    with open("long_words.txt", "w") as long_words_out:
        with open("short_words.txt", "w") as short_words_out:
            for raw_word in words_in:
                word = raw_word.rstrip()
                if len(word) >= MINIMUM_LENGTH:
                    long_words.append(word)
                    long_words_out.write(raw_word)  # need \n
                    word_count += 1
                if len(word) <= MAXIMUM_LENGTH:
                    short_words_out.write(raw_word)

print(f"There were {word_count} words of length {MINIMUM_LENGTH} or more")

for word in sorted(long_words):
    print(word)
