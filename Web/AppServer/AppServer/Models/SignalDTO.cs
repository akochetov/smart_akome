using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    /// <summary>
    /// Signal entity, representing signal able to send or receive signals
    /// </summary>
    public class SignalDTO
    {
        public SignalDTO() { }

        public SignalDTO(Signal signal)
        {
            ID = signal.ID;
            Name = signal.Name;
            SignalDirection = signal.SignalDirection;
            Pattern = signal.Pattern;
            DeviceID = signal.DeviceID;
        }

        [Key]
        public int ID { get; set; }

        [Required]
        public string Name { get; set; }       
        public SignalDirection SignalDirection { get; set; }
        public short[] Pattern { get; set; }
        public int DeviceID { get; set; }

        public Signal ToEntity()
        {
            Signal signal = new Signal
            {
                Name = Name,
                ID = ID,          
                SignalDirection = SignalDirection,
                Pattern = Pattern,
                DeviceID = DeviceID
            };

            return signal;
        }
    }
}