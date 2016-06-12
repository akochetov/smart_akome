using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;

namespace AppServer.Models
{
    public class DeviceSignalContext : DbContext
    {
        public DeviceSignalContext()
            : base("name=DefaultConnection")
        {
        }

        public DbSet<Signal> Signals { get; set; }
        public DbSet<Device> Devices { get; set; }
    }
}