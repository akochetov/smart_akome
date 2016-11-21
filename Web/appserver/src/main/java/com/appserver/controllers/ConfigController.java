package com.appserver.controllers;

import static spark.Spark.get;
import static spark.Spark.post;
import static spark.Spark.put;


import com.appserver.data.DbContext;
import com.appserver.models.Config;

import Utils.JsonEntity;
import Utils.JsonTransformer;

public class ConfigController extends BaseController
{
    public ConfigController(DbContext dbContext)
    {
		super(dbContext);
		// TODO Auto-generated constructor stub
	}

	@Override
    protected void setupEndPoints()
    {
		//TODO Add 201 http response as an output
     
        get(getApiContext() + "/configs/:id", "application/json", (request, response) -> dbContext.getConfig(Integer.parseInt(request.params(":id"))), new JsonTransformer());
 
        get(getApiContext() + "/configs", "application/json", (request, response) -> dbContext.getConfigs(), new JsonTransformer());
 
        put(getApiContext() + "/configs/:id", "application/json", (request, response) -> dbContext.putConfig(Integer.parseInt(request.params(":id")), Config.class.cast(JsonEntity.fromJson(request.body(),Config.class))), new JsonTransformer());
    }
}
