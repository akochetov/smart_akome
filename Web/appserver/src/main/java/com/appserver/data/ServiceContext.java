package com.appserver.data;

import java.io.IOException;
import java.util.UUID;
import java.util.concurrent.TimeoutException;

import com.appserver.models.Device;

import Utils.JsonEntity;
import Utils.Settings;
import Utils.Queue.AppServerQueue;
import Utils.Queue.AppServerQueueDestination;
import Utils.Queue.AppServerRequest;
import Utils.Queue.AppServerResponse;

public class ServiceContext
{
	public AppServerResponse getDeviceLogs(Device device, int pageIndex, int pageSize)
	{
    	UUID responseQueue = UUID.randomUUID();
    	AppServerQueue queue = new AppServerQueue();
		
    	try
    	{
    		queue.createQueue(responseQueue.toString(), Settings.getRequestResponseTimeoutSec());
			AppServerRequest request = new AppServerRequest(JsonEntity.toJson(device,Device.class),
															pageIndex,
															pageSize,
															responseQueue.toString()
															);
			AppServerQueue.postRequest("service:log", request);
			String result = queue.readMessage(responseQueue.toString(),Settings.getRequestResponseTimeoutSec());
			if (result == null) throw new TimeoutException();
			return (AppServerResponse)JsonEntity.fromJson(result,AppServerResponse.class);
    	} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (TimeoutException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	finally
    	{
    		queue.close();
    	}
		
		return null;
	}
}
