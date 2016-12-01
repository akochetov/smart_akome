package Utils.Queue;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public abstract class BaseQueue {
	private String host = "localhost";		
	
	public String getHost() {
		return host;
	}
	public void setHost(String host) {
		this.host = host;
	}
	abstract public byte[] get(String queue);
	abstract public void post(String queue, byte[] body);
	abstract public void post(byte[] body) throws IOException;
	abstract public String createAndConnect() throws IOException, TimeoutException;
	abstract public void connect(String queue) throws IOException, TimeoutException;
	abstract public void close();
}
