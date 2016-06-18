package com.appserver.models;

public abstract class EntityBase {
	public abstract int getID();
	public abstract void setID(int ID);
	
	@Override
	public int hashCode()
	{
		return getID();
	}

	@Override
	public boolean equals(Object obj)
	{
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EntityBase other = (EntityBase) obj;
		if (getID() != other.getID())
			return false;
		return true;
	}
}
