def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
string = input("Enter String: ")
result = char_frequency(string)
for char, count in result.items():
    print(f"'{char}': {count}")
