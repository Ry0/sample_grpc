import grpc
import time
import simple_pb2
import simple_pb2_grpc
from concurrent import futures


class SimpleServiceServicer(simple_pb2_grpc.SimpleServiceServicer):
    def __init__(self):
        pass

    def SimpleSend(self, request, context):
        # print('logging: name {}, msg {}'.format(request.name, request.msg))
        # protoファイルのResponseと一致させる
        res_list = simple_pb2.SimpleResponseList()
        for req in request.person_list:
            print(req)
            res = simple_pb2.SimpleResponse()
            msg = req.name + " says " + req.msg + ". aho."
            res.reply_msg = msg
            res_list.response_list.append(res)
        return res_list


# start server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
simple_pb2_grpc.add_SimpleServiceServicer_to_server(
    SimpleServiceServicer(), server)
server.add_insecure_port('[::]:5051')
server.start()
print('run server')

# wait
try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    # stop server
    server.stop(0)
