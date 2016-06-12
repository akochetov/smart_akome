using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    /// <summary>
    /// Device entity, representing device able to send or receive signals
    /// </summary>
    public class Device : IEntityBase
    {
        [Required]
        public int ID { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public DeviceCommunicationMethod CommunicationMethod { get; set; }

        public List<Signal> Signals { get; set; }

        public override bool Equals(object obj)
        {
            if (obj == null)
                throw new ArgumentNullException();

            Device device = obj as Device;
            if (device == null)
                throw new InvalidCastException("Object of Device type is expected. Type given: "+obj.GetType().ToString());

            return device.ID == ID;
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
    }
}