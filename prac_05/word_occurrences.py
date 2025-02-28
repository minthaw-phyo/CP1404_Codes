"""
Word Occurrences
Estimate: 15 minutes
Actual:   10 minutes
"""

text = input("Text: ").strip()
words_from_text = text.split()
words = {}

if text:
    for word in words_from_text:
        words[word] = words.get(word, 0) + 1

sorted_words = dict(sorted(words.items()))
word_length=len(max(words.keys()))

for word, count in sorted_words.items():
    print(f"{word:<{word_length}} : {count}")