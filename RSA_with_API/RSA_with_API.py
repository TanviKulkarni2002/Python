import rsa 


with open('priv.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)


with open('pub.pem', mode='rb') as publicfile:
    keydata = publicfile.read()

pubkey = rsa.PublicKey.load_pkcs1(keydata)


msg=input("Enter text to encrypt").encode('utf8')
crypto = rsa.encrypt(msg, pubkey)
print(crypto)

msg = rsa.decrypt(crypto, privkey)

print(msg)

(bob_pub, bob_priv) = rsa.newkeys(512)

message = 'abcd'.encode('utf8')

crypto = rsa.encrypt(message, bob_pub)

message = rsa.decrypt(crypto, bob_priv)

print(message.decode('utf8'))