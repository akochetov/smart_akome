package com.appserver.controllers;

import static spark.Spark.post;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import static spark.Spark.get;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.appserver.data.DbContext;

import com.appserver.models.Device;
import com.appserver.models.Signal;

import com.rabbitmq.client.Channel;

import Utils.JsonEntity;
import Utils.JsonTransformer;
import Utils.Queue;

public class SignalTriggerController extends BaseController
{
	public SignalTriggerController(DbContext dbContext) {
		super(dbContext);
		// TODO Auto-generated constructor stub
	}

	@Override
    protected void setupEndPoints()
    {
        get(getApiContext() + "/triggersignal/:id", "application/json", (request, response) -> PostToQueue( Integer.parseInt(request.params(":id")) ),new JsonTransformer());
        
        //TODO Add 201 http response as an output
        post(getApiContext() + "/triggersignal", "application/json",(request, response) -> PostToQueue(Signal.class.cast(JsonEntity.fromJson(request.body(),Signal.class))), new JsonTransformer());
    }
	
	private int PostToQueue(int signalId)
	{	
		Signal signal = dbContext.getSignal(signalId);
		return PostToQueue(signal);
	}
	
	private int PostToQueue(Signal signal)
	{
		//find associated device first
		Device device = dbContext.getDevice(signal.getDeviceID());
		if (device == null)
			return 0;
		return Queue.Post(device,signal);
	}
}
