package com.appserver.data;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import java.io.*;

import com.appserver.models.Config;
import com.appserver.models.Device;
import com.appserver.models.Signal;
import com.appserver.models.User;
import com.appserver.data.UserDTO;

import Utils.JsonReader;

import com.google.gson.reflect.TypeToken;

public class DbContext
{
     private List<Config> Configs = new ArrayList<Config>();
     private List<User> Users = new ArrayList<User>();

     private Config currentConfig;
    
    public DbContext(String fpath) throws IOException
    { 	
    	//load configs
    	Collection<Config> configs = JsonReader.readFromFile(fpath, new TypeToken<Collection<Config>>(){}.getType());   		
    	Configs.addAll(configs);    	
   	
    	//load devices
    	for(Iterator<Config> i = Configs.iterator(); i.hasNext(); ) 
    	{
        	    Config config = i.next();

        	    if (config.isActive())
        	    	selectConfig(config);
 
        		//load devices
    		Collection<Device> devices = JsonReader.readFromFile(fpath, new TypeToken<Collection<Device>>(){}.getType());
    		config.getDevices().addAll(devices);  
    		
			//load signals
			for(Iterator<Device> dev = devices.iterator(); dev.hasNext(); )
			{
				  Device device = dev.next();
				  config.getSignals().addAll(device.getSignals());
			}    	
    	}
    }

	public User getUserByUsername(String username)
	{
		int index = getUsers().indexOf(new User(0,username));

		if (index == -1) throw new NoSuchElementException();
		
		return getUsers().get(index);
	}
    
	private void selectConfig(Config config)
	{
		if (currentConfig != null) 
		{
			System.out.println("Deativating config: "+currentConfig.getConfigFile());
			currentConfig.Deactivate();
		}

		System.out.println("Activating config: "+config.getConfigFile());
		currentConfig = config;
		currentConfig.Activate();
	}
        
	public Config putConfig(int id, UserDTO userdto)
	{
		//Find user by user name
		User user = getUserByUsername(userdto.Username);

		if (!user.Authenticate(userdto.Username,userdto.Password))
			throw new IllegalArgumentException();

		//Select config
		int index = getConfigs().indexOf(new Config(id));

		if (index == -1) throw new NoSuchElementException();
		
		selectConfig(getConfigs().get(index));
		
		return currentConfig;
	}
	
	public Config getConfig(int id)
	{
		int index = getConfigs().indexOf(new Config(id));

		if (index == -1) throw new NoSuchElementException();
		
		return getConfigs().get(index);
	}
    
	
	
	public int addDevice(Device device)
	{
		throw new java.lang.UnsupportedOperationException();
	}

	public Device putDevice(int id, Device device)
	{
		throw new java.lang.UnsupportedOperationException();
	}
	
	public Device getDevice(int id)
	{
		int index = getDevices().indexOf(new Device(id));

		if (index == -1) throw new NoSuchElementException();
		
		return getDevices().get(index);
	}
	
	
	
	public Signal getSignal(int id)
	{
		int index = getSignals().indexOf(new Signal(id));

		if (index == -1) throw new NoSuchElementException();
		
		return getSignals().get(index);
	}
	
	public List<Signal> getSignals() {	return currentConfig.getSignals();	}
	public List<Device> getDevices() {	return currentConfig.getDevices();	}
	public List<Config> getConfigs() {	return Configs;	}
	public List<User> getUsers() {	return Users;	}
}
