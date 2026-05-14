import markovify

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

model = markovify.Text(text, state_size=2)

for i in range(5):
    sentence = model.make_sentence(tries=100)

    if sentence:
        print(sentence)