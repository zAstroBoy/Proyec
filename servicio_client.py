import grpc

# Importamos las clases generadas por Protocol Buffers
import servicio_pb2
import servicio_pb2_grpc

def run():
    # Nos conectamos al servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = servicio_pb2_grpc.FactorialServiceStub(channel)
        number = 5  # Número para calcular el factorial
        response = stub.CalculateFactorial(servicio_pb2.FactorialRequest(number=number))
        print(f"Factorial de {number}: {response.result}")

if __name__ == '__main__':
    run()

try:
    response = stub.CalculateFactorial(servicio_pb2.FactorialRequest(number=number))
    print(f"Factorial de {number}: {response.result}")
except grpc.RpcError as e:
    print(f"Error al conectarse al servidor: {e.details()}")
