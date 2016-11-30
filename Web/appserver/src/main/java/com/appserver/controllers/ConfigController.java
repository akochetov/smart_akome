package com.appserver.controllers;

import static spark.Spark.get;
import static spark.Spark.post;
import static spark.Spark.put;


import com.appserver.data.DbContext;
import com.appserver.models.Config;
import com.appserver.data.UserDTO;

import Utils.JsonEntity;
import Utils.JsonTransformer;
import Utils.Queue;

public class ConfigController extends BaseController
{
	private int DispatcherID = 0;

    public ConfigController(DbContext dbContext,int dispatcherID)
    {
		super(dbContext);
		DispatcherID = dispatcherID;
	}

	@Override
    protected void setupEndPoints()
    {
		//TODO Add 201 http response as an output
     
        get(getApiContext() + "/configs/:id", "application/json", (request, response) -> dbContext.getConfig(Integer.parseInt(request.params(":id"))), new JsonTransformer());
 
        get(getApiContext() + "/configs", "application/json", (request, response) -> dbContext.getConfigs(), new JsonTransformer());
 
        put(getApiContext() + "/configs/:id", "application/json",
		(request, response) -> Activate(Integer.parseInt(request.params(":id")),UserDTO.class.cast(JsonEntity.fromJson(request.body(),UserDTO.class))),
		new JsonTransformer());
    }

	public Config Activate(int id, UserDTO userdto)
	{
		Config res = dbContext.putConfig(id,userdto);
		Queue.Post(DispatcherID,res.getConfigFile());
		return res;
	}
}
