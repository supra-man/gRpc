import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
class UnaryService(pb2_grpc.UnaryServicer):
    pass

    def GetServerResponse(self,request,context):
        message = request.message
        result = f"Server received: {message}"
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(),server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    print("Server started at...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()