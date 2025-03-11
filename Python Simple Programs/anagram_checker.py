# Description: Write a function that checks whether two given strings are anagrams of each other.
# anagram_checker.py

def are_anagrams(word1, word2):
    """
    Check if two words are anagrams.
    
    Parameters:
    word1 (str): The first word.
    word2 (str): The second word.
    
    Returns:
    bool: True if the words are anagrams, False otherwise.
    """

    # Convert both words to lowercase to make the check case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Sort the characters of both words and compare
    return sorted(word1) == sorted(word2)

def are_anagrams_manual(word1, word2):
    """
    Manually check if two words are anagrams without using sorted().
    
    Parameters:
    word1 (str): The first word.
    word2 (str): The second word.
    
    Returns:
    bool: True if the words are anagrams, False otherwise.
    """

    # Convert both words to lowercase to make the check case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()
    
    # If lengths are different, they cannot be anagrams
    if len(word1) != len(word2):
        return False
    
    # Create dictionaries to count the frequency of each character
    char_count1 = {}
    char_count2 = {}

    #The for loops count the frequency of each character in both words.
    #The dictionaries char_count1 and char_count2 store these frequencies.
    
    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare the dictionaries to determine if the words are anagrams.
    return char_count1 == char_count2

def get_user_input():
    """
    Get words from the user to check for anagrams.
    
    Returns:
    tuple: A tuple containing two words entered by the user.
    """
    word1 = input("Enter the first word: ").strip()
    word2 = input("Enter the second word: ").strip()
    return word1, word2

def main():
    """
    Main function to test the are_anagrams function with user input.
    """
    # Get words from the user
    word1, word2 = get_user_input()
    
    # Check if the words are anagrams using sorted method
    if are_anagrams(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams (using sorted method).')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams (using sorted method).')
    
    # Check if the words are anagrams using manual method
    if are_anagrams_manual(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams (using manual method).')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams (using manual method).')

if __name__ == "__main__":
    main()