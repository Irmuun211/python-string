# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    return len(text)
    
# Exercise 2
def remove_spaces(text):
    text1 = ""
    for i in range(len(text)):
        if text[i] != " ":
            text1 += text[i]
    return text1

# Exercise 3
def count_vowels(text):
    x=0
    for i in text:
        if i.lower() in "aeiou":
            x+=1
    return x

# Exercise 4
def replace_vowels(text):
    for i in text:
        if i.lower() in "aeiou":
            text = text.replace(i, '*')
    return text

# Exercise 5
def count_words(text):
    words = text.split()
    return len(words)

# Exercise 6
def find_longest_word(text):
    words= text.split()
    m=0
    if(len(words)==0):
        return ""
    else:
        for i in range(len(words)):
            if(m<len(words[i])):
                d= i
                m= len(words[i])
        return words[d]
