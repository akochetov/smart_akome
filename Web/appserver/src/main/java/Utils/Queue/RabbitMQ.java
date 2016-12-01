package Utils.Queue;

import java.io.IOException;
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
	public byte[] get(String queue)
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
	    	GetResponse response = ch.basicGet(queue, false);	   
	    	return response.getBody();
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
	    } catch (IOException e) {
	    	return;
		} catch (TimeoutException e) {
			return;
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
	public String createAndConnect() throws IOException, TimeoutException {
	    factory.setHost(getHost());
	    connection = factory.newConnection();
	    channel = connection.createChannel();
		return channel.queueDeclare().getQueue();
	}

	@Override
	public void connect(String queue) throws IOException, TimeoutException {
	    factory.setHost(getHost());
	    connection = factory.newConnection();
	    channel = connection.createChannel();
		channel.queueDeclare(queue, false, false, false, null);
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
