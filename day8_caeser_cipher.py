alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message
# .

def encrypt(text,shift):
    encrypt_message_list=[]
    for letter in text:
        index = alphabet.index(letter)
        new_index = (index+shift)%len(alphabet)
        encrypt_message_list.append(alphabet[new_index])
    encrypt_message = "".join(encrypt_message_list)
    print(f"Here is the encoded result {encrypt_message}")


#encrypt(text,shift)

def decrypt(text,shift):
    decrypt_message_list=[]
    for letter in text:
        index = alphabet.index(letter)
        new_index = (index-shift)%len(alphabet)
        decrypt_message_list.append(alphabet[new_index])
    encrypt_message = "".join(decrypt_message_list)
    print(f"Here is the decoded result {encrypt_message}")

#decrypt(text,shift)

def caesar(text,shift,direction):
    encrypt_message_list=[]
    for letter in text:
        if direction =="decode":
            shift *= -1
        index = alphabet.index(letter)
        new_index = (index+shift)%len(alphabet)
        encrypt_message_list.append(alphabet[new_index])
    encrypt_message = "".join(encrypt_message_list)
    print(f"Here is the encoded result {encrypt_message}")