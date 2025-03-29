// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Counter
{
    private int cnc =0;

    public synchronized void inc()
    {
        this.cnc++;

    }

    public int get()
    {
        return cnc;
    }

    }
class Main {


   
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");

        Counter a  = new Counter();

        Thread t1 = new Thread(() -> {
        for(int i =0; i< 10; i++)
        {
            a.inc();
        } });

        Thread t2 = new Thread(() -> {
            for(int j=0; j<10;j++)
            {
                a.inc();
            }
        });

        t1.start();
        t2.start();

        try{

            t1.join();
            t2.join();

        }
        catch (InterruptedException e)
        { e.printStackTrace();}

        System.out.println("Counter: " + a.get());

    }
}