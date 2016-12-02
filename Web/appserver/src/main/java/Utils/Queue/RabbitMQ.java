package Utils.Queue;

import java.io.IOException;
import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeoutException;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.GetResponse;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;

public class RabbitMQ extends BaseQueue
{
	ConnectionFactory factory = new ConnectionFactory();
    Connection connection = null;
    Channel channel = null;
    String queue = null;
    
	@Override
	public byte[] get(String queue, int timeout_sec)
	{
		ConnectionFactory f = new ConnectionFactory();
	    f.setHost(getHost());
	    Connection c = null;
	    Channel ch = null;
	    
	    try
	    {
		    c = f.newConnection();
		    ch = c.createChannel();
		    
		    Map<String, Object> args = new HashMap<String, Object>();	    
		    if(timeout_sec >0)
		    	args.put("x-expires", timeout_sec * 1000);
		    
	    	ch.queueDeclare(queue, false, false, false, args);

	    	Instant time_start = Instant.now();
	    	while (true)
	    	{
	    		GetResponse response = ch.basicGet(queue, true);
	    		if (response != null)
	    		{
	    			//message received
	    		    byte[] body = response.getBody();
	    			return body;
	    		}
	    		
	    		if (timeout_sec > 0)
	    			if (Duration.between(time_start, Instant.now()).toMillis() > timeout_sec*1000)
	    				break;
	    		{
	    			
	    		}
	    	}
	   
	    	return null;
	    } catch (IOException e) {
	    	return null;
		} catch (TimeoutException e) {
			return null;
		}
	    finally
	    {
	    	if (ch !=null)
				try {
					ch.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (TimeoutException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	        if (c != null)
				try {
					c.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	    }		
	}
	
	@Override
	public void post(String queue, byte[] body)
	{
		ConnectionFactory f = new ConnectionFactory();
	    f.setHost(getHost());
	    Connection c = null;
	    Channel ch = null;
	    
	    try
	    {
		    c = f.newConnection();
		    ch = c.createChannel();
		    
	    	ch.queueDeclare(queue, false, false, false, null);
	        ch.basicPublish("", queue, null, body);	
		System.out.println("Posted to queue: "+queue+", data: "+new String(body, "UTF-8"));      
	    } catch (IOException e) {
	    	return;
		} catch (TimeoutException e) {
			e.printStackTrace();
		}
	    finally
	    {
	    	if (ch !=null)
				try {
					ch.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (TimeoutException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	        if (c != null)
				try {
					c.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	    }		
	}

	@Override
	public void post(byte[] body) throws IOException {
		// TODO Auto-generated method stub
		channel.basicPublish("",this.queue, null, body);	
	}

	@Override
	public void connect(String queue, int timeout_sec) throws IOException, TimeoutException {
	    factory.setHost(getHost());
	    connection = factory.newConnection();
	    channel = connection.createChannel();
	    
	    Map<String, Object> args = new HashMap<String, Object>();	    
	    if(timeout_sec >0)
	    	args.put("x-expires", timeout_sec * 1000);
	    
		channel.queueDeclare(queue, false, false, false, args);
		this.queue = queue;
	}

	@Override
	public void close() {
		queue = null;
    	if (channel !=null)
				try {
					channel.close();
					channel = null;
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
					connection = null;
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	}
}
