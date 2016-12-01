package Utils;

import java.io.FileReader;
import java.io.IOException;

import java.lang.reflect.Type;

import com.google.gson.Gson;

public class JsonReader {
	public static <T> T readFromFile(String fpath, Type typeOfT) throws IOException
	{
		Gson gson = new Gson();
		FileReader fileReader = null;
    	try    
    	{
    		fileReader = new FileReader(fpath);
    		
    		return gson.fromJson(fileReader, typeOfT);	
    	}
    	finally
    	{
    		if (fileReader != null) fileReader.close();
    	}
	}
}
