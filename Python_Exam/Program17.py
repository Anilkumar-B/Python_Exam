"""17. Word Counter
- Create a program to count the occurrences of each word in a sentence provided by the
user."""


def count_each_occurences_of_word(s):
    words=s.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
s=input('Enter the sentence to check word count:')
print(count_each_occurences_of_word(s))