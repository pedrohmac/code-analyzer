# Python Code Analyzer

## Overview
This Python Code Analyzer was created as a base step for CI/CD pipeline construction and is a tool designed to analyze the complexity of Python code files (.py) within a specified directory. It also performs linting using pylint to provide insights into the code quality.

## Features
- Analyze the complexity of Python code files based on control flow structures.
- Perform linting using pylint to detect potential code quality issues.
- Supports analysis of multiple Python files within a directory.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.
- Pylint package installed (`pip install pylint`).

### Installation
1. Clone the repository to your local machine:

    ```
    git clone https://github.com/pedrohmac/code-analyzer.git
    ```

2. Navigate to the project directory:

    ```
    cd code-analyzer
    ```

### Usage
1. Run the script by executing the following command:

    ```
    python analyzer.py
    ```

2. Enter the folder path containing Python files when prompted.

3. The script will then analyze the complexity and lint the Python files within the specified directory.

## File Structure
- `analyzer.py`: Main Python script for code analysis.
- `README.md`: Documentation file.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project.

## License
This project is licensed under the MIT License.

## Acknowledgements
- This project utilizes the [ast](https://docs.python.org/3/library/ast.html) module for abstract syntax tree analysis in Python.
- Special thanks to the Python community for developing and maintaining helpful tools and libraries.
