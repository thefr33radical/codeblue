/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Count_Sort
{
	public static void main (String[] args) throws java.lang.Exception
	{ int arr[]=new int[]{2,45,1,6,8};
		
	int count[]=new int[10];
	int output[]=new int[5];
	
	for(int i=0;i<10;i++)
		count[i]=0;
	
		
		for(int i=0;i<arr.length;i++)
		{
			count[arr[i]]++;
		}
		
		for(int i=1;i<10;i++)
		{
			count[i-1]+=count[i];
		}
	
			
		for(int i=0;i<arr.length;i++)
		{
			output[i]=count[arr[i]]-1;
			count[arr[i]]--;
		}
		
		
		
		
		
	}
}