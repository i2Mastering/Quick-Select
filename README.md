# Quick Select Algorithm

## Description
This Python program implements the Quick Select algorithm, an efficient method for finding the k-th smallest element in an unsorted array. The program generates a random list of 1000 integers and allows the user to select a k-th smallest element interactively.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Classes](#classes)
- [Requirements](#requirements)
- [License](#license)

## Features
- Uses the Quick Select algorithm for fast k-th smallest element selection.
- Generates a random array of integers between 1 and 1000.
- Allows user input to specify the desired k-th smallest element.
- Efficient partitioning using a pivot selection method.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/quick-select-algorithm.git
   ```
2. Navigate to the project directory:
   ```sh
   cd quick-select-algorithm
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Run the script:
   ```sh
   python quick_select.py
   ```
2. Enter a value for `k` when prompted (between 1 and 1000).
3. The program will return the k-th smallest element in the randomly generated array.

## Example Output
```sh
Enter the value of k. Please choose a number between 1 and 1000: 5
The array that has been generated with the total of one thousand numbers is: [...]
The 5th smallest element is 42
```

## Classes
### `Solution`
- Implements the Quick Select algorithm.
- **Methods:**
  - `arrSplit(nums, l, r)`: Partitions the array around a pivot, placing smaller elements on the left and larger elements on the right.
  - `quick_select(nums, l, r, k)`: Finds the k-th smallest element in the array using Quick Select.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
