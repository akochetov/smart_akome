package com.appserver.data;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import java.io.*;

import com.appserver.models.Config;
import com.appserver.models.Device;
import com.appserver.models.Signal;
import com.appserver.models.User;
import com.appserver.data.UserDTO;

public class DbContext
{
	private List<User> Users = new ArrayList<User>();
	
	private JsonDataSource dataSource;
	private Config currentConfig;
    
    public DbContext(String fpath) throws IOException
    { 	
    	dataSource = new JsonDataSource(fpath);
    	dataSource.load();
    	
    	//check if there are any sessions set as active
    	boolean bAnyActiveSessions = false;
    	for(Iterator<Config> i = getConfigs().iterator(); i.hasNext(); ) 
    	{
        	    Config config = i.next();

        	    if (!bAnyActiveSessions && config.isActive())
        	    {
        	    	bAnyActiveSessions = true;   
        	    	currentConfig = config;
        	    	break;
    			}
    	}
    	
    	//if no sessions are activated in config - activate first one by default
    	if (!bAnyActiveSessions && !getConfigs().isEmpty())
    		selectConfig(getConfigs().get(0));
    }

	public User getUserByUsername(String username)
	{
		int index = getUsers().indexOf(new User(0,username));

		if (index == -1) throw new NoSuchElementException();
		
		return getUsers().get(index);
	}
    
	private void selectConfig(Config config) throws IOException
	{
		if (currentConfig != null) 
		{
			System.out.println("Deativating config: "+currentConfig.getConfigFile());
			currentConfig.Deactivate();
		}

		System.out.println("Activating config: "+config.getConfigFile());
		currentConfig = config;
		currentConfig.Activate();
		dataSource.save();
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
		
		try {
			selectConfig(getConfigs().get(index));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
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
	public List<Config> getConfigs() {	return dataSource.getConfigs();	}
	public List<User> getUsers() {	return Users;	}
}
