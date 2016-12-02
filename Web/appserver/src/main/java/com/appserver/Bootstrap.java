package com.appserver;

import static spark.Spark.setIpAddress;
import static spark.Spark.setPort;
import static spark.SparkBase.externalStaticFileLocation;

import java.io.IOException;
import java.util.Iterator;

import com.appserver.controllers.ConfigController;
import com.appserver.controllers.DeviceController;
import com.appserver.controllers.DeviceLogController;
import com.appserver.controllers.SignalTriggerController;
import com.appserver.data.DbContext;
import com.appserver.data.ServiceContext;
import com.appserver.models.User;
import com.appserver.models.Config;

import Utils.Settings;
import Utils.Queue.AppServerQueue;

public class Bootstrap {

	@SuppressWarnings("static-access")
	public static void main(String[] args) throws IOException
	{ 
		Settings.get().Init("appserver.config");
		
    	setIpAddress(Settings.get().getIPAddress());
        setPort(Settings.get().getPort());
        externalStaticFileLocation(Settings.get().getResourceRoot());
    	
        //setup routes and controllers
        DbContext dbContext = new DbContext(Settings.get().getDBPath());
        ServiceContext serviceContext = new ServiceContext();
        new DeviceLogController(dbContext,serviceContext);
        new DeviceController(dbContext,serviceContext);
        new SignalTriggerController(dbContext,serviceContext);
        new ConfigController(dbContext,serviceContext,Settings.get().getDispatcherID());

	//add single user in this implementation
	dbContext.getUsers().add(new User(1,
			Settings.get().getUser(),
			Settings.get().getSalt(),
			Settings.get().getHashedPassword()));

	//activate devices mode
	for(Iterator<Config> i = dbContext.getConfigs().iterator(); i.hasNext(); )
		{
			Config c = i.next();
			if (c.isActive())
				AppServerQueue.postText(Settings.get().getDispatcherID(),c.getConfigFile());
		}
	}

}
