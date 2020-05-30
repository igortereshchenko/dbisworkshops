from cryptography.fernet import Fernet

def decrypt(key):
    f = Fernet(key)
    with open("encrypted_credentials.txt", "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_data = decrypted_data.decode()

    return decrypted_data.split('\r\n')

# Saved here for now
key = b'QLBkwuk3f8QDr1QTmMv4luQW9j71S6JjK2z-nIX6kP4='

credentials = decrypt(key)

Name = credentials[0]
Pass = credentials[1]
Path = credentials[2]
