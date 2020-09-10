using System;
using Grpc.Core;
using GrpcSimple;
using Google.Protobuf.WellKnownTypes;

namespace ExampleGrpcClient
{
    public class MainClass
    {
        public static void Main(string[] args)
        {
            var channel = new Channel("127.0.0.1:5051", ChannelCredentials.Insecure);
            var client = new SimpleService.SimpleServiceClient(channel);


            var req = new SimpleRequestList();
            var req_1 = new SimpleRequest();
            req_1.Name = "ken";
            req_1.Msg = "baka";
            req.PersonList.Add(req_1);
            var req_2 = new SimpleRequest();
            req_2.Name = "tom";
            req_2.Msg = "aho";
            req.PersonList.Add(req_2);

            var res = client.SimpleSend(req);
            foreach (var item in res.ResponseList)
            {
                Console.WriteLine(item.ReplyMsg);
            }
        }
    }
}
