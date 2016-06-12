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
    public class DeviceController : ApiController
    {
        private DeviceSignalContext db = new DeviceSignalContext();

        // GET api/devices
        public IEnumerable<DeviceDTO> Get()
        {
            IEnumerable<DeviceDTO> result = db.Devices.Include("Signals").AsEnumerable().Select(device => new DeviceDTO(device));
            return result;
        }

        // GET api/devices/5
        public DeviceDTO Get(int id)
        {
            Device device = db.Devices.Find(id);
            if (device == null)
            {
                throw new HttpResponseException(Request.CreateResponse(HttpStatusCode.NotFound));
            }

            return new DeviceDTO(device);
        }

        // POST api/devices
        [ValidateHttpAntiForgeryToken]
        public HttpResponseMessage Post([FromBody]DeviceDTO deviceDTO)
        {
            if (!ModelState.IsValid)
                return Request.CreateErrorResponse(HttpStatusCode.BadRequest, ModelState);

            Device device = deviceDTO.ToEntity();
            db.Devices.Add(device);
            db.SaveChanges();
            deviceDTO.ID = device.ID;

            HttpResponseMessage response = Request.CreateResponse(HttpStatusCode.Created, deviceDTO);
            response.Headers.Location = new Uri(Url.Link("DefaultApi", new { id = deviceDTO.ID }));
            return response;
        }

        // PUT api/devices/5
        public HttpResponseMessage Put(int id, [FromBody]DeviceDTO deviceDTO)
        {
            if (!ModelState.IsValid)
            {
                return Request.CreateErrorResponse(HttpStatusCode.BadRequest, ModelState);
            }

            if (id != deviceDTO.ID)
            {
                return Request.CreateResponse(HttpStatusCode.BadRequest);
            }

            Device device = deviceDTO.ToEntity();
            db.Entry(device).State = EntityState.Modified;

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

        // DELETE api/devices/5
        [ValidateHttpAntiForgeryToken]
        public HttpResponseMessage Delete(int id)
        {
            Device device = db.Devices.Find(id);
            if (device == null)
            {
                return Request.CreateResponse(HttpStatusCode.NotFound);
            }

            DeviceDTO deviceDTO = new DeviceDTO(device);
            db.Devices.Remove(device);

            try
            {
                db.SaveChanges();
            }
            catch (DbUpdateConcurrencyException)
            {
                return Request.CreateResponse(HttpStatusCode.InternalServerError);
            }

            return Request.CreateResponse(HttpStatusCode.OK, deviceDTO);
        }

        protected override void Dispose(bool disposing)
        {
            db.Dispose();
            base.Dispose(disposing);
        }
    }
}
