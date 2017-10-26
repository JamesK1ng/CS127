def  score(w):
    #I'm not sure how to do this the smart way... I hope this unorthodox method works
    value1 = ['A','E','I','O','U','L','N','R','S','T']
    value2 = ['D','G']
    value3 = ['B','C','M','P']
    value4 = ['F','H','V','W','Y']
    value5 = ['K']
    value8 = ['J','X']
    value10 = ['Q','Z']
    score = 0
    
    for i in w.upper():
        if i in value1:
            score = score + 1
        if i in value2:
            score = score + 2
        if i in value3:
            score = score + 3
        if i in value4:
            score = score + 4
        if i in value5:
            score = score + 5
        if i in value8:
            score = score + 8
        if i in value10:
            score = score + 10
    return score
        
  
print(score('hello'))

print(score('I am Boss'))