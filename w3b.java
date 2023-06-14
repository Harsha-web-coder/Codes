import java.util.*;
class w3b
{
	public static void main(String args[])
	{
		int a,b,c,ch;
		String cha;
		Scanner s = new Scanner(System.in);
		System.out.print("Enter the A value :");
		a=s.nextInt();
		System.out.print("Enter the B value :");
		b=s.nextInt();
		do
		{
			System.out.println("1.add\n 2.sub\n");
			System.out.print("Enter Your choice:");
			ch =s.nextInt();
			switch(ch)
			{
				case 1:
				c=a+b;
				System.out.println("The sum is "+c);
				break;
				case 2:
				c=a-b;
				System.out.println("The differnce is  "+c);
				break;
				default:
				System.out.println("Entered wrong choice");
				break;
			}
			System.out.print("Would you like to continue?");
			cha =s.next();
		}while(cha.equalsIgnoreCase("y"));
	}
}
