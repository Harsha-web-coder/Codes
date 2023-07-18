def run_length_encoding(string):
    encoded_string = ''
    current_letter = string[0]
    current_count = 0
    
    for letter in string:
        if letter == current_letter:
            current_count += 1
            if current_count == 9:
                encoded_string += '9' + current_letter
                current_count = 0
        else:
            encoded_string += str(current_count) + current_letter
            current_letter = letter
            current_count = 1
    
    encoded_string += str(current_count) + current_letter
    return encoded_string
input_string = input()
encoded_string = run_length_encoding(input_string)
print(encoded_string)
