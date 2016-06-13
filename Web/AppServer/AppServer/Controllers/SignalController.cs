using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

using AppServer.Models;
using AppServer.Filters;

namespace AppServer.Controllers
{
    //[Authorize]
    [ValidateHttpAntiForgeryToken]
    public class SignalController : ApiController
    {
        private DeviceSignalContext db = DeviceSignalContext.Instance;

        // GET api/signals
        public IEnumerable<Signal> Get()
        {
            return db.Signals;
        }
/*
        // POST api/signals
        [ValidateHttpAntiForgeryToken]
        public HttpResponseMessage Post([FromBody]SignalDTO signalDTO)
        {
            if (!ModelState.IsValid)
                return Request.CreateErrorResponse(HttpStatusCode.BadRequest, ModelState);

            Signal signal = signalDTO.ToEntity();
            db.Entry(signal).State = EntityState.Detached;
            db.Signals.Add(signal);
            db.SaveChanges();
            signalDTO.ID = signal.ID;

            HttpResponseMessage response = Request.CreateResponse(HttpStatusCode.Created, signalDTO);
            response.Headers.Location = new Uri(Url.Link("DefaultApi", new { id = signalDTO.ID }));
            return response;
        }

        // PUT api/signals/5
        public HttpResponseMessage Put(int id, [FromBody]SignalDTO signalDTO)
        {
            if (!ModelState.IsValid)
            {
                return Request.CreateErrorResponse(HttpStatusCode.BadRequest, ModelState);
            }

            if (id != signalDTO.ID)
            {
                return Request.CreateResponse(HttpStatusCode.BadRequest);
            }

            Signal signal = signalDTO.ToEntity();
            Device device = db.Devices.Find(signal.DeviceID);
            if (device == null)
            {
                return Request.CreateResponse(HttpStatusCode.NotFound);
            }

            // Need to detach to avoid duplicate primary key exception when SaveChanges is called
            db.Entry(signal).State = EntityState.Detached;
            db.Entry(signal).State = EntityState.Modified;

            try
            {
                db.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                return Request.CreateResponse(HttpStatusCode.InternalServerError);
            }

            return Request.CreateResponse(HttpStatusCode.OK);
        }

        // DELETE api/signals/5
        [ValidateHttpAntiForgeryToken]
        public HttpResponseMessage Delete(int id)
        {
            Signal signal = db.Signals.Find(id);
            if (signal == null)
            {
                return Request.CreateResponse(HttpStatusCode.NotFound);
            }

            SignalDTO signalDTO = new SignalDTO(signal);
            db.Signals.Remove(signal);

            try
            {
                db.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                return Request.CreateResponse(HttpStatusCode.InternalServerError);
            }

            return Request.CreateResponse(HttpStatusCode.OK, signalDTO);
        }

        protected override void Dispose(bool disposing)
        {
            db.Dispose();
            base.Dispose(disposing);
        }
 */
    }
}
