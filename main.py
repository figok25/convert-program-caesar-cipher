from tkinter import *

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    window = Tk()
    window.title("Convert Program: Caesar Cipher")

    Label(window, text="Enter Text:").grid(row=0, column=0)
    input_text = Entry(window)
    input_text.grid(row=0, column=1)
    Label(window, text="Enter Shift Value:").grid(row=1, column=0)
    input_shift = Entry(window)
    input_shift.grid(row=1, column=1)

    Label(window, text="Encrypted Text:").grid(row=2, column=0)
    output_encrypted = Entry(window)
    output_encrypted.grid(row=2, column=1)
    Label(window, text="Decrypted Text:").grid(row=3, column=0)
    output_decrypted = Entry(window)
    output_decrypted.grid(row=3, column=1)
    text = Label(text="Dev Figo Kurniawan")
    text.place(x=0,y=120)

    def encrypt_button():
        text = input_text.get()
        shift = int(input_shift.get())
        encrypted_text = encrypt(text, shift)
        output_encrypted.delete(0, END)
        output_encrypted.insert(0, encrypted_text)

    def decrypt_button():
        text = input_text.get()
        shift = int(input_shift.get())
        decrypted_text = decrypt(text, shift)
        output_decrypted.delete(0, END)
        output_decrypted.insert(0, decrypted_text)

    Button(window, text="Encrypt", command=encrypt_button).grid(row=4, column=0)
    Button(window, text="Decrypt", command=decrypt_button).grid(row=4, column=1)

    window.mainloop()

if __name__ == '__main__':
    main()