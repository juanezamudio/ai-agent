# 🤖 AI Code Assistant

A command-line interface (CLI) tool that leverages Google's Gemini AI to assist with coding questions and provide programming help. Built with Python 3.12+.

## ✨ Features

- 🔍 Get instant coding help directly in your terminal
- 💡 Powered by Google's Gemini 2.0 Flash AI model
- 📊 Token usage tracking for monitoring API costs
- 🔧 Simple and intuitive command-line interface

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-agent.git
   cd ai-agent
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

## 🔑 Configuration

1. Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Create a `.env` file in the project root and add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 🛠️ Usage

```bash
# Basic usage
python main.py "your coding question here"

# Example
python main.py "How do I implement a binary search in Python?"

# Verbose mode (shows token usage)
python main.py "Explain async/await in Python" --verbose
```

## 📝 Example Output

```
$ python main.py "How do I reverse a string in Python?"

In Python, you can reverse a string in several ways. Here are the most common methods:

1. Using slicing:
    text = "Hello, World!"
    reversed_text = text[::-1]
    print(reversed_text)  # Output: "!dlroW ,olleH"

2. Using the reversed() function with join():
    text = "Hello, World!"
    reversed_text = ''.join(reversed(text))
    print(reversed_text)  # Output: "!dlroW ,olleH"

The slicing method is generally the most Pythonic and efficient way to reverse a string.
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Juan Zamudio - [@your_twitter](https://twitter.com/your_twitter)

---

Made with ❤️ by Juan Zamudio
