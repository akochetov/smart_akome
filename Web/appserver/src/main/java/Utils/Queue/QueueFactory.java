package Utils.Queue;

public class QueueFactory {
	public static BaseQueue getInstance(QueueType type)
	{
		if (type == QueueType.RabbitMQ)
			return new RabbitMQ();
		
		throw new java.lang.UnsupportedOperationException();
	}
}
