package Utils;

import static spark.Spark.post;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;

import com.appserver.models.Device;
import com.appserver.models.Signal;

import com.rabbitmq.client.Channel;

import Utils.JsonEntity;
import Utils.JsonTransformer;

public class Queue
{
	private static int PostRaw(int destination,String message)
	{
		ConnectionFactory factory = new ConnectionFactory();
	    factory.setHost("localhost");
	    Connection connection = null;
	    Channel channel = null;
	    
	    try
	    {
		    connection = factory.newConnection();
		    channel = connection.createChannel();
		    
	    	channel.queueDeclare("smart_akome:"+destination, false, false, false, null);
	        channel.basicPublish("", "smart_akome:"+destination, null, message.getBytes());
	        
		System.out.println("Posted to queue \"smart_akome:"+destination+"\", message \""+message+"\"");		

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

	public static int Post(Device device,Signal signal)
	{
	    	JsonTransformer json = new JsonTransformer();
	        String message = json.render(signal);
		return PostRaw(device.getSignalDestinationID(), message);
	}

	public static int Post(int destination,String message)
	{
		Signal signal = new Signal(0,destination);
		byte[] bytes = message.getBytes();
		long[] longs = new long[bytes.length];
		for (int i=0;i<bytes.length;i++)
			longs[i]=bytes[i];
		signal.setPattern(longs);
	    	JsonTransformer json = new JsonTransformer();
	        String messageString = json.render(signal);
		return PostRaw(destination, messageString);
	}
}
