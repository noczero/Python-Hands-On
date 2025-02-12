"""
https://www.codewars.com/kata/55c45be3b2079eccff00010f/python

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""


"""

def your_order_please(text):
    # Step 1 : early exit for empty string
    if text == "":
        return ""

    # Step 2 : split string by delimiter
    words = text.split()

    # Step 3 : generate dictionary of word as key and number as value
    h_number_word = {}
    for word in words:
        for i in range(1, len(words) + 1):
            if str(i) in word:
                h_number_word[word] = i

    # Step 4 : sort the dict
    sorted_text = ""
    for word, number in sorted(h_number_word.items(), key=lambda item: item[1]):
        sorted_text += word + ' '

    return sorted_text.strip()


def extract_number(word):
    for char in word:
        if char.isdigit():
            return int(char)

def your_order_please2(text):
    # Step 1: early exit for empty string
    if not text:
        return ""

    # Step 2: split text into array of word
    words = text.split()

    # Step 3: Sort the list of words using the extracted number as the key
    sorted_words = sorted(words, key=extract_number)

    # Join the sorted words back into a single string
    return " ".join(sorted_words)

print(your_order_please("is2 Thi1s T4est 3a"))
print(your_order_please("4of Fo1r pe6ople g3ood th5e the2"))
print(your_order_please(""))


print(your_order_please2("is2 Thi1s T4est 3a"))
print(your_order_please2("4of Fo1r pe6ople g3ood th5e the2"))
print(your_order_please2(""))