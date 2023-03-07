from gtts import gTTS
from playsound import playsound


language = 'en'
words = ['read', 'write', 'other', 'machine']
with open('words.txt') as file:
    correct_words = []
    num_correct = 0
    wrong_words = []
    num_wrong = 0
    for word in file:
        gTTS(text=word, lang=language, slow=False).save("word.mp3")
        playsound("word.mp3")
        ask = input('Write the word: ')
        if ask == word.strip():
            print("correct answer")
            correct_words.append(word.strip())
            num_correct += 1
        else:
            print("wrong answer")
            wrong_words.append(word.strip())
            num_wrong += 1

print(f'You have {num_correct} correct answered and {num_wrong} wrong answer ')
print(f'correct words: {correct_words}')
print(f'Wrong words: {wrong_words}')

