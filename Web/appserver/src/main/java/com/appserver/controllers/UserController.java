package com.appserver.controllers;

import com.appserver.data.DbContext;
import com.appserver.models.User;

import org.mindrot.jbcrypt.*;

public class UserController extends BaseController
{
    public UserController(DbContext dbContext)
    {
		super(dbContext);
		// TODO Auto-generated constructor stub
	}

	@Override
    protected void setupEndPoints()
    {
	//no action is performed here
    }

    // Authenticate the user by hashing the inputted password using the stored salt,
    // then comparing the generated hashed password to the stored hashed password
    public boolean Authenticate(String username, String password) {
        if (username.isEmpty() || password.isEmpty()) {
            return false;
        }
        User user = dbContext.getUserByUsername(username);
        if (user == null) {
            return false;
        }
        String hashedPassword = BCrypt.hashpw(password, BCrypt.gensalt(8));
        return hashedPassword.equals(user.getHashedPassword());
    }
}
