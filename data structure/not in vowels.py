text = ['h','e','1','1','o']
print(text)
vowels = "aeiou"
newText = [x.upper( ) for x in text if x not in vowels]
print(newText)
