# This sequence will handle any brute force attempt to breach security.
import time 
def sequence():
    print("Hi i'm Patrick Ofili. \nWelcome to the Terragon Group Caesar Cipher Tool!")
    s = input('Enter a string of text to encrypt \n: ')
    alp = 'abcdefghijklmnopqrstuvwxyz    '
    cnt =0
    for l in s:
        if l not in alp:
            cnt +=1
    if len(s) < 1 or str(s) != s or cnt > 0:
        try_again = int(input('Please enter a valid text of strings without numbers or special characters. Do you want to try again? \n (1)Yes  \n (2)No: \n '))
        if try_again == 1:
            s = input('Enter your text of strings \n: ')
            if s != "" and cnt == 0:
                caesarCipher(s)
            else:
                print("Multiple wrong attempts not permitted for security reasons. \nKindly run the program again. Exiting..."); time.sleep(5)
        elif try_again == 2:
            print('Thank you for encrypting with Terragon Group, Have a lovely day'); time.sleep(3)
    else:
        caesarCipher(s)

# The main Algorithm
# I set a hidden key in the function called num that shifts the letters of the text by a certain step.
def caesarCipher(s):
    alp = 'abcdefghijklmnopqrstuvwxyz    '  ; num = 3;  low_s= s.lower();  new_string = "" ;   num = num % 26
    cnt =0
    for i in range(0,len(low_s)):
        current_letter = low_s[i]
        # Just in case a user inputs an empty string.
        if current_letter == " ":
            new_string += current_letter
            continue   
        new_index = alp.index(current_letter)
        index_jump = new_index + num          
        if index_jump > 25:
            index_jump = index_jump % 26   
        if index_jump<0 :
            index_jump = index_jump + 26
        if s[i].isupper() == True:
            new_letter = alp[index_jump]
            new_string += new_letter.upper() 
        else:
            new_letter = alp[index_jump]
            new_string += new_letter
    print('Successfully Encrypted as: '+ new_string) ; time.sleep(1)
    again = int(input ('Do you want to encrypt some more?  \n (1) Yes \n (2) No \n : '))
    if again == 1:
        s= input('Enter your text of strings \n: ')
        for l in s:
            if l not in alp:
                cnt +=1
        if s != "" and cnt == 0:
            caesarCipher(s)
        else:
            print('Multiple wrong trials not permitted for security purpose. \nKindly run the program again, Exiting...') ; time.sleep(5)
    elif again == 2:
        print('Thank you for encrypting with Terragon Group, Have a lovely day') ; time.sleep(2)
        
   
# Calling the function to start the Caesar Cipher sequence
print(sequence())




