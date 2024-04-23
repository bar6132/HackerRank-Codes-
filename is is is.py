if __name__ == '__main__':
    s = input()

    any_is_alnum = any(char.isalnum() for char in s)
    any_is_alpha = any(char.isalpha() for char in s)
    any_is_digit = any(char.isdigit() for char in s)
    any_is_lower = any(char.islower() for char in s)
    any_is_upper = any(char.isupper() for char in s)

    print(f"{any_is_alnum}\n{any_is_alpha}\n{any_is_digit}\n{any_is_lower}\n{any_is_upper}")
