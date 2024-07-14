a=input("Enter a string: ")
a=a.lower()
vowel = {'a', 'e', 'i', 'o', 'u'}
count = 0
for i in a:
    if i in vowel:
        count +=1
print("Number of Vowels: ", count)