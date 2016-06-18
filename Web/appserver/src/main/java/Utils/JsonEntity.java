package Utils;

import com.google.gson.Gson;

/**
 * Base class, used to read an instance of an object from Json
 */
public class JsonEntity
{
	public static Object fromJson(String json, Class<?> c)
	{
    	Gson gson = new Gson();

 		return gson.fromJson(json, c);		
	}
}
