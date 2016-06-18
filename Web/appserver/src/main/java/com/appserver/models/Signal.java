package com.appserver.models;

/**
 * Device signal class
 */
public class Signal extends EntityBase
{
	private int ID;
	private int DeviceID;
	private short[] Pins;
	private String Name;
	private SignalDirection signalDirection;
	private short[] Pattern;

    public int getID() { return ID; }
	public void setID(int id) { ID = id; }
	
	//This block requires refactoring, DTO has to be added to store DeviceID
    public int getDeviceID() { return DeviceID; }
	public void setDeviceID(int id) { DeviceID = id; }

    public String getName() { return Name; }
	public void setName(String name) { Name = name; }
	
	public SignalDirection getSignalDirection() {	return signalDirection;	}
	public void setSignalDirection(SignalDirection signalDirection) {	this.signalDirection = signalDirection; }
	
	public short[] getPattern() { return Pattern;}
	public short[] getPins() { return Pins;}
	
	public Signal(int id)
	{
		ID = id;
	}	
	public Signal(int id, int deviceid)
	{
		ID = id;
		DeviceID = deviceid;
	}	
}
