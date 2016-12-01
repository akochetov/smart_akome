package Utils.Queue;

public class AppServerRequest
{
	public String requestBody;
	public int pageIndex;
	public int pageSize;
	
	public String responseQueue;
	
	public AppServerRequest(String requestBody, int pageIndex, int pageSize,
			String responseQueue) {
		super();
		this.requestBody = requestBody;
		this.pageIndex = pageIndex;
		this.pageSize = pageSize;
		this.responseQueue = responseQueue;
	}
}
