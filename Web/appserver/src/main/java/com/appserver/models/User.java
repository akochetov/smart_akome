package com.appserver.models;

/**
 * User entity
 */
public class User extends EntityBase
{
    private int ID;
  
    private String Username;
    private String HashedPassword;

    public User(int id, String username, String hashedpassword)
    {
	setID( id );
	setUsername( username );
	setHashedPassword( hashedpassword );
    }

    public int getID() { return ID; }
    public void setID(int id) { ID = id; }

    public String getUsername() { return Username; };
    public void setUsername(String username) { Username = username; };

    public String getHashedPassword() { return HashedPassword; };
    public void setHashedPassword(String hashedpassword) { HashedPassword = hashedpassword; };

	@Override
	public boolean equals(Object obj)
	{
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		User other = (User) obj;
		if (getUsername() != other.getUsername())
			return false;
		return true;
	}
}
