using System;
public class Practice1
{
    public record Point(int X, int Y);
    public static void Main()
    {
        String s="gamers";
        Console.WriteLine ("Hello"+s);
        s="coders";
        Console.WriteLine($"Hello {s}");
        Console.WriteLine(s.Length);
        String st="    Hello World      ";
        Console.WriteLine($"start{st}end");
        String trimst=st.TrimStart();
        Console.WriteLine($"start{trimst}end");
        trimst=st.TrimEnd();
        Console.WriteLine($"start{trimst}end");
        trimst=st.Trim();
        Console.WriteLine($"start{trimst}end");
        s=s.Replace("coders","Hackers");
        Console.WriteLine($"Hello {s}");
        Console.WriteLine(s.ToLower());
        Console.WriteLine(s.ToUpper());
        String sb="Hello I am a Developer";
        Console.WriteLine(sb.Contains("not"));
        Console.WriteLine(sb.StartsWith("Hello"));
        Console.WriteLine(sb.EndsWith("Developer"));
        int max=int.MaxValue;
        int min=int.MinValue;
        Console.WriteLine($"min {min} max {max}");
        double a = 19;
        double b = 23;
        double c = 8;
        double d = (a + b) / c;
        Console.WriteLine(d);
        double maxi = double.MaxValue;
        double mini = double.MinValue;
        Console.WriteLine($"The range of double is {mini} to {maxi}");
        decimal minimum = decimal.MinValue;
        decimal maximum = decimal.MaxValue;
        Console.WriteLine($"The range of the decimal type is {minimum} to {maximum}");
        double aa = 1.0;
        double bb = 3.0;
        Console.WriteLine(aa / bb);
        
        decimal cc = 1.0M;
        decimal dd = 3.0M;
        Console.WriteLine(cc / dd);
        
        double radius=2.50;
        double area=radius*radius*Math.PI;
        Console.WriteLine($"Circle {area} and {Math.PI}");
        
        Point p1=new Point(2,3);
        Console.WriteLine(p1);
        var p2=p1 with {Y=4};
        Console.WriteLine(p2);

        if(p1==p2)
        
            Console.WriteLine("Equal");
        
        else
        
            Console.WriteLine("Not Equal");

        int count = 0;
        while (count < 10)
        {
            Console.WriteLine(count);
            count++;
        }

        do
        {
            Console.WriteLine(count);
            count++;
        } while (count < 15);

        for(int i = 0; i < 5; i++)
        {
            Console.WriteLine(i);
        }
        
    }
}