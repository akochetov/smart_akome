package com.appserver.models;

import java.util.ArrayList;
import java.util.List;

/**
 * Device entity, representing device able to send or receive signals
 */
public class Device extends EntityBase
{
	private int ID;
	private String Name;
	private DeviceCommunicationMethod CommunicationMethod;
	private String Icon;
	private List<Signal> Signals = new ArrayList<Signal>();

    public int getID() { return ID; }
	public void setID(int id) { ID = id; }

    public String getName() { return Name; }
	public void setName(String name) { Name = name; }
	
	public String getIcon() { return Icon; }
	
	public DeviceCommunicationMethod getCommunicationMethod() {	return CommunicationMethod;	}
	public void setCommunicationMethod(DeviceCommunicationMethod communicationMethod) {	CommunicationMethod = communicationMethod; }
	public List<Signal> getSignals() {	return Signals;	}
	
	public Device(int id)
	{
		ID = id;
	}	
}
