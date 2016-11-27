package smart_akome.Web.appserver.src.main.java.com.appserver;

import static spark.Spark.setIpAddress;
import static spark.Spark.setPort;
import static spark.SparkBase.externalStaticFileLocation;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import com.appserver.controllers.ConfigController;
import com.appserver.controllers.DeviceController;
import com.appserver.controllers.SignalTriggerController;
import com.appserver.data.DbContext;
import com.appserver.models.User;

public class Bootstrap {

	public static void main(String[] args) throws IOException
	{
		Properties config = new Properties();
    	FileReader fileReader = null;
    	
    	//read appserver properties from config file
    	try    
    	{
    		fileReader = new FileReader("appserver.config");
    		
    		config.load(fileReader);    	
    	}
    	finally
    	{
    		if (fileReader != null) fileReader.close();
    	}
    	
    	setIpAddress(config.getProperty("ip_address"));
        setPort(Integer.parseInt(config.getProperty("port")));
        externalStaticFileLocation(config.getProperty("root"));
    	
        //setup routes and controllers
        DbContext dbContext = new DbContext(config.getProperty("db_file"));
        new ConfigController(dbContext);
        new DeviceController(dbContext);
        new SignalTriggerController(dbContext);

	//add single user in this implementation
	dbContext.getUsers().add(new User(1,config.getProperty("user"),config.getProperty("hashedpassword")));
	}

}
