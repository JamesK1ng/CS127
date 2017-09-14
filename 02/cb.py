def string_times(str,n):
  result = (str * n)
  return result


def front_times(str, n):
    front = str[:3]
    result = front * n
    return result


def string_bits(str):
    bits = str[::2]
    return bits


def lone_sum(a, b, c):
   sum = 0
   if a != b and a != c:
      sum = sum + a
   if b != c and b != a:
      sum = sum + b
   if c != b and c != a:
      sum = sum + c
   return sum   

def string_splosion(str):
    result = ""
    for length in range(len(str)+1):
        result = result + str[0:length]
    return result 

def cigar_party(cigars, is_weekend):
    if cigars >= 40 and cigars <= 60:
        return True
    elif cigars >= 40 and is_weekend:
        return True
    else:
        return False
    
def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speed = speed -5
    if speed >= 81:
        return 2
    elif speed >= 61 and speed <=80:
        return 1

    return 0
        
print(string_times("Hello", 5))

print(front_times("Teach", 3))

print(string_bits("hype"))

print(lone_sum(15, 20, 5))

print(string_splosion("Tea"))

print(cigar_party(60, True))

print(caught_speeding(90, True))

