import os
import config

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('miracle.txt')
    for word in words:
        send_message(config.FRIEND1, word)

    # python3 main.py   use this to run the code. 