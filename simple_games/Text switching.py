text = "Когда ты смотришь в бездну, бездна смотрит в тебя"
new_text = ""
for char in enumerate(text):
    if char[0] % 5 == 0:
        new_text += '*'
    else:
        new_text += char[1]
print(new_text)
