package Utils.Queue;

public class AppServerQueueDestination {
	public static String build(String path)
	{
		return "smart_akome:"+path;
	}

}
