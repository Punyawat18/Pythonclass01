
def main():
    text = input("text:")
    letter = letters(text)
    word = words(text)
    sentence = sentences(text)
    L = (letter * 100) / word
    S = (sentence * 100) / word
    Grade = round((0.0588 * L) - (0.296 * S) - 15.8)
    if Grade >= 16:
        print("Grade 16+")
    elif Grade < 1:
        print("Before Grade 1")
    else:
        print("Grade ", Grade)



def letters(text):
    length = len(text)
    letter = 0
    for i in range(length):
        if text[i].isalpha() == True:
            letter = letter + 1
    return letter


def words(text):
    length = len(text)
    word = 1
    for i in range(length):
        if text[i].isspace() == True:
            word = word + 1
    return word


def sentences(text):
    length = len(text)
    sentence = 0
    for i in range(length):
        if text[i] == ('.'):
            sentence = sentence + 1
        elif text[i] == ('?'):
            sentence = sentence + 1
        elif text[i] == ('!'):
            sentence = sentence + 1
    return sentence


main()