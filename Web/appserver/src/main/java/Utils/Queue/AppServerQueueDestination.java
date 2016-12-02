package Utils.Queue;

public class AppServerQueueDestination {
	public static String build(String path)
	{
		return "smart_akome:"+path;
	}
	public static String build(String[] pathes)
	{
		StringBuilder sb = new StringBuilder();
		for (int i=0;i<pathes.length;i++)
			sb.append(pathes[i]+":");
		return "smart_akome:"+sb.toString();
	}
}
