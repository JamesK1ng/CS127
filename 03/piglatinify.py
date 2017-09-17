def topiglatin(word):
    first = word[0]
    if first in "aeiou":
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"
    
print(topiglatin("duck"))
print(topiglatin("chicken"))