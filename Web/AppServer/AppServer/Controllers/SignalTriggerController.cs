using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Text;

using Newtonsoft.Json;

using AppServer.Models;
using AppServer.Filters;

using RabbitMQ.Client;

namespace AppServer.Controllers
{
    //[Authorize]
    [ValidateHttpAntiForgeryToken]
    public class SignalTriggerController : ApiController
    {
        // POST api/signaltrigger
        public HttpResponseMessage Post([FromBody]SignalDTO signalDTO)
        {
            //trigger signal here

            PostSignalToQueue(signalDTO.ToEntity());

            HttpResponseMessage response = Request.CreateResponse(HttpStatusCode.Accepted, signalDTO);
            response.Headers.Location = new Uri(Url.Link("DefaultApi", new { id = signalDTO.ID }));
            return response;
        }

        private void PostSignalToQueue(Signal signal)
        {
            var factory = new ConnectionFactory() { HostName = "192.168.0.100",UserName="pi",Password="pi"};
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.QueueDeclare(queue: "smart_akome",
                                     durable: false,
                                     exclusive: false,
                                     autoDelete: false,
                                     arguments: null);

                string message = JsonConvert.SerializeObject(signal);
                var body = Encoding.UTF8.GetBytes(message);

                channel.BasicPublish(exchange: "",
                                     routingKey: "smart_akome",
                                     basicProperties: null,
                                     body: body);
            }
        }
    }
}
