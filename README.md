###### [↩ Back to _main_ branch](https://github.com/cuongpiger/python)

<hr>

# 1. Introduction
- A set of simple `oslo.messaging` clients. You can use these clients to play with the `oslo.messaging` API.

# 2. Clients
- The clients includes of:
  - `rpc-server`: Listens for RPC requests and sends replies.
  - `rpc-client`: Sends RPC requests to an RPC server.
  - `notifier`: Sends nofication messages.

- Use `--help` option for more details.


# 3. Running
- These examples assum you are runing the RabbitMQ broker on localhost port 5672.
- To run the RabbitMQ server, using the below command, you also look at [this](https://x-team.com/blog/set-up-rabbitmq-with-docker-compose/#:~:text=Open%20a%20terminal%2C%20navigate%20to,to%20http%3A%2F%2Flocalhost%3A15672.).
  ```bash
  docker compose up -d
  ```

- Run the `rpc-server`:
  ```bash
  ./rpc-server --name Server01 
  ```

- Run the `rpc-client`:
  ```bash
  ./rpc-client --method echo --kwargs "arg1=value1 arg2=value2"i
  ```