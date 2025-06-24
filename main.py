from stats import get_num_words, get_char_count, sort_characters
import sys

def get_book_text(book):
    """
    Extracts the text from a book object.
    
    Args:
        book (object): The book object containing text.
        
    Returns:
        str: The text of the book.
    """
    with open(book.path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text



def main():
    class Book:
        def __init__(self, path):
            self.path = path

    # book = Book('books/frankenstein.txt')
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = Book(book_path)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book.path}")
    print(f"----------- Word Count ----------")
    num_words = get_num_words(get_book_text(book))
    print(f'Found {num_words} total words')
    char_count = get_char_count(get_book_text(book))
    sorted_chars = sort_characters(char_count)
    print(f'----------- Character Count -----------')
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print(f'============= END ===============')


if __name__ == "__main__":
    main()
