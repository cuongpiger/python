import grpc

import calculator_pb2
import calculator_pb2_grpc

# open thje gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)

# make a call
response = stub.SquareRoot(number)

# print response
print(f"Client: respose.value = {response.value}")
