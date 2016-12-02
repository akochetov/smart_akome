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
	abstract public byte[] get(String queue, int timeout_sec);
	public byte[] get(String queue) {return get(queue,0);};
	abstract public void post(String queue, byte[] body);
	abstract public void post(byte[] body) throws IOException;
	abstract public void connect(String queue, int timeout_sec) throws IOException, TimeoutException;
	public void connect(String queue) throws IOException, TimeoutException {connect(queue,0);}
	abstract public void close();
}
