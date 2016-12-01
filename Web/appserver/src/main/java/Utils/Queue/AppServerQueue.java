package Utils.Queue;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.concurrent.TimeoutException;

import com.appserver.models.Device;
import com.appserver.models.Signal;

import Utils.JsonTransformer;

public class AppServerQueue
{
	BaseQueue queue = null;
			
	public AppServerQueue()
	{
		queue = QueueFactory.getInstance(QueueType.RabbitMQ);
	}
			
	private static void PostRaw(String destination,String message)
	{
		//TODO	Add queue selection basing on config file contents
		BaseQueue queue = QueueFactory.getInstance(QueueType.RabbitMQ);
		queue.post(AppServerQueueDestination.build(destination), message.getBytes());
	}

	public static void PostDeviceSignal(Device device,Signal signal)
	{
    	JsonTransformer json = new JsonTransformer();
        String message = json.render(signal);
		PostRaw(Integer.toString(device.getSignalDestinationID()), message);
	}
	
	public static void PostText(int destination,String message)
	{
		PostText(Integer.toString(destination), message);
	}

	public static void PostText(String destination,String message)
	{
		Signal signal = new Signal(0,Integer.parseInt(destination));
		byte[] bytes = message.getBytes();
		long[] longs = new long[bytes.length];
		for (int i=0;i<bytes.length;i++)
			longs[i]=bytes[i];
		signal.setPattern(longs);
		JsonTransformer json = new JsonTransformer();
		String messageString = json.render(signal);
		PostRaw(destination, messageString);
	}
	
	public static void PostRequest(String destination,AppServerRequest request)
	{
    	JsonTransformer json = new JsonTransformer();
        String message = json.render(request);   
        
        PostRaw(destination, message);
	}
	
	public String createQueue() throws IOException, TimeoutException
	{
		return queue.createAndConnect();
	}
	
	public String readMessage(String queue) throws UnsupportedEncodingException
	{
		byte[] body = this.queue.get(queue);
		return new String(body, "UTF-8");
	}
}
