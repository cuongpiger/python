###### References
* The guideline - [https://www.learnpythonwithrune.org/ultimate-tox-guide-with-practical-examples-with-mypy-and-pytest](https://www.learnpythonwithrune.org/ultimate-tox-guide-with-practical-examples-with-mypy-and-pytest/)
* Author's source code - [https://github.com/LearnPythonWithRune/fruit-service-with-tox](https://github.com/LearnPythonWithRune/fruit-service-with-tox)

<hr>

# 1. Introduction
* This is a simple guideline to use `tox` to test your Python project.

# 2. Pre-requisites
* Anaconda

# 3. Instruction
Create a virtual environment for your project using **Anaconda**:
  ```bash=
  make create-env
  ```

Install `tox`:
  ```bash=
  make install-tox
  ```

Using `tox` to test your project:
  ```bash=
  make tox
  ```
  ![](./img/01.png)
  