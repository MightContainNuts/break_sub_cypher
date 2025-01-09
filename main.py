import string
import re


def open_file()->str:
    with open ("data_file.txt", "r") as read_handle:
        file_contents = read_handle.read()
    return file_contents


def main():
    encrypted_data = open_file()
    encrypted_word_list = create_list_of_words_from_data(encrypted_data)
    single_letter_freq_dict = create_letter_freq_dict(encrypted_word_list)
    #decrypted_text = substitute_letters_in_encrypted_text(encrypted_word_list)
    bigram_freq = dict_of_xgrams(get_bigrams(encrypted_word_list))
    trigram_freq = dict_of_xgrams(get_trigrams(encrypted_word_list))
    print(bigram_freq)
    print(trigram_freq)
    decrypted_text = substitute_letters_in_encrypted_text(encrypted_word_list)


def create_letter_freq_dict(encrypted_word_list:[list[str]])->dict[str,int] :
    single_letter_freq: dict = {}
    for word in encrypted_word_list:
        for letter in word:
            if letter not in string.ascii_uppercase and letter not in string.ascii_lowercase:
                pass
            else:
                letter = letter.lower()
                if single_letter_freq.get(letter, 0) == 0:
                    single_letter_freq[letter] = 1
                else:
                    single_letter_freq[letter] +=1
    sorted_slf_dict = sorted(single_letter_freq.items(), key = lambda x: x[1], reverse = True)
    print("Single letter frequency\n")
    for idx, (key, value) in enumerate(sorted_slf_dict, start=1):
        print(f"{idx:02} {key} : {value}")
    return sorted_slf_dict

def get_key_from_value(encrypted_letter)->str:
    char_freq_eng ={
        "E":"i", #correct
        "T":"k", #correct
        "A":"s",#correct
        "O":"u",#correct
        "N":"l",#correct
        "I": "e",#correct
        "H":"f", #correct
        "S":"j",
        "R":"r",
        "L":"v",
        "D":"f",
        "U":"m",
        "C":"f",
        "M":"w",
        "W":"n",
        "Y":"z",
        "F":"h",
        "G":"x",
        "P":"q",
        "B":"b",
        "V":"m",
        "K":"t",
        "J":"y",
        "X":"a",
        "Q":"p",
        "Z":"g",
    }
    for key,value in char_freq_eng.items():
        if value == encrypted_letter:
            return key
    return ""

def substitute_letters_in_encrypted_text(encrypted_word_list):
    decrypted_word_list =[]
    for word in encrypted_word_list:
        decrypted_word =""
        for letter in word:
            decrypted_letter = get_key_from_value(letter)
            decrypted_word +=decrypted_letter
        decrypted_word_list.append(decrypted_word)
    print(decrypted_word_list)
    return decrypted_word_list

def create_list_of_words_from_data(data)-> list[str]:
    pattern = r"[^a-zA-Z0-9\s]"

    cleaned_words = re.sub(pattern, "", data)
    list_of_words = [word for word in cleaned_words.lower().split()]

    print(list_of_words)
    print(cleaned_words)
    print(f"Number of words: {len(cleaned_words)}")
    return list_of_words

def get_bigrams(encrypted_word_list):
    list_of_bigrams =[]
    for word in encrypted_word_list:
        word.strip()
        word = word.lower()
        if len(word) == 3:
            list_of_bigrams.append(word)
    return list_of_bigrams


def dict_of_xgrams(list_of_xgrams):
    dict_xgrams ={}
    for word in list_of_xgrams:
        if dict_xgrams.get(word,0) == 0:
            dict_xgrams[word] = 1
        else:
            dict_xgrams[word] +=1
    sorted_dict = sorted(dict_xgrams.items(), key = lambda x: x[1], reverse = True)
    return sorted_dict

def get_trigrams(encrypted_word_list):
    list_of_trigrams =[]
    for word in encrypted_word_list:
        if len(word) == 2:
            list_of_trigrams.append(word)
    return list_of_trigrams


if __name__ == '__main__':
    main()
