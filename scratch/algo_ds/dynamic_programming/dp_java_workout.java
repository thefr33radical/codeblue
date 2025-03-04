
public class Main
{   public static void kadane(int[] data)
    {
        int start_index=0, end_index=0,cur_total=0,max_total=0;
        
        for(int i=0; i <data.length;i++)
        {
            cur_total+=data[i];
            
            //Reject values less than zero
            if(cur_total < 0)
            {
                cur_total=0;
                start_index=i+1;
            }
            // if present total is +ve
            if(cur_total>max_total)
            {
                max_total=cur_total;
                end_index=i;
            }
        }
        System.out.println("start  "+start_index+" end :"+end_index+" Sum :"+max_total);
        return;
    }
	public static void main(String[] args) {
		System.out.println("Hello World");
		int[] a={2,3,4,5};
		kadane(a);
		
	}
}
