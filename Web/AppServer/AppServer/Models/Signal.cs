using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    /// <summary>
    /// Device signal class
    /// </summary>
    public class Signal : IEntityBase
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public SignalDirection SignalDirection { get; set; }
        public short[] Pattern { get; set; }

        public int DeviceID { get; set; }
    }
}