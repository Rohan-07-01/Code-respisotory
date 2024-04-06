txt =input('Enter the word:')

los =len(txt)
print("The length of the string is", los);

Word =txt.upper()
print(Word);

i=0
VCount=0
CCount=0

if (Word>='A' and Word<='Z'):
    for i in range(0,los):
        if (Word[i] in ('A','E','I','O','U')):
            VCount=VCount+1
        else:
            CCount=CCount+1

    print("The number of vowels are", VCount);
    print("The number of consonants are", CCount);
else:
    print("Please enter a valid string");
    
