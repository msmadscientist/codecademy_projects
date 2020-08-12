# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:06:34 2020

@author: Kimberly Taylor

Description: Cypher Project from Codecademy
"""

import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

message2 = "is this message correctly coded?"

message3 = "yi jxyi cuiiqwu sehhusjbo setut?"

message4 = "ebiil"

message5 = "hello"

message6 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

vigenere1 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"

def decode_caesar_cypher (message, offset):
    new_message = ""
    for letter in message:
        index = alphabet.find(letter)
        if (index != -1):
            if index + offset > 25:
                new_message += alphabet[(index + offset - 1) % 25]
            else:
                new_message = new_message + alphabet[index + offset]
        else:
            new_message = new_message + letter
    
    return new_message

def code_caesar_cypher (message, offset):
    new_message = ""
    for letter in message:
        index = alphabet.find(letter)       
        if (index != -1):
            new_message += alphabet[index - offset]
        else:
            new_message = new_message + letter
    
    return new_message

def generate_keystream (word, n):
    keystream = ""
    for i in range(n):
        keystream += word
        
    return keystream

def decode_vigenere (phrase, codeword):
    solution = ""
    
    n = math.ceil(len(phrase)/len(codeword))
    keystream = generate_keystream(codeword, n)
    
    i = 0   #counter for phrase
    j = 0   #counter for keystream
    
    while i < len(phrase):
        if phrase[i] in alphabet:
            letter_index = alphabet.find(phrase[i])
            keystream_index = alphabet.find(keystream[j])
            index_difference = letter_index - keystream_index
            solution += alphabet[index_difference]
            i += 1
            j += 1

        else:
            solution += phrase[i]
            i += 1
    
    return solution

def code_vigenere (phrase, codeword):
    new_message = ""
    
    n = math.ceil(len(phrase)/len(codeword))
    keystream = generate_keystream(codeword, n)
    
    i = 0   #counter for phrase
    j = 0   #counter for keystream
    
    while i < len(phrase):
        if phrase[i] in alphabet:
            letter_index = alphabet.find(phrase[i])
            keystream_index = alphabet.find(keystream[j])
            index_difference = letter_index + keystream_index
            if index_difference > 25:
                new_message += alphabet[(letter_index + keystream_index - 1) % 25]
            else:
                new_message += alphabet[index_difference]
            i += 1
            j += 1

        else:
            new_message += phrase[i]
            i += 1
    
    return new_message

print(decode_caesar_cypher(message, 10))
print(code_caesar_cypher(message2,10))
print(decode_caesar_cypher(message3,10))
print(decode_caesar_cypher(message4,3))
print(code_caesar_cypher(message5,3))
print(decode_caesar_cypher(message6,14))
    
print(decode_vigenere(vigenere1, "friends"))
print(code_vigenere(alphabet,"punk"))
print(decode_vigenere("pvpntztrxdxvbhbzflfdjpjhnt","punk"))