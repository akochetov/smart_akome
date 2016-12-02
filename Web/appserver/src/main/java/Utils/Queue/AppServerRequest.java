package Utils.Queue;

public class AppServerRequest
{
	public String requestBody;
	public int pageIndex;
	public int pageSize;
		
	public String responseQueue;
	public int responseTTL;
	
	public AppServerRequest(String requestBody, int pageIndex, int pageSize,
			String responseQueue, int responseTTL) {
		super();
		this.requestBody = requestBody;
		this.pageIndex = pageIndex;
		this.pageSize = pageSize;
		this.responseQueue = responseQueue;
		this.responseTTL = responseTTL;
	}
}
