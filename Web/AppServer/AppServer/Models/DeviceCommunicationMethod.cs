using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    /// <summary>
    /// Contains device communication ways, e.g. send, receive etc.
    /// </summary>
    public enum DeviceCommunicationMethod
    {
        /// <summary>
        /// Device can only send signals
        /// </summary>
        Send = 1,
        /// <summary>
        /// Device can only receive signals
        /// </summary>
        Receive = 2,
        /// <summary>
        /// Device can send and receive signals
        /// </summary>
        Both = 3
    }
}