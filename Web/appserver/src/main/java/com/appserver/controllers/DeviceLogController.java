package com.appserver.controllers;

import static spark.Spark.get;
import static spark.Spark.post;
import static spark.Spark.put;


import com.appserver.data.DbContext;
import com.appserver.data.ServiceContext;
import com.appserver.models.Device;

import Utils.JsonEntity;
import Utils.JsonTransformer;

public class DeviceLogController extends BaseController
{
	private ServiceContext serviceContext = null;
	
    public DeviceLogController(DbContext dbContext, ServiceContext serviceContext)
    {
    	super(dbContext, serviceContext);
	}

    protected void setupEndPoints()
    {
		//TODO Add 201 http response as an output
        get(getApiContext() + "/device_logs", "application/json",
        		(request, response) -> serviceContext.getDeviceLogs(
        									dbContext.getDevice(Integer.parseInt(request.queryParams("DeviceID"))),
        									Integer.parseInt(request.queryParams("pageIndex")),
        									Integer.parseInt(request.queryParams("pageSize"))
        									),
        		new JsonTransformer());
    }
}
