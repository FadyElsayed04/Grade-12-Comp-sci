character_counter = 0
def count_strings(s,ch):
    global character_counter
    if len(s) == 1:
        if ch == s[0]:
            character_counter+=1
            
        return s[0]

    else:
        count_strings(s[1:],ch)
        if ch == s[0]:
            character_counter += 1
        
        return character_counter

def print_strings(s):
    if len(s) == 1:
        return s[0]
    
    else:
        print (s[0])
        return print_strings(s[1:])


def print_reverse(s):
    if len(s) == 1:
        return s[0]
    
    else:
        print (s[-1])
        return print_reverse(s[:-1])

word_reverse = ""
def reverse_string(s):
    global word_reverse
    if len(s) == 0:
        return s
    
    else:
        reverse_string(s[1:])
        word_reverse+=s[0]
        print (word_reverse)
        
def main():
    print (count_strings("Word", "r"))
    print (print_strings("Word"))
    print (print_reverse("Word"))

if __name__ == '__main__':
    main()
