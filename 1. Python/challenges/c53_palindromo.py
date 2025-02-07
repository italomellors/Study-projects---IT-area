# Create a program that reads a phrase
# and says whether it is a palindrome, ignoring spaces
phrase = str(input("Palindrome: \n")).upper()
phrase = "".join(phrase.split(" "))
print(f'The word {phrase} reversed is {phrase[::-1]} and ',
end="")
if phrase == phrase[::-1]:
    print("is a palindrome.")
else:
    print("is not a palindrome.")