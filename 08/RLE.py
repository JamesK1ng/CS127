def encode(s):
    encoded = []
   
    for i in s:
        if i not in encoded:   
            encoded.append(i)
            if s.count(i) > 1:
                
                encoded.append(s.count(i))
    print(encoded)

encode('sdklfnhlsdfn')

encode('aaabcccc ')


#I was unsure if the spaces should count as values as well, so I left it 