import random
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
words = text.split()
# Create Markov Chain model
markov_chain = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

# Choose random starting word
current_word = random.choice(words)
# Generate text
generated_text = current_word
for _ in range(100):
    if current_word in markov_chain:
        next_word = random.choice(markov_chain[current_word])
        generated_text += " " + next_word
        current_word = next_word
    else:
        break
print("\nGenerated Text:\n")
print(generated_text)