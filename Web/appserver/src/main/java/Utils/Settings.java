package Utils;

import java.io.FileReader;
import java.util.Properties;

import java.io.IOException;

/*
 * *.config file (standard ini format) reader, singletone for ease of access
 */
public class Settings
{
	private static Settings instance = new Settings();
	
	private static String ip_address;
	private static int port;
    private static String root;
    private static String db_file;
    private static int dispatcherID;
    private static String user;
    private static String salt;
    private static String hashedpassword;
    
    private static int rr_timeout_sec;
	
	public static String getIPAddress(){return ip_address;};
	public static int getPort(){return port;};
	public static String getResourceRoot(){return root;};
	public static String getDBPath(){return db_file;};
	public static int getDispatcherID(){return dispatcherID;};
	public static String getUser(){return user;};
	public static String getSalt(){return salt;};
	public static String getHashedPassword(){return hashedpassword;};
	public static int getRequestResponseTimeoutSec(){return rr_timeout_sec;};
	
	private Settings(){}
	public static Settings get(){return instance;}

	public static void Init(String fpath) throws IOException
	{	
		Properties config = new Properties();
		FileReader fileReader = null;
		
		//read appserver properties from config file
		try    
		{
			fileReader = new FileReader(fpath);
			
			config.load(fileReader);    	
		}
		finally
		{
			if (fileReader != null) fileReader.close();
		}
		
		ip_address = config.getProperty("ip_address");
		port = Integer.parseInt(config.getProperty("port"));
	    root = config.getProperty("root");
	    db_file = config.getProperty("db_file");
	    dispatcherID = Integer.parseInt(config.getProperty("dispatcherID"));
	    user = config.getProperty("user");
	    salt = config.getProperty("salt");
	    hashedpassword = config.getProperty("hashedpassword");
	}
}
