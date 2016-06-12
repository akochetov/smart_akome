using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    /// <summary>
    /// Defines signal type, if it is a signal coming from or to device
    /// </summary>
    public enum SignalDirection
    {
        ToDevice = 1,
        FromDevice = 2
    }
}