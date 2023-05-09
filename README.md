# Quick GPT Format

`quick_gpt_format` is a Python script that helps you quickly format your codebase into GPT-friendly code blocks, ignoring specified directories and files, and then splitting the content into multiple text files. This can be useful when you want to share your codebase with others in a readable format or when you want to process it using AI models like OpenAI's GPT.

## Features

- Traverses the codebase directory and creates GPT-friendly code blocks
- Ignores specified directories and files
- Splits the output into multiple text files based on a character limit

## Requirements

- Python 3.6+

## Usage

1. Clone the repository or download the `quick_gpt_format.py` script.
2. Open the script in your favorite text editor or IDE.
3. Modify the `ignore_dirs` set to include any directories you want to ignore.
4. Modify the `ignore_files` set to include any files you want to ignore.
5. Save your changes and run the script from the command line:
```
python quick_gpt_format.py
```

# Contributions
We welcome contributions! Feel free to open issues or submit pull requests for improvements, bug fixes, or new features.

# Future
- Add OpenAi API Integration to send off codebase directly to OpenAi GPT
- Add Embeddings to Convert Larger codebases directly into a Long-Term Memory Format
- Add Vector Database Integration to manage Embeddings
