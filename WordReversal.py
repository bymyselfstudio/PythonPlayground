def wordReversal(sentence):
   list = sentence.rsplit(' ')
   for i in range(len(list)-1, 0-1, -1):
        print(str(list[i]), end=" ")

def main():
    sentence="Dog bites man"
    wordReversal(sentence)

main()