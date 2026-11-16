#problem 1
'''text="Aegis-flow"
for t in reversed(text):
    print(t,end="")

'''

## problem 2
'''text="Mahek Geete"
vowels="aeiou"

print(text)
for char in text:
    if char.lower() in vowels:
        print(char, end="")
        '''
text="Mahek Geete"
vowels="aeiou"
count=0
print(text)
for char in text:
    if char.lower() in vowels:
        count += 1
print("Vowel count:", count)
        
        