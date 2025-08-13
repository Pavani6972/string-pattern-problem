def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():  # only consider letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

text = input("Enter String: ")
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
