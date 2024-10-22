import grpc
from concurrent import futures
import time

# Importamos las clases generadas por Protocol Buffers
import servicio_pb2
import servicio_pb2_grpc

# Implementamos la clase del servicio que hereda de la clase generada
class FactorialServiceServicer(servicio_pb2_grpc.FactorialServiceServicer):
    def CalculateFactorial(self, request, context):
        number = request.number
        result = self.factorial(number)
        return servicio_pb2.FactorialResponse(result=result)

    def factorial(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n - 1)

# Configuramos y ejecutamos el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicio_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Mantiene el servidor en ejecución
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
