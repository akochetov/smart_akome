package com.appserver.controllers;

import com.appserver.data.DbContext;
import com.appserver.data.ServiceContext;

public abstract class BaseController
{
    protected final DbContext dbContext;
    protected final ServiceContext serviceContext;
    
	private static final String API_CONTEXT = "/api";

	public BaseController(DbContext dbContext,ServiceContext serviceContext)
	{
		this.dbContext = dbContext;   
		this.serviceContext = serviceContext;   
		setupEndPoints();
	}

	public String getApiContext()
	{
		return API_CONTEXT;
	}
	
	protected abstract void setupEndPoints();
}
