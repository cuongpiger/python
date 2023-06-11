#!/usr/bin/sh

# create virtual env using anaconda
create_virtual_env() {
    echo "Creating the Virtual ENV using Anaconda"
    conda create -n python_grpc python=3.8 pip
}

generate_grpc_calculator() {
    echo "Generating the GRPC Calculator"
    python -m grpc_tools.protoc -I./src --python_out=./src --grpc_python_out=./src ./src/calculator.proto
}

install_dependencies() {
    echo "Installing the dependencies"
    pip install -r requirements.txt
}

delete_virtual_env() {
    echo "Deleting the Virtual ENV"
    conda remove -y --name python_grpc --all && \
    sudo rm -rf $HOME/anaconda3/envs/python_grpc
}

run_server() {
    echo "Running the Server"
    python src/server.py
}

run_client() {
    echo "Running the Client"
    python src/client.py
}

# switch case for the $1 argument
case $1 in
"create_virtual_env")
    create_virtual_env
    ;;
"generate_calculator_protobuf")
    generate_grpc_calculator
    ;;
"install_dependencies")
    install_dependencies
    ;;
"delete_virtual_env")
    delete_virtual_env
    ;;
"run_server")
    run_server
    ;;
"run_client")
    run_client
    ;;
*)
    echo "Invalid argument"
    ;;
esac
