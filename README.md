# 🤖 AI Code Assistant

A command-line interface (CLI) tool that leverages Google's Gemini AI to assist with coding questions, debugging, and file operations. Built with Python 3.12+.

## ✨ Features

- 🔍 Get instant coding help directly in your terminal
- 🐛 Debug and fix code issues with AI assistance
- 📁 File system operations (read, write, list files)
- 🐍 Execute and test Python code
- 💡 Powered by Google's Gemini 2.0 Flash AI model
- 📊 Token usage tracking for monitoring API costs
- 🔒 Secure file operations with working directory restrictions

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

# Enable verbose mode (shows token usage and function calls)
python main.py "your question" --verbose

# Example: Debug a calculation issue
python main.py "my pkg/calculator.py file seems to have a bug. 3 + 7 * 2 shouldn't be 20"

# List files in a directory
python main.py "what files are in the root directory?"

# Read file contents
python main.py "what's in lorem.txt?"

# Run Python files
python main.py "run tests.py"
```

## 🛡️ Security

- All file operations are restricted to the configured working directory
- The tool will not access files outside the working directory
- Function calls are validated and sanitized

## ⚙️ Configuration Options

Edit `config.py` to customize:
- `MAX_FILE_SIZE`: Maximum file size for read operations (default: 10000 bytes)
- `MAX_EXECUTION_TIME`: Maximum execution time for Python scripts (default: 30 seconds)
- `WORKING_DIRECTORY`: Base directory for file operations (default: "./calculator")
- `MAX_ITERATIONS`: Maximum number of AI iterations (default: 20)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Juan Zamudio - [LinkedIn](https://www.linkedin.com/in/juanezamudio/)

---

Made with ❤️ by Juan Zamudio
