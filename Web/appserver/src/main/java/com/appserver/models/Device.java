package com.appserver.models;

import java.util.ArrayList;
import java.util.List;

/**
 * Device entity, representing device able to send or receive signals
 */
public class Device extends EntityBase
{
	private int ID = 0;
	private String Name;
	private DeviceCommunicationMethod CommunicationMethod;
	private String Icon;
	private List<Signal> Signals = new ArrayList<Signal>();
	private int SignalSourceID = 0;
	private int SignalDestinationID = 0;

    public int getID() { return ID; }
	public void setID(int id) { ID = id; }

    public String getName() { return Name; }
	public void setName(String name) { Name = name; }
	
	public String getIcon() { return Icon; }
	
	public DeviceCommunicationMethod getCommunicationMethod() {	return CommunicationMethod;	}
	public void setCommunicationMethod(DeviceCommunicationMethod communicationMethod) {	CommunicationMethod = communicationMethod; }
	public List<Signal> getSignals() {	return Signals;	}
	
    public int getSignalSourceID()
    {
    	if (SignalSourceID == 0)
    		return ID;
    	return SignalSourceID;
    }
	public void setSignalSourceID(int id) { SignalSourceID = id; }	
	
    public int getSignalDestinationID()
    {
    	if (SignalDestinationID == 0)
    		return ID;
    	return SignalDestinationID;
    }
	public void setSignalDestinationID(int id) { SignalDestinationID = id; }	
	
	public Device(int id)
	{
		ID = id;
	}	
}
