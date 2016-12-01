package com.appserver.data;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import com.appserver.models.Device;

import Utils.JsonEntity;
import Utils.Queue.AppServerQueue;
import Utils.Queue.AppServerRequest;


public class ServiceContext
{
	public String[] getDeviceLogs(Device device, int pageIndex, int pageSize) throws IOException, TimeoutException
	{
		AppServerQueue queue = new AppServerQueue();
		String responseQueue = queue.createQueue();
		
		AppServerRequest request = new AppServerRequest(JsonEntity.toJson(device,Device.class),
														pageIndex,
														pageSize,
														responseQueue
														);
		AppServerQueue.PostRequest("log", request);
		
		return null;
	}
}
