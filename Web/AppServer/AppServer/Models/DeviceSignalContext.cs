using System;
using System.Collections.Generic;
using System.Web.Configuration;
using System.IO;

using Newtonsoft.Json;

namespace AppServer.Models
{
    public class DeviceSignalContext
    {
        private static DeviceSignalContext _self;

        private List<Signal> _signals = new List<Signal>();
        private List<Device> _devices = new List<Device>();

        private DeviceSignalContext()
        {
            string filePath = WebConfigurationManager.ConnectionStrings["JsonConnection"].ConnectionString;
            if (String.IsNullOrEmpty(filePath))
                throw new ArgumentException("JsonConnection connection string is not specified in web.config");

            // read JSON directly from a file
            using (StreamReader file = File.OpenText(filePath))
            {
                JsonSerializer serializer = new JsonSerializer();
                Devices.AddRange((List<Device>)serializer.Deserialize(file, typeof(List<Device>)));
            }
/*
            if (Devices.Count == 0)
            {
                Devices.Add(new Device { ID = 1, Name = "Light Switch", CommunicationMethod = DeviceCommunicationMethod.Receive });
                Devices.Add(new Device { ID = 2, Name = "Speakers", CommunicationMethod = DeviceCommunicationMethod.Receive });
                Devices.Add(new Device { ID = 3, Name = "Motion Sensor", CommunicationMethod = DeviceCommunicationMethod.Send });
            }

            foreach (Device device in Devices)
            {
                device.Signals.Add(new Signal { ID = 1, DeviceID = device.ID, Name = "On/Off", SignalDirection = SignalDirection.FromDevice });
                device.Signals.Add(new Signal { ID = 2, DeviceID = device.ID, Name = "On/Off", SignalDirection = SignalDirection.ToDevice });
            }

            using (StreamWriter file = File.CreateText(filePath))
            {
                JsonSerializer serializer = new JsonSerializer();
                serializer.Formatting = Formatting.Indented;
                serializer.Serialize(file, Devices);
            }
 */
        }

        public static DeviceSignalContext Instance
        {
            get
            {
                if (_self == null)
                    _self = new DeviceSignalContext();
                return _self;
            }
        }

        public List<Signal> Signals { get { return _signals;} }
        public List<Device> Devices { get { return _devices;} }
    }
}