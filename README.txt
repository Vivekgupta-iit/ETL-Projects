
# Scientific Calculator Web App

This project is a simple scientific calculator web application built using Python and Flask. The application allows users to enter mathematical expressions, which are then evaluated using Python's `eval` function to provide the result. The goal of this project is to demonstrate a basic implementation of a scientific calculator and showcase how to deploy it as a web app.

## Features

- Evaluate mathematical expressions with support for basic arithmetic operations.
- Handle basic error handling for invalid expressions.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3 (https://www.python.org/downloads/)
- Git (https://git-scm.com/downloads/)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd scientific-calculator-web-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. Start the Flask web server by running the following command:

   ```bash
   python app.py
   ```

2. Open your web browser and visit `http://localhost:5000` to access the scientific calculator web app.

3. Enter a mathematical expression in the input field and click the "Calculate" button to view the result.

## Notes

- **Security Warning**: This project uses the `eval` function for expression evaluation, which can be risky if user input is not properly validated. For real-world applications, consider using a safer expression evaluation method.

- This project is intended as a basic demonstration and does not include advanced mathematical operations or complex error handling.

## Contributing

Contributions to the project are welcome! If you find any issues or have ideas for improvements, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--
