# PRODIGY_CS_03
# Password Complexity Checker

## Overview
This is a simple GUI-based Python application that checks the complexity of a given password. The program ensures that the password meets standard security requirements, such as length, uppercase and lowercase letters, digits, and special characters.

## Features
- Validates password strength based on:
  - Minimum length of 8 characters
  - At least one lowercase letter
  - At least one uppercase letter
  - At least one digit
  - At least one special character
- Provides real-time feedback on missing criteria.
- User-friendly graphical interface using Tkinter.

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)

## Snapshot of imports 
```bash
import re
import tkinter as tk
from tkinter import messagebox
```

## Run on CMD
1. Run the application:
   ```bash
   python task03.py
   ```
## Output :

--When program starts and we enter password :
![T1](https://github.com/Indira12-gopal/PRODIGY_CS_03/blob/main/o03%20(1).jpeg)

--When we have entered password "indir@Bhatta4jee" we get:

![T2](https://github.com/Indira12-gopal/PRODIGY_CS_03/blob/main/o03%20(2).jpeg)

## Usage
1. Enter a password into the input field.
2. Click the "Check Password" button.
3. The application will display whether the password is strong or provide feedback on how to improve it.

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork this repository and submit pull requests for improvements!

## Author
Indira Bhattacharjee
