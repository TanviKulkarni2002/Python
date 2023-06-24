#Transposition Cipher Encryption (Single Columnar)
def transposition_cipher_encrypt():
    
    word = input("Enter the word to be encrypted into Transposition cipher: ")
    word = word.replace(" ","") #Removes white spaces, if any
    word = word.upper() #Converts all lowercase letters to uppercase, if any

    word1 = list(word.strip(" ")) #Converts string to list
    
    d = int(input("Enter the value of the depth: "))
    arr1 = []
    arr2 = []
    for i in range (0,len(word1)):
        if(i%d==0):
            arr1.append(word1[i])
    
    for j in range (0,len(word1)):
        if(j%d!=0):
            arr2.append(word1[j]) 
    
    arr3 = arr1 + arr2
    encrypted_word = ''.join(arr3)
    print("Word Encrypted into Transposition Cipher: ",encrypted_word)
transposition_cipher_encrypt() 