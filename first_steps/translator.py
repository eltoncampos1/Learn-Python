# random language
# vowels -> g

# dog -> dgg
# cat -> cgt
vowels = "aeiou"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "gA"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))