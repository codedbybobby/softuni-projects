from collections import Counter
from itertools import count

# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:
    text = choice[::-1]

elif choice == 2:
    text = text.upper()

elif choice == 3:
    text = text.lower()

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    text = text.title()

elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    vowels_c = 0
    text.count('a''e''i''o''u')
    # 2nd way
    # for ch in text:
    #     if ch in ['a', 'e', 'i', 'o', 'u']:
    #         vowels_c +=1
    # print(f'{vowels_c} vowels are in the text')

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    text = text.join('')

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    for ch in text:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            ch = '*'
    print(f'All vowels with "*": {text}')

elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)
    text = text.join('')
    if text == text[::-1]:
        print(f'{text} is a palindrome')
    else:
        print(f'{text} is NOT a palindrome')

elif choice == 9:
    new_list = []
    text = text.split()
    for word in text:
        if word not in new_list:
            new_list.append(word)
            time = text.count(word)
            print(f'Word \'{word}\' is counted {time} times')
        else:
            continue
else:
    print("❌ Invalid choice! Please restart the program.")
