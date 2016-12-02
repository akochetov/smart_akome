package Utils;

import java.io.FileWriter;
import java.io.IOException;

import java.lang.reflect.Type;

import com.google.gson.Gson;

public class JsonWriter {
	public static void writeToFile(Object T, String fpath, Type typeOfT) throws IOException
	{
		Gson gson = new Gson();
		FileWriter fileWriter = null;
    	try    
    	{
    		fileWriter = new FileWriter(fpath);
    		
    		gson.toJson(T, typeOfT, fileWriter);	
    	}
    	finally
    	{
    		if (fileWriter != null) fileWriter.close();
    	}
	}
}
