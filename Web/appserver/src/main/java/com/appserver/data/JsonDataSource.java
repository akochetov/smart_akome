package com.appserver.data;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;

import com.appserver.models.Config;
import com.appserver.models.Device;
import com.appserver.models.User;
import com.google.gson.reflect.TypeToken;

import Utils.JsonReader;
import Utils.JsonWriter;

public class JsonDataSource 
{
	private List<Config> Configs = new ArrayList<Config>();
	private String fpath = null;
	
	public JsonDataSource(String fpath)
	{
		this.fpath = fpath;
	}
	    
    public void load() throws IOException
    { 	
    	//load configs
    	Collection<Config> configs = JsonReader.readFromFile(this.fpath, new TypeToken<Collection<Config>>(){}.getType());   		
    	Configs.addAll(configs);    	
   	
    	//load devices
    	for(Iterator<Config> i = Configs.iterator(); i.hasNext(); ) 
    	{
    		Config config = i.next();
 
    		//load devices
    		Collection<Device> devices = JsonReader.readFromFile(config.getConfigFile(), new TypeToken<Collection<Device>>(){}.getType());
    		config.getDevices().addAll(devices);  
    		
			//load signals
			for(Iterator<Device> dev = devices.iterator(); dev.hasNext(); )
			{
				  Device device = dev.next();
				  config.getSignals().addAll(device.getSignals());
			}    	
    	}
    }
    
    public void save() throws IOException
    {
    	JsonWriter.writeToFile(getConfigs(), fpath, new TypeToken<Collection<Config>>(){}.getType());
    }
    
	public List<Config> getConfigs() {	return Configs;	}
}
