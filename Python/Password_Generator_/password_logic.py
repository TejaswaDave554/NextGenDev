import random

def generate_password(chars, words, length):
    password = ''
    word_index = 0

    try:
        while len(password) < length:
            if word_index < len(words):
                word = words[word_index]
                word_index += 1

                if random.choice([True, False]) and len(password) + len(word) <= length:
                    password += word
                else:
                    remaining_length = length - len(password)
                    num_random_chars = random.randint(1, remaining_length - len(word))
                    random_chars = ''.join(random.choice(chars) for _ in range(num_random_chars))
                    if random.choice([True, False]):
                        password += random_chars + word
                    else:
                        password += word + random_chars
            else:
                remaining_length = length - len(password)
                random_chars = ''.join(random.choice(chars) for _ in range(remaining_length))
                password += random_chars

        return password[:length]
    except IndexError:
        return "Error: Unable to generate password. Check your input."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
