class Singleton{
    private static Singleton obj;
    private Singleton(){}
    
    public static Singleton getInstance(){
        if(obj==null)
        {
            obj= new Singleton();
        }
        
        return obj;
    }
    
    
}
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        Singleton x= Singleton.getInstance();
          System.out.println("Hello, World!"); 
    }
}
