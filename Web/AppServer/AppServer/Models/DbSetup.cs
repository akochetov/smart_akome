using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

using AppServer.Controllers;

namespace AppServer.Models
{
    public class DbSetup
    {
        static List<Device> Devices = new List<Device>
        {
            new Device { ID = 1, Name = "Speakers", CommunicationMethod = DeviceCommunicationMethod.Receive },
            new Device { ID = 2, Name = "Motion Sensor", CommunicationMethod = DeviceCommunicationMethod.Send },
            new Device { ID = 3, Name = "Light Switch", CommunicationMethod = DeviceCommunicationMethod.Receive }
        };

        static List<Signal> Signals = new List<Signal>
        {
            new Signal { ID = 1, DeviceID = 1, Name = "Volume UP", SignalDirection = SignalDirection.ToDevice},
            new Signal { ID = 2, DeviceID = 1, Name = "Volume Down", SignalDirection = SignalDirection.ToDevice},
            new Signal { ID = 3, DeviceID = 1, Name = "Turn On", SignalDirection = SignalDirection.ToDevice},
            new Signal { ID = 4, DeviceID = 1, Name = "Turn Off", SignalDirection = SignalDirection.ToDevice},
            new Signal { ID = 5, DeviceID = 2, Name = "Motion Detected", SignalDirection = SignalDirection.FromDevice},
            new Signal { ID = 6, DeviceID = 3, Name = "Turn On/Off", SignalDirection = SignalDirection.ToDevice}
        };

        public static void Setup()
        {
            DeviceSignalContext db = new DeviceSignalContext();
            foreach (Device device in db.Devices)
                db.Devices.Remove(device);
            foreach (Signal signal in db.Signals)
                db.Signals.Remove(signal);
            db.SaveChanges();
            foreach (Device device in Devices)
            {
                IEnumerable<Signal> signals = Signals.Where(s => s.DeviceID == device.ID);
                foreach (Signal signal in signals)
                    db.Signals.Add(signal);
                db.Devices.Add(device);
            }
            db.SaveChanges(); 
        }
    }
}