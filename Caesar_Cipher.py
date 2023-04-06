
def caesar_cipher():
    
    word = input("Enter the word to be encrypted into caesar cipher: ")
    word = word.replace(" ","") #Removes white spaces, if any
    word = word.upper() #Converts all lowercase letters to uppercase, if any

    word1 = list(word.strip(" ")) #Converts string to list
    
    shift = int(input("Enter the value of the shift: "))
    
    word2 = []
    for i in word1:
        x =  (ord(i) - 65)%26 + shift  #Takes ASCII values to form the new values
        word2.append(x)
    
    encrypt = []
    for j in word2:
        j = j + 65
        y = chr(j) #Converts the new values to the corresponding alphabets
        encrypt.append(y)
    
    encrypted_word = ''.join(encrypt) #Converts the list to string of the encrypted word
    print("Encrpted word in Caesar Cipher is:" ,encrypted_word)
    
    print("\n\n")
    
    word3 = input("Enter the word to be decrypted from caesar cipher: ")
    word3 = word.replace(" ","") #Removes white spaces, if any
    word3 = word.upper() #Converts all lowercase letters to uppercase, if any
    print("Word decrypted from Caesar Cipher: ",word3)
caesar_cipher()