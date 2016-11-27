package com.appserver.models;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import com.appserver.models.Device;
import com.appserver.models.Signal;

/**
 * System mode configuration class
 */
public class Config extends EntityBase
{
    private int ID = 0;
   
    private String Name;
    private String ConfigFile;
    private String Css;

	private boolean Active = false;
	private boolean InvertColors = false;
       
    private String Icon;  

	private transient List<Signal> Signals = new ArrayList<Signal>(); 
	private transient List<Device> Devices = new ArrayList<Device>(); 

	public Config()
	{

	}	

	public Config(int id)
	{
		ID = id;
	}	

    public int getID() { return ID; }
	public void setID(int id) { ID = id; }

    public boolean isActive() { return Active; }
	public void Activate() { Active = true; }
	public void Deactivate() { Active = false; }

    public String getName() { return Name; };
    public void setName(String name) { Name = name; };
    
    public String getConfigFile() { return ConfigFile; };
    public void setConfigFile(String config) { ConfigFile = config; };
    
    public String getCss() { return Css; };
    public void setCss(String css) { Css = css; };

    public String getIcon() { return Icon;};

	public List<Signal> getSignals() {	return Signals;	}
	public List<Device> getDevices() {	return Devices;	}
}
