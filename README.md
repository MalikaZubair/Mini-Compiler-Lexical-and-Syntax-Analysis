#  Mini Compiler: Lexical & Syntax Analysis

A mini compiler application built in Python that performs **Lexical Analysis** and **Syntax Analysis**, complete with a graphical interface for visualizing the compilation process.

##  Overview

This project implements the front-end phases of a compiler — Lexical Analysis (Tokenization) and Syntax Analysis (Parsing) — to demonstrate how source code is processed and validated. It includes an interactive interface that allows users to input code and view the tokenization and parsing results in real time.

##  Project Structure

```
mini-compiler/
│
├── compiler with interface.py   # Main application (lexer, parser, and GUI)
└── README.md                    # Project documentation
```

##  Features

- **Lexical Analysis:** Breaks down source code into tokens (keywords, identifiers, operators, literals, etc.)
- **Syntax Analysis:** Validates token sequences against grammar rules and detects syntax errors
- **Interactive Interface:** User-friendly GUI to input code and view analysis results
- Real-time error detection and reporting
- Clear breakdown of tokens and parse results

## Tech Stack

- **Language:** Python
- **Interface:** Tkinter *(update if you used PyQt, a web GUI, or another framework)*
- **Concepts:** Compiler Design, Lexical Analysis, Syntax Analysis, Finite Automata, Grammar Parsing

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mini-compiler.git
   cd mini-compiler
   ```

2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

##  How to Run

```bash
python "compiler with interface.py"
```

##  How It Works

1. **Input:** Enter source code into the interface.
2. **Lexical Analysis:** The lexer scans the input and converts it into a stream of tokens, identifying keywords, identifiers, operators, and literals.
3. **Syntax Analysis:** The parser checks the token stream against the defined grammar rules to verify the code's structural correctness.
4. **Output:** The interface displays the generated tokens and syntax analysis results, including any errors found.

##  Screenshots

*(Add screenshots or a GIF of the interface in action here)*

##  Future Improvements

- Add Semantic Analysis phase
- Add support for more complex grammars
- Generate and display parse trees / AST visually
- Add intermediate code generation
- Improve error messages with line/column tracking

##  Author

**Malika**
Computer Science Graduate | AI/ML & Full-Stack Developer

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
