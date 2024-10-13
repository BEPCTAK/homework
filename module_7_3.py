import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Read the content of the file
                    content = file.read().lower()

                    # Remove punctuation
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))

                    # Split into words
                    words = content.split()

                    # Store in the dictionary
                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"File {file_name} not found.")
                all_words[file_name] = []  # If file is not found, return an empty list for that file

        return all_words

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1  # +1 for 1-based index

        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)

        return word_counts


# Example usage:
if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # All words from the files
    print(finder2.find('text'))  # Position of the first occurrence of 'text'
    print(finder2.count('text'))  # Count of 'text' in the files
