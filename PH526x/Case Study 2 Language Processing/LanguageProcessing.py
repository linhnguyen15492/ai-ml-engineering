import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


cwd = os.path.dirname(os.path.abspath(__file__))
book_dir = os.path.join(cwd, "Books")
text = "Complex Sentence Generator is a free content rewriter that can potentially rephrase, reword, paraphrase and/or rewrite sentences, paragraphs, articles, content, words and/or phrases into a more complex, unorthodox or convoluted alternative while delivering the same meaning. The vocabulary of this sentence paraphraser contains an abundance of rarely used words/phrases and can paraphrase sentences in a variety of ways that are chosen randomly. Aside from this web based software being used as a paraphrasing tool or a text spinner, it can also be used as a vocabulary improvement tool. The artificial intelligence of this paraphrase generator is so sophisticated that it is capable of understanding context. Use the dictionary or thesaurus to learn definitions for words or discover more synonyms."


def count_words(text: str) -> dict:
    text = text.lower()
    skips = [",", ".", ":", ";", "''", '""']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words_fast(text: str) -> Counter:
    text = text.lower()
    skips = [",", ".", ":", ";", "''", '""']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


# print(count_words(text) == count_words_fast(text))
# print(count_words(text) is count_words_fast(text))


def read_book(title_path: str) -> str:
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r", "")
    return text


def word_stats(word_counts: dict) -> tuple:
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))

title_num = 0
for language in os.listdir(book_dir):
    for author in os.listdir(os.path.join(book_dir, language)):
        for title in os.listdir(os.path.join(book_dir, language, author)):
            filename = os.path.join(book_dir, language, author, title)
            text = read_book(filename)
            (num_unique, counts) = word_stats(count_words(text))

            # row = pd.DataFrame(
            #     {
            #         "language": language,
            #         "author": author.capitalize(),
            #         "title": title.replace(".txt", ""),
            #         "length": len(text),
            #         "unique": num_unique,
            #     },
            #     index=[title_num],
            # )
            # stats = pd.concat([stats, row], ignore_index=True)

            stats.loc[title_num] = [
                language,
                author.capitalize(),
                title.replace(".txt", ""),
                len(text),
                num_unique,
            ]

            title_num += 1

print(stats.shape)
# print(stats.iloc[0:10, [0, 2, 4]].head())


plt.plot(stats["length"], stats["unique"], "o", markersize=2, alpha=0.5)

output_file = os.path.join(cwd, "plot.png")
plt.figure(figsize=(16, 9))
subset = stats[stats["language"] == "English"]
plt.loglog(subset["length"], subset["unique"], "o", label="English", color="crimson")
subset = stats[stats["language"] == "French"]
plt.loglog(subset["length"], subset["unique"], "o", label="French", color="forestgreen")
subset = stats[stats["language"] == "German"]
plt.loglog(subset["length"], subset["unique"], "o", label="German", color="orange")
subset = stats[stats["language"] == "Portuguese"]
plt.loglog(
    subset["length"], subset["unique"], "o", label="Portuguese", color="blueviolet"
)
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.title("Unique words in books by language")
plt.savefig(output_file)
# plt.show()
