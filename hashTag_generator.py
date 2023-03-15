def generate_hashtag(s):
    if len(s)>140 or len(s)==0:
        return False
    else:
       hash = '#'
       new_h = s.title().strip().replace(' ', '')
       return hash + new_h
    
text = 'A single letter is considered to be a word of length 1'
generate_hashtag(text)


# 2nd way

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

# 3d way

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False