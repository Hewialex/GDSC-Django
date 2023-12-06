# Task 1: Print numbers from 0 to 99
for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")

# Task 2: Print a pattern based on user input
char = input("Enter a character: ")
for i in range(1, 6):
    print(char * i if i <= 3 else char * (5 - i))

# Task 3: Check if a word is a palindrome
word = input("Enter a word: ")
is_palindrome = word == word[::-1]
print(f"{word} is a palindrome." if is_palindrome else f"{word} is not a palindrome.")

# Task 4: Find the sum of even numbers from 1 to 50 with replacements
total_sum = 0
replace_count = 0

for num in range(2, 51, 2):
    total_sum += num
    if num % 3 == 0:
        print("Three", end=", ")
        replace_count += 1
    elif num % 5 == 0:
        print("Five", end=", ")
        replace_count += 1
    else:
        print(num, end=", ")

print("\nTotal Sum:", total_sum)
print("Count of 'Three' or 'Five':", replace_count)
