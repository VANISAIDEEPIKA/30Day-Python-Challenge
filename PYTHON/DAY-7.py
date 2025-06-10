import string
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Read the file
file_path = "sample_text.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Step 2: Clean and process the text
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

# Step 3: Count word frequencies
word_counts = Counter(words)

# Step 4: Display word frequencies
print("Word Frequencies:\n")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Step 5: Save to CSV
with open("word_frequencies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Word", "Frequency"])
    writer.writerows(word_counts.items())

print("\n✅ Word frequencies saved to 'word_frequencies.csv'.")

# Step 6: Plot bar chart
top_words = word_counts.most_common(10)  # Top 10 words
words, counts = zip(*top_words)

plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='skyblue')
plt.title("Top 10 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("word_frequencies_chart.png")
plt.show()

print("📊 Chart saved as 'word_frequencies_chart.png'.")
