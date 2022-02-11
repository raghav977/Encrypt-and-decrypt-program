
def encrypt(plain_text, shift_number):     #hello  #5
    encrypt_text=""
    for letter in plain_text:             #letter = 'h'
        if letter in alphabet:
            position = alphabet.index(letter)  #position = alphabet.index('h') position = 7
            new_position = position + shift_number #new_position = 7 + 5 = 12
            encrypt_text+=alphabet[new_position]
        else:
            encrypt_text+=letter
    print(encrypt_text)

def decrypt(text, number):
    decrypt_text = ""
    for let in text:
        if let in alphabet:
            position = alphabet.index(let)
            new_position = position - number
    
        
            decrypt_text += alphabet[new_position]
        else:
            decrypt_text+=let

    print(decrypt_text)



alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
should_contiue = True
while should_contiue:
    direction= input("what do you want to do? encrypt or decrypt, type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text = input("enter the message\n").lower()
    shift = int(input("enter the shift number\n"))%26
    a=0
    # encrypt_text =""
    # if text == "encrypt":
    if direction =="encode":
        encrypt(plain_text =text, shift_number= shift)  
    if direction =="decode":
        decrypt(text = text, number = shift)
    want = input("do you want to play again?, type 'yes' for continue and 'no' for exit \n")
    if want=="no":
        should_contiue= False
        print("Goodbye")



            

