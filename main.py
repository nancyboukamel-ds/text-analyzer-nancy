import re
from collections import Counter

def analyze_text(text):
    # 1. SENTENCE COUNT
    # Split on:
    # - Punctuation followed by a space and a Capital Letter (handles 'Or is it? AI...')
    # - Or one or more newlines (handles 'Abdo Kamar\n' and list items)
    # This prevents splitting on 3.14 or example.com
    sentence_delimiters = r'(?<=[.!?]) +(?=[A-Z])|\n+'
    sentences = re.split(sentence_delimiters, text.strip())
    # Filter out empty strings and strip whitespace
    clean_sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(clean_sentences)

    # 2. WORD COUNT & TOP 10
    # This pattern captures words, numbers like 3.14, and hyphenated words
    word_pattern = r'''(?x)
    (?:https?://\S+)                    # URLs
    | (?:[\w.+-]+@[\w-]+\.[\w.-]+)      # Emails
    | (?:\d+\.\d+|1e-\d+)               # Decimals and Scientific Notation (3.14, 1e-3)
    | (?:[\w\d]+(?:-[\w\d]+)+)          # Hyphenated words (end-to-end, INC-2026-00042)
    | (?:[\w\d]+(?:'[\w\d]+)+)          # Contractions (don't, it's)
    | (?:\b\w+\b)                       # Standard words
    '''
    words = re.findall(word_pattern, text.lower())

    top_10 = Counter(words).most_common(10)

    return {
        'word_count': len(words),
        'sentence_count': sentence_count,
        'top_10': top_10,
        'sentences': clean_sentences  # Added so you can verify the list
    }

if __name__ == "__main__":
    try:
        with open("sample_text.txt", "r") as f:
            content = f.read()
        
        stats = analyze_text(content)
        
        print("--- Text Analysis Results ---")
        print(f"Total Words: {stats['word_count']}")
        print(f"Total Sentences: {stats['sentence_count']}")
        print("\nTop 10 Most Frequent Words:")
        for word, count in stats['top_10']:
            print(f"- {word}: {count}")
            
    except FileNotFoundError:
        print("Error: sample_text.txt not found.")