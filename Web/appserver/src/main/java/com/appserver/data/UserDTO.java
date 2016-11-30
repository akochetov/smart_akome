package com.appserver.data;

/**
 * User DTO entity
 */
public class UserDTO
{
    public int ID;
  
    public String Username;
    public String Password;

    public UserDTO(int id, String username, String password)
    {
	ID = id;
	Username = username;
	Password = password;
    }
}
