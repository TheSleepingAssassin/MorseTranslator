from Dictionary import *


# def encrypt(message):
#     cipher = ''
#     for letter in message:
#         if letter != ' ':
#             cipher += dictionary[letter] + ' '
#         else:
#             cipher += ' '
#     return cipher


# def decrypt(message):
#     message += ' '

#     decipher = ''
#     citext = ''
#     for letter in message:
#         if letter != ' ':
#             i = 0
#             citext += letter
#         else:
#             i += 1
#             if i == 2:
#                 decipher += ' '
#             else:
#                 decipher += list(
#                     dictionary.keys()
#                 )[
#                     list(dictionary.values()).index(citext)
#                 ]
#                 citext = ''
#     return decipher

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += dictionary[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english


def decrypt(message):

    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter

        else:
            i += 1

            if i == 2:

                decipher += ' '
            else:

                decipher += list(dictionary.keys())[list(dictionary
                                                         .values()).index(citext)]
                citext = ''

    return decipher
