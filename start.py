import randomCNF
from concurrent import futures
import grpc, time
from api_pb2 import Cnf
import api_pb2_grpc

class RandomCnf(api_pb2_grpc.ServiceServicer):
    def RandomCnf(self, request, context):
        return randomCNF.ok()

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
api_pb2_grpc.add_ServiceServicer_to_server(
    RandomCnf(), server=server
)

print('Starting server. Listening on port 8000.')
server.add_insecure_port('[::]:8000')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)