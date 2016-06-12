using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace AppServer.Models
{
    public interface IEntityBase
    {
        int ID { get; set; }
    }
}