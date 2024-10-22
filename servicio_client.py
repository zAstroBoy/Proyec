import grpc
# Importamos las clases generadas por Protocol Buffers
import servicio_pb2
import servicio_pb2_grpc

def run():
    try:
        # Establecemos la conexión con el servidor
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = servicio_pb2_grpc.FactorialServiceStub(channel)
            
            # Definimos el número para el cual queremos calcular el factorial
            number = 8

            # Realizamos la llamada RPC al servidor
            response = stub.CalculateFactorial(servicio_pb2.FactorialRequest(number=number))
            
            # Mostramos el resultado devuelto por el servidor
            print(f"Factorial de {number}: {response.result}")

    except grpc.RpcError as e:
        # Capturamos errores relacionados con la comunicación gRPC
        print(f"Error al conectarse al servidor: {e.details()}")

if __name__ == '__main__':
    run()
