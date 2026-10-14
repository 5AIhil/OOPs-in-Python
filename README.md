# Object-Oriented Programming (OOP) in Python

A structured collection of Python scripts and Jupyter notebooks demonstrating core Object-Oriented Programming (OOP) concepts, conventions, and best practices in Python.

---

## 📚 Topics & Repository Structure

| File | Description | Key Concepts |
| :--- | :--- | :--- |
| [`oops_py.ipynb`](./oops_py.ipynb) | Introduction to Classes & Objects | Class definition, instantiation, `__init__` constructor, `self`, object interaction |
| [`script.py`](./script.py) | Basics of Encapsulation | Protected attributes convention (`_variable`), basic getters |
| [`s1.py`](./s1.py) | Private Attributes & Name Mangling | Private variables (`__variable`), name mangling (`_Class__variable`), Python's consenting adults philosophy |
| [`s2.py`](./s2.py) | Getter & Setter Methods | Traditional getters and setters, data validation, preserving state integrity |
| [`s3.py`](./s3.py) | Properties & Decorators | `@property` and `@<attribute>.setter`, Pythonic syntactic sugar for getter/setters |
| [`s4.py`](./s4.py) | Class (Static) Attributes | Class-level variables shared across instances, instance counter pattern |
| [`s5.py`](./s5.py) | Static Methods & Helper Functions | `@staticmethod` decorator, utility methods, internal helper methods |

---

## 🔑 Core Concepts Covered

### 1. Classes, Objects, and `__init__`
- Defining a blueprint with `class`.
- Initializing instance attributes using the `__init__` dunder method.
- The role of `self` in pointing to the current instance.

### 2. Encapsulation & Access Control
- **Public**: Accessible anywhere (`self.username`).
- **Protected (`_variable`)**: A convention indicating that the attribute is intended for internal or subclass use only.
- **Private (`__variable`)**: Triggers Python's name mangling mechanism (`_ClassName__variable`) to prevent accidental overrides in subclasses.

### 3. Getters and Setters
- Traditional methods (`get_email`, `set_email`) to control access and validate data before modifying internal state.

### 4. Properties (`@property`)
- Using the `@property` decorator to turn methods into readable attributes.
- Using `@<property_name>.setter` for validation without breaking the attribute access syntax (`user.email = ...`).

### 5. Class Attributes (Static Variables)
- Attributes defined directly inside the class body, shared by all instances (e.g., `user_count`).
- Modified and accessed via the class name or instance.

### 6. Static Methods (`@staticmethod`)
- Methods that do not receive an implicit first argument (`self` or `cls`).
- Ideal for utility and validation functions whose behavior depends solely on parameters passed to them.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook / JupyterLab (optional, for viewing notebooks)

### Running the Scripts
Run any script directly using Python:

```bash
python3 s1.py
python3 s2.py
python3 s3.py
python3 s4.py
python3 s5.py
```
