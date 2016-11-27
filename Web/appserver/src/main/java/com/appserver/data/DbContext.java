package com.appserver.data;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import java.io.*;
import java.lang.reflect.Type;

import com.appserver.models.Config;
import com.appserver.models.Device;
import com.appserver.models.Signal;
import com.appserver.models.User;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class DbContext
{
     private List<Config> Configs = new ArrayList<Config>();
     private List<User> Users = new ArrayList<User>();

     private Config currentConfig;
    
    public DbContext(String connectionString) throws IOException
    {
    	Gson gson = new Gson();
    	Type collectionType = new TypeToken<Collection<Config>>(){}.getType();
    	
    	FileReader fileReader = null;
    	
    	//load configs
    	try    
    	{
    		fileReader = new FileReader(connectionString);
    		
    		Collection<Config> configs = gson.fromJson(fileReader, collectionType);
    		
    		//load configs
    		Configs.addAll(configs);    	
    		
    		//setup current config
    		selectConfig(Configs.get(0));
    	}
    	finally
    	{
    		if (fileReader != null) fileReader.close();
    	}
    	
    	//load devices
    	collectionType = new TypeToken<Collection<Device>>(){}.getType();
    	for(Iterator<Config> i = Configs.iterator(); i.hasNext(); )
        	try    
        	{
        	    Config config = i.next();
        		fileReader = new FileReader(config.getConfigFile());
        		
        		Collection<Device> devices = gson.fromJson(fileReader, collectionType);
        		
        		//load devices
        		config.getDevices().addAll(devices);  
        		
        		    	//load signals
            	for(Iterator<Device> dev = devices.iterator(); dev.hasNext(); )
            	{
            		  Device device = dev.next();
            		  config.getSignals().addAll(device.getSignals());
            	}    	
        	}
        	finally
        	{
        		if (fileReader != null) fileReader.close();
        	}
   	
        }
    
	private void selectConfig(Config config)
	{
		if (currentConfig != null) currentConfig.Deactivate();

		currentConfig = config;
		currentConfig.Activate();
	}
        
    	public Config putConfig(int id, Config config)
	{
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


	public User getUserByUsername(String username)
	{
		int index = getUsers().indexOf(new User(0,username,""));

		if (index == -1) throw new NoSuchElementException();
		
		return getUsers().get(index);
	}
    
	
	public List<Signal> getSignals() {	return currentConfig.getSignals();	}
	public List<Device> getDevices() {	return currentConfig.getDevices();	}
	public List<Config> getConfigs() {	return Configs;	}
	public List<User> getUsers() {	return Users;	}
}
