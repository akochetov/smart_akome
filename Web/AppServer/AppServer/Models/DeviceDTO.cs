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
    public class DeviceDTO
    {
        public DeviceDTO() { }

        public DeviceDTO(Device device)
        {
            ID = device.ID;
            Name = device.Name;
            CommunicationMethod = device.CommunicationMethod;
            Signals = new List<SignalDTO>();

            if (device.Signals != null)
                foreach (Signal signal in device.Signals)
                {
                    Signals.Add(new SignalDTO(signal));
                }
        }

        [Key]
        public int ID { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        public DeviceCommunicationMethod CommunicationMethod { get; set; }

        public virtual List<SignalDTO> Signals { get; set; }

        public Device ToEntity()
        {
            Device device = new Device
            {
                Name = Name,
                ID = ID,          
                CommunicationMethod = CommunicationMethod,
                Signals = new List<Signal>()
            };
            foreach (Signal signal in device.Signals)
            {
                Signals.Add(new SignalDTO(signal));
            }

            return device;
        }
    }
}