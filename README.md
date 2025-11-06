# algorithm-challenge-backend-sanaap

This repository contains clean, testable Python implementations of SANAAP algorithmic problems.  
Each module is organized into its own folder with a corresponding test suite.

---

## 📁 Repository Structure
```bash
.
├── consecutive_numbers/
│ ├── main/
│ │ └── __init__.py
│ │ └── app.py # contains has_n_consecutive_ones_circular()
│ └── tests/
│   └── __init__.py
│   └── test_consecutive_ones.py # unit tests using pytest
│
├── longest_unique_substring/
│ ├── main/
│ │ └── __init__.py
│ │ └── app.py # contains longest_unique_substring()
│ └── tests/
│   └── __init__.py
│   └── test_longest_unique_substring.py # unit tests using pytest
│
├── .gitignore
├── LICENSE
└── README.md
```

## 🧩 Problems Included

### 1️⃣ Longest Unique Substring
Find the **length of the longest substring** in a string without repeating characters.

**Example:**
```text
Input:  "ABCABCFKAB"
Output: 5 (CFKAB)
```

### 2️⃣ N Consecutive Ones (Circular)

Check whether a binary string contains n consecutive 1s, considering circular rotation
(i.e., the end of the string connects to the start).

**Example:**
```text
Input:  binary_str = "1010111", n = 4
Output: True
```

## 🧪 Running Tests

This project uses pytest for testing.

To run all tests:
```bash
pytest -v
```

To run tests for a specific module:
```bash
pytest longest_unique_substring/tests
# or
pytest consecutive_numbers/tests
```

## ⚙️ Requirements

Python 3.13+

pytest (for running unit tests)

Install dependencies:
```bash
pip install pytest
```

## 📝 License

This project is licensed under the terms of the MIT License

## 👨‍💻 Author

Created by [Abolfazl Jelodar]