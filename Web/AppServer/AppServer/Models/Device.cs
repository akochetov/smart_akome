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
        private List<Signal> _signals = new List<Signal>();

        [Required]
        public int ID { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public DeviceCommunicationMethod CommunicationMethod { get; set; }

        public List<Signal> Signals { get { return _signals; } }

        public override bool Equals(object obj)
        {
            if (obj == null)
                throw new ArgumentNullException();

            Device device = obj as Device;
            if (device == null)
                return base.Equals(obj);

            return device.ID == ID;
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }
    }
}