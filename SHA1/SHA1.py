import hashlib
with open('SHA1_data.txt') as f:
    lines = f.readlines()
f = ''.join(lines)
result = hashlib.sha1(f.encode())
print("Hashing value: ")
print(result.hexdigest())