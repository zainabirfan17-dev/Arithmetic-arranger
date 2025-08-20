# Arithmetic Formatter 🧮

A Python project that takes arithmetic problems (addition, subtraction) and formats them neatly for easy reading.

---

## Features

- Formats arithmetic problems in a vertical, easy-to-read style.
- Supports multiple problems at once.
- Checks for proper input and handles errors gracefully.

---

## Usage

1. Make sure Python is installed (Python 3.x recommended).  
2. Open your terminal or command prompt and navigate to the project folder.  
3. Run the script directly:
```bash
python arithmetic_formatter.py
```
4. Or use the main function in your own script:
```python
from arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))
```
- Set the second argument `True` to display answers. Use `False` to hide them.

---

## Example

**Input:**
```
["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
```

**Output (without answers):**
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

**Output (with answers):**
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

---
## 🎥 Project Demo

[![Watch the video](https://img.youtube.com/vi/eiXL2sJPQpc/0.jpg)](https://youtu.be/eiXL2sJPQpc)



## Author

[Zainab Irfan](https://github.com/zainabirfan17-dev)
