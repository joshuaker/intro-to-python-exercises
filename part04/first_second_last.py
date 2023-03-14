# Write your solution here
def first_word(sentence):
    index = sentence.find(' ')
    return sentence[0:index]

def second_word(sentence):
    sentence_save = sentence
    index = sentence.find(' ')
    sentence = sentence[index+1:]
    index2 = sentence.find(' ')
    # if there is nothing to find, index2 returns -1
    if index2 == -1:
        return sentence_save[index+1:]
    else:
        return sentence_save[index+1:index+1 + index2]
    #index+1 to skip the space; index+1 + index2 for the complete sentence index

def last_word(sentence):
    index = sentence.rfind(' ')
    return sentence[index+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))