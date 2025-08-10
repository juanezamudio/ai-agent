# 🧮 Calculator Application

A command-line calculator application that evaluates mathematical expressions with support for basic arithmetic operations. Built with Python 3.12+.

## ✨ Features

- 🧠 Evaluates mathematical expressions with operator precedence
- 🎨 Beautiful console output with ASCII art formatting
- ➕ Supports basic arithmetic operations: `+`, `-`, `*`, `/`
- 🧪 Comprehensive test suite for reliability
- 🚀 Simple and intuitive command-line interface

## 🚀 Installation

1. Ensure you have Python 3.12 or later installed
2. Clone the repository (if not already done):
   ```bash
   git clone https://github.com/yourusername/ai-agent.git
   cd ai-agent/calculator
   ```

## 🛠️ Usage

Run the calculator with a mathematical expression as an argument:

```bash
python main.py "3 + 5 * 2"
```

Example output:
```
┌─────────────┐
│  3 + 5 * 2  │
│             │
│  =          │
│             │
│  13         │
└─────────────┘
```

### Available Operations

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`

### Examples

```bash
# Simple addition
python main.py "5 + 3"

# Mixed operations with precedence
python main.py "3 + 5 * 2"

# Division
python main.py "10 / 2"

# Complex expression
python main.py "10 + 2 * 6 / 3 - 4"
```

## 🧪 Running Tests

To run the test suite:

```bash
python -m unittest tests.py -v
```

## 🏗️ Project Structure

```
calculator/
├── main.py           # Command-line interface
├── pkg/
│   ├── calculator.py # Core calculator logic
│   └── render.py     # Output formatting
└── tests.py          # Unit tests
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 📬 Contact

Juan Zamudio - [LinkedIn](https://www.linkedin.com/in/juanezamudio/)

---

Made with ❤️ by Juan Zamudio