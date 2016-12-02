package Utils.Queue;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Map;
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
			
	private static void postRaw(String destination,String message)
	{
		//TODO	Add queue selection basing on config file contents
		BaseQueue queue = QueueFactory.getInstance(QueueType.RabbitMQ);
		queue.post(AppServerQueueDestination.build(destination), message.getBytes());
	}

	public static void postDeviceSignal(Device device,Signal signal)
	{
    	JsonTransformer json = new JsonTransformer();
        String message = json.render(signal);
		postRaw(Integer.toString(device.getSignalDestinationID()), message);
	}
	
	public static void postText(int destination,String message)
	{
		postText(Integer.toString(destination), message);
	}

	public static void postText(String destination,String message)
	{
		Signal signal = new Signal(0,Integer.parseInt(destination));
		byte[] bytes = message.getBytes();
		long[] longs = new long[bytes.length];
		for (int i=0;i<bytes.length;i++)
			longs[i]=bytes[i];
		signal.setPattern(longs);
		JsonTransformer json = new JsonTransformer();
		String messageString = json.render(signal);
		postRaw(destination, messageString);
	}
	
	public static void postRequest(String destination,AppServerRequest request)
	{
    	JsonTransformer json = new JsonTransformer();
        String message = json.render(request);   
        
        postRaw(destination, message);
	}
	
	public String readMessage(String queue, int timeout_sec) throws UnsupportedEncodingException
	{
		byte[] body = this.queue.get(queue, timeout_sec);
		return new String(body, "UTF-8");
	}
	
	public String readMessage(String queue) throws UnsupportedEncodingException
	{
		byte[] body = this.queue.get(queue);
		return new String(body, "UTF-8");
	}
	
	public void createQueue(String queue, int timeout_sec) throws IOException, TimeoutException
	{
		this.queue.connect(queue,timeout_sec);
	}
	
	public void close()
	{
		this.queue.close();
	}
}
