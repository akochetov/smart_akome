package com.appserver.data;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

import java.io.*;
import java.lang.reflect.Type;

import com.appserver.models.Device;
import com.appserver.models.Signal;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class DbContext
{
    private List<Signal> Signals = new ArrayList<Signal>();
    private List<Device> Devices = new ArrayList<Device>();
    
    public DbContext(String connectionString) throws IOException
    {
    	Gson gson = new Gson();
    	Type collectionType = new TypeToken<Collection<Device>>(){}.getType();
    	
    	FileReader fileReader = null;
    	
    	try    
    	{
    		fileReader = new FileReader(connectionString);
    		
    		Collection<Device> devices = gson.fromJson(fileReader, collectionType);
    		
    		//load devices
    		Devices.addAll(devices);    	
    	}
    	finally
    	{
    		if (fileReader != null) fileReader.close();
    	}
    	
    	//load signals
    	for(Iterator<Device> i = Devices.iterator(); i.hasNext(); )
    	{
    		  Device device = i.next();
    		  Signals.addAll(device.getSignals());
    	}    	
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
		int index = Devices.indexOf(new Device(id));

		if (index == -1) throw new NoSuchElementException();
		
		return Devices.get(index);
	}
	
	public Signal getSignal(int id)
	{
		int index = Signals.indexOf(new Signal(id));

		if (index == -1) throw new NoSuchElementException();
		
		return Signals.get(index);
	}
	
	public List<Signal> getSignals() {	return Signals;	}
	public List<Device> getDevices() {	return Devices;	}
}
