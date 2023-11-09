# Gauss-Seidel Solver

## Description

This project provides a solver for systems of linear equations based on the Gauss-Seidel algorithm. The equations are read from a text file and the solution is printed to the console as well as saved to an `output.txt` file.

## Installation

Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/Gauss-Seidel-Solver.git
```


## Files
main.py: The main entry point for the program, handling command-line arguments and coordinating other modules.

readEquation.py: Contains methods to read and validate the system of equations from a text file.

testReadEquation.py: Unit tests for readEquation.py.

GaussSeidelAlgorithm.py: Implements the Gauss-Seidel algorithm.

testGauss.py: Unit tests for GaussSeidelAlgorithm.py.


## Usage
Navigate to the project directory and run the following command:
python main.py <path_to_equation_file> -t <tolerance_level> -i <max_iterations>

path_to_equation_file: Path to the TXT file containing the equations.

tolerance_level: (Optional) Tolerance level for Gauss-Seidel. Default is 1e-7.

max_iterations: (Optional) Maximum number of iterations for Gauss-Seidel. Default is 10000.

## Example
python main.py equations.txt -t 0.00001 -i 5000
This will read the system of equations from equations.txt, solve it using Gauss-Seidel with a tolerance of 0.00001, and perform a maximum of 5000 iterations.

## Testing
To run the tests for reading equations:
python -m unittest testReadEquation.py
To run the tests for Gauss-Seidel algorithm:
python -m unittest testGauss.py


Feel free to customize the content according to your project's needs!
