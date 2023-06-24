#Substitution Cipher Encryption
def caesar_cipher_encrypt():
    
    word = input("Enter the word to be encrypted into substitution cipher: ")
    word = word.replace(" ","") #Removes white spaces, if any
    word = word.upper() #Converts all lowercase letters to uppercase, if any

    word1 = list(word.strip(" ")) #Converts string to list
    
    s1 = 2 #Shift for odd terms
    s2 = 3 #Shift for even terms
    
    word2 = []
    for j in (0,len(word1)):
        for i in word1:
            if(j%2==0):
                x =  (ord(i) - 65)%26 + s2  #Takes ASCII values to form the new values
                word2.append(x)
            elif(j%2!=0):
                x =  (ord(i) - 65)%26 + s1  #Takes ASCII values to form the new values
                word2.append(x)  
    
    encrypt = []
    for j in word2:
        j = j + 65
        y = chr(j) #Converts the new values to the corresponding alphabets
        encrypt.append(y)
    
    encrypted_word = ''.join(encrypt) #Converts the list to string of the encrypted word
    print("Encrpted word in Caesar Cipher is:" ,encrypted_word)

#Substitution Cipher Decryption
def caesar_cipher_decrypt():
    
    word = input("Enter the word to be decrypted from Substitution cipher: ")
    word = word.replace(" ","") #Removes white spaces, if any
    word = word.upper() #Converts all lowercase letters to uppercase, if any

    word1 = list(word.strip(" ")) #Converts string to list
    
    s1 = 2 #Shift for odd terms
    s2 = 3 #Shift for even terms
    
    word2 = []
    for j in (0,len(word1)):
        for i in word1:
            if(j%2==0):
                x =  (ord(i) + 65) - s2  #Takes ASCII values to form the new values
                word2.append(x)
            elif(j%2!=0):
                x =  (ord(i) + 65) - s1  #Takes ASCII values to form the new values
                word2.append(x)    
    decrypt = []
    for j in word2:
        j = j - 65
        y = chr(j) #Converts the new values to the corresponding alphabets
        decrypt.append(y)
    
    decrypted_word = ''.join(decrypt) #Converts the list to string of the encrypted word
    print("Decrpted word from Substitution Cipher is:" ,decrypted_word)

caesar_cipher_encrypt()
caesar_cipher_decrypt()