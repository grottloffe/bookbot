def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_char_count(book_content: str) -> dict[str, int]:
    """Counts the frequency of each character in the book content to analyze character usage."""
    chars_dict = {}
    for char in book_content.lower():
        if char != "\n":
            try:
                if char.isalpha():
                    chars_dict[char] += 1
            except KeyError:
                chars_dict[char] = 1
    return chars_dict

def sort_characters(chars_dict: dict[str, int]) -> list[dict[str, int]]:
    """Sorts characters by their frequency in descending order."""
    sorted_chars = [{"char": char, "num": count} for char, count in chars_dict.items()]
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars