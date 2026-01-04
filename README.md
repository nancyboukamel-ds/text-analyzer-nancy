# text-analyzer-nancy
# Python Text Analyzer

A robust Python script designed to analyze text strings and provide detailed statistics. This project was developed as an onboarding task for the AI/LLMs Mentorship, focusing on advanced tokenization and sentence segmentation.

## Features
- **Advanced Tokenization**: Handles complex tokens including:
  - URLs (https://...)
  - Emails (hello@example.com)
  - Scientific notation (1e-3) and decimals (3.14)
  - Hyphenated words (end-to-end) and Ticket IDs (INC-2026-00042)
  - Contractions (don't, it's)
- **Smart Sentence Splitting**: Identifies sentence boundaries using punctuation and newlines while ignoring false positives like decimal points.
- **Frequency Analysis**: Extracts the Top 10 most frequent words (case-insensitive).

## How to Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/nancyboukamel-ds/text-analyzer-nancy.git](https://github.com/nancyboukamel-ds/text-analyzer-nancy.git)
   cd text-analyzer-nancy

## Execute the script
python main.py 

## Example output
--- Text Analysis Results ---
Total Words: 181
Total Sentences: 38

Top 10 Most Frequent Words:
- and: 9
- ai: 7
- we: 6
- repeat: 5
- is: 4
- are: 4
- to: 2
- 2026: 2
- ship: 2
- test: 2

### 2. Pattern Breakdown

| Pattern | Description | Example Match |
| :--- | :--- | :--- |
| `(?:https?://\S+)` | Matches strings starting with http/https followed by non-whitespace characters. | `https://example.com/docs` |
| `(?:[\w.+-]+@[\w-]+\.[\w.-]+)` | Matches standard email structures. | `hello@example.com` |
| `(?:\d+\.\d+\|1e-\d+)` | Matches floating point numbers or scientific notation. | `3.14`, `1e-3` |
| `(?:[\w\d]+(?:-[\w\d]+)+)` | Matches words joined by hyphens. The nested group `(?:-[\w\d]+)+` ensures we catch multiple hyphens. | `end-to-end`, `INC-2026-00042` |
| `(?:[\w\d]+(?:'[\w\d]+)+)` | Matches words containing apostrophes. | `don't`, `isn't` |
| `(?:\b\w+\b)` | The fallback: matches any standard alphanumeric "word" bound by spaces or punctuation. | `hello`, `world` |