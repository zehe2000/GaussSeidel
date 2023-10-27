Gauss-Seidel Solver Project README
Overview
This project aims to provide a Python-based solution to linear systems of equations using the Gauss-Seidel method. The project is organized into five primary Python files that each serve specific functions:

main.py: Executes the core functionality and serves as the entry point to the application.
readEquation.py: Reads and validates the system of equations from a text file.
testReadEquation.py: Contains unit tests for readEquation.py.
GaussSeidelAlgorithm.py: Implements the Gauss-Seidel algorithm to solve equations.
testGauss.py: Contains unit tests for GaussSeidelAlgorithm.py.
How to Use
To run the main program, use the following command:

bash
Copy code
python main.py <file_path> [-t <tolerance>] [-i <max_iter>]
file_path: Path to the text file containing the system of equations.
-t, --tolerance: Tolerance level for the Gauss-Seidel method (optional, default is 1e-7).
-i, --max_iter: Maximum number of iterations for the Gauss-Seidel method (optional, default is 10000).
Example
bash
Copy code
python main.py equations.txt -t 1e-7 -i 10000
Files Description
main.py
The main program that glues everything together. It uses argparse for command-line argument parsing. It reads the equation file, validates it, applies the Gauss-Seidel method, and prints the result. It also saves the output to output.txt.

readEquation.py
This file has two main functions:

readfile(file_path): Reads the content of the file from the given path.
convertContentToArray(content): Validates and converts the read content to a NumPy array.
The file must contain sections prefixed by A: and b: to specify the matrix and the vector, respectively.

testReadEquation.py
Contains a series of unit tests that test various aspects of the readEquation.py file, such as whether the equations are overdetermined, underdetermined, or if the file format is wrong.

GaussSeidelAlgorithm.py
Contains the gaussSeidel function, which takes a matrix, a vector, a tolerance level, and a maximum iteration count as arguments. It returns the solution to the equation using the Gauss-Seidel method.

testGauss.py
Includes unit tests that check the functionality of the GaussSeidelAlgorithm.py. It uses NumPy's testing framework for array comparisons.

Dependencies
Python 3.9.13
NumPy



bash
Copy code
pip install numpy
Run the program as described in the "How to Use" section.

Testing
To run tests, execute:

bash
Copy code
python -m unittest testReadEquation.py
python -m unittest testGauss.py
License
This project is licensed under the MIT License. See the LICENSE.md file for details.

Authors
[Zeinab Herz]
Feel free to reach out for any issues or contributions.