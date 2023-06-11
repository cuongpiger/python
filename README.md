[_↩ Back to `main` branch_](https://github.com/cuongpiger/python)

###### References
* Medium - [https://medium.com/engineering-semantics3/a-simplified-guide-to-grpc-in-python-6c4e25f0c506](https://medium.com/engineering-semantics3/a-simplified-guide-to-grpc-in-python-6c4e25f0c506)

###### Brief
A simple gRPC server and client in Python.

# 1. Prerequisite
* **Important**:
  * Your machine must have **Anaconda** installed.
* Grant execution permission to `cmd/commands.sh` file:
  ```bash=
  chmod +x cmd/commands.sh
  ```

* Create a Python virtual environment:
  ```bash=
  make create-env
  ```

* Activate the Python virtual environment:
  ```bash=
  conda activate python_grpc
  ```

* Install Python packages:
  ```bash=
  make install-deps
  ```

# 2. Run
* Run the server:
  ```bash=
  python ./src/server.py
  ```

* Run the client:
  ```bash=
  python ./src/client.py
  ```

* Check the results:
  ![](./img/01.png)

* **[Optional]** Delete virtual environment:
  ```bash=
  make delete-env
  ```
