
/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;




public interface Publisher
{
	
	public void register(Observer o);
	public void deRegister(Observer o);
	public void notify();
	
}

public interface Observer
{

	public void update(int var1, int var2);
}

public class WeatherStation implements Publisher
{
	private List<Observer> observers;
	
	Publishers()
	{this.observers = new ArrayList<>();
	}
	
	@overrirde
	public void register(Observer o)
	{
		observers.add(o);
	}
	
	
	@overrirde
	public void deregister(Observer o)
	{
		int index = observers.indexOf(o);
		if(index >=0)
		{
			observers.remove(o);
		}
	}
	
	@override
	public void notify(){
		
		// for i in observsers  notify call o.update
	}
	
	
}

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	}
}
