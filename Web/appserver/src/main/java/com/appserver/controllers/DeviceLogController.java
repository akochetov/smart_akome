package com.appserver.controllers;

import static spark.Spark.get;
import static spark.Spark.post;
import static spark.Spark.put;

import java.io.IOException;
import java.util.UUID;
import java.util.concurrent.TimeoutException;

import com.appserver.data.DbContext;
import com.appserver.data.ServiceContext;
import com.appserver.models.Device;

import Utils.JsonEntity;
import Utils.JsonTransformer;
import Utils.Settings;

public class DeviceLogController extends BaseController
{
    public DeviceLogController(DbContext dbContext, ServiceContext serviceContext)
    {
    	super(dbContext, serviceContext);
	}

    protected void setupEndPoints()
    {
		//TODO Add 201 http response as an output
	    get(getApiContext() + "/device_logs/:id", "application/json",
	    		(request, response) -> serviceContext.getDeviceLogs(
	    									dbContext.getDevice(Integer.parseInt(request.params(":id"))),
	    									Integer.parseInt(request.queryParams("pageIndex")),
	    									Integer.parseInt(request.queryParams("pageSize"))
	    									),
	    		new JsonTransformer());
    }
}
