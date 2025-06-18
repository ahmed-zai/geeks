"""Challenge 2

Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

Examples


user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"


Notes

Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
"""

def remove_consecutive_duplicates(word):
    result = ""
    
    for i in range(len(word)):
        if i == 0 or word[i] != word[i - 1]:
            result += word[i]
    
    return result


user_word = input("Enter a word: ")


cleaned_word = remove_consecutive_duplicates(user_word)

print(f"Cleaned word: {cleaned_word}")


