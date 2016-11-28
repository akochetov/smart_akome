package com.appserver.models;

import org.mindrot.jbcrypt.*;

/**
 * User entity
 */
public class User extends EntityBase
{
    private int ID;
  
    private String Username;
    private String Salt;
    private String HashedPassword;

    public User(int id, String username)
    {
	setID( id );
	setUsername( username );
    }

    public User(int id, String username, String salt, String hashedpassword)
    {
	setID( id );
	setUsername( username );
	setSalt( salt );
	setHashedPassword( hashedpassword );
    }

    public int getID() { return ID; }
    public void setID(int id) { ID = id; }

    public String getSalt() { return Salt; };
    public void setSalt(String salt) { Salt = salt; };

    public String getUsername() { return Username; };
    public void setUsername(String username) { Username = username; };

    public String getHashedPassword() { return HashedPassword; };
    public void setHashedPassword(String hashedpassword) { HashedPassword = hashedpassword; };


    // Authenticate the user by hashing the inputted password using the stored salt,
    // then comparing the generated hashed password to the stored hashed password
    public boolean Authenticate(String username, String password) {
        if (username.isEmpty() || password.isEmpty()) {
            return false;
        }

        String hashedPassword = BCrypt.hashpw(password, getSalt());
        return hashedPassword.equals(getHashedPassword());
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
		User other = (User) obj;
		if (getUsername() == null)
			return false;
		if (!getUsername().equals(other.getUsername()))
			return false;

		return true;
	}
}
