package com.appserver.controllers;

import com.appserver.data.DbContext;

public abstract class BaseController
{
    protected final DbContext dbContext;
    
	private static final String API_CONTEXT = "/api";

	public BaseController(DbContext dbContext)
	{
		this.dbContext = dbContext;   
		setupEndPoints();
	}
	
	public String getApiContext()
	{
		return API_CONTEXT;
	}
	
	protected abstract void setupEndPoints();
}
