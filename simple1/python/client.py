import grpc
import simple_pb2
import simple_pb2_grpc


with grpc.insecure_channel('localhost:5051') as channel:
    stub = simple_pb2_grpc.SimpleServiceStub(channel)
    person_list = simple_pb2.SimpleRequestList()
    person = simple_pb2.SimpleRequest()
    person.name = "Tom"
    person.msg = "Test"
    person_list.person_list.append(person)

    person.name = "Ken"
    person.msg = "Hoge"
    person_list.person_list.append(person)

    print(person_list)
    response = stub.SimpleSend(person_list)

print(response)
for res in response.response_list:
    print('Reply: ', res.reply_msg)
