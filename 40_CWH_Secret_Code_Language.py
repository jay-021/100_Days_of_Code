import random
# if you want to read question that is available at the end of the program scroll down for that

def random_char ():
    '''function generates a random three-character string by using the choices() function
    from the random module to select three random characters from the alphabet. 
    The join() method is then used to concatenate the characters into a single string.'''
    
    return "".join(random.choices([chr(i)for i in range(ord('a'),ord('z')+1)] ,k=3 ))

s = " Encoding and Decoding "
print(s.center(80,"~"))
print("Right now it only works with single word.")
code_or_decode = input("Enter c for encoding , Enter d for decoding : ")

match code_or_decode.lower():
    
    case "c" :
        code = input("Enter your keyword or string for coding: ")
        
        if len(code)<= 3 :
            a=0
            list_code = list(code)
            list_code.reverse()
            modified_code = "".join(list_code)
            print("encoded word = ",modified_code)
        else:
            list_code = list(code)
            temp = list_code.pop(0)
            list_code.append(temp)
            modified_code = "".join(list_code)
            word1 = random_char()
            word2 = random_char()
            final_code = word1 + modified_code + word2
            print("encoded word = ",final_code)
    case "d":
        decode = input("Enter your keyword or string for decoding: ")
        if len(decode)<= 3 :
            a=0
            list_decode = list(decode)
            list_decode.reverse()
            modified_decode = "".join(list_decode)
            print("decoded word = ",modified_decode)
        else:
            list_decode = list(decode)
            temp = list_decode.pop(-4)
            list_decode.pop(-3)
            list_decode.pop(-2)
            list_decode.pop(-1)
            list_decode.pop(2)
            list_decode.pop(1)
            list_decode.pop(0)
            list_decode.insert(0,temp)
            modified_decode = "".join(list_decode)
            print("decoded word = ",modified_decode)
print("Thank you for using this program")


# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode