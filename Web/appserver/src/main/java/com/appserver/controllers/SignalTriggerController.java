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

public class SignalTriggerController extends BaseController
{
	public SignalTriggerController(DbContext dbContext) {
		super(dbContext);
		// TODO Auto-generated constructor stub
	}

	@Override
    protected void setupEndPoints()
    {
        get(getApiContext() + "/triggersignal/:id", "application/json",
        	(request, response) -> PostToQueue( Integer.parseInt(request.params(":id")) ),
        	new JsonTransformer());
        
        //TODO Add 201 http response as an output
        post(getApiContext() + "/triggersignal", "application/json",
        		(request, response) ->
       			PostToQueue(Signal.class.cast(JsonEntity.fromJson(request.body(),Signal.class))),
        		new JsonTransformer());
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
		
		ConnectionFactory factory = new ConnectionFactory();
	    factory.setHost("localhost");
	    Connection connection = null;
	    Channel channel = null;
	    
	    try
	    {
		    connection = factory.newConnection();
		    channel = connection.createChannel();
		    
	    	channel.queueDeclare("smart_akome:"+device.getSignalDestinationID(), false, false, false, null);
	    	
	    	JsonTransformer json = new JsonTransformer();
	        String message = json.render(signal);
	        channel.basicPublish("", "smart_akome:"+device.getSignalDestinationID(), null, message.getBytes());
	        
	        return message.length();
	    } catch (IOException e) {
	    	return 0;
		} catch (TimeoutException e) {
			return 0;
		}
	    finally
	    {
	    	if (channel !=null)
				try {
					channel.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (TimeoutException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	        if (connection != null)
				try {
					connection.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	    }
	}
}
