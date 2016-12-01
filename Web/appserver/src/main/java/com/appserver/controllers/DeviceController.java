package com.appserver.controllers;

import static spark.Spark.get;
import static spark.Spark.post;
import static spark.Spark.put;


import com.appserver.data.DbContext;
import com.appserver.data.ServiceContext;
import com.appserver.models.Device;

import Utils.JsonEntity;
import Utils.JsonTransformer;

public class DeviceController extends BaseController
{
    public DeviceController(DbContext dbContext,ServiceContext serviceContext)
    {
		super(dbContext,serviceContext);
		// TODO Auto-generated constructor stub
	}

	@Override
    protected void setupEndPoints()
    {
		//TODO Add 201 http response as an output
        post(getApiContext() + "/devices", "application/json", (request, response) -> dbContext.addDevice(Device.class.cast( JsonEntity.fromJson(request.body(),Device.class) )), new JsonTransformer());
 
        get(getApiContext() + "/devices/:id", "application/json", (request, response) -> dbContext.getDevice(Integer.parseInt(request.params(":id"))), new JsonTransformer());
 
        get(getApiContext() + "/devices", "application/json", (request, response) -> dbContext.getDevices(), new JsonTransformer());
 
        put(getApiContext() + "/devices/:id", "application/json", (request, response) -> dbContext.putDevice(Integer.parseInt(request.params(":id")), Device.class.cast(JsonEntity.fromJson(request.body(),Device.class))), new JsonTransformer());
    }
}
