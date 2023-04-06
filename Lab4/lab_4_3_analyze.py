import csv
import sys
from collections import Counter

path = input("Podaj ścieżkę do pliku tekstowego: ")

with open(path, "r") as file:
    content = file.read()

num_chars = len(content)
num_words = len(content.split())
num_lines = content.count("\n") + 1  # add last line

char_counts = Counter(content)
most_common_char = char_counts.most_common(1)[0][0]

word_counts = Counter(content.split())
most_common_word = word_counts.most_common(1)[0][0]

writer = csv.writer(sys.stdout, delimiter=",")
writer.writerow(["ścieżka do pliku", "liczba znaków", "liczba słów", "liczba wierszy", "znak najczęściej występujący",
                 "słowo najczęściej występujące"])
writer.writerow([path, num_chars, num_words, num_lines, most_common_char, most_common_word])
