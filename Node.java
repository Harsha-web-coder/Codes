package unit1;
class Node
{
	String ename;
	String eid;
	String edepartment;
	int esalary;
	Node next;
	Node(String ename,String eid,String edepartment,int esalary)
	{
		this.ename=ename;
		this.eid=eid;
		this.edepartment=edepartment;
		this.esalary=esalary;
		this.next=null;
	}
	
}

public class StuList {
	Node head=null;
	void insert(String ename,String eid,String edepartment,int esalary)
	{
		Node newnode=new Node(ename,eid,edepartment,esalary);
		if(head==null)
		{
			head=newnode;
		}
		else
		{
			Node t=head;
			while(t.next!=null)
			{
				t=t.next;
			}
			t.next=newnode;
			}
		}
	
	void disp()
	{
		Node t=head;
		while(t.next!=null)
		{
			System.out.println(t.ename+"  "+t.eid+"  "+t.edepartment+"  "+t.esalary);
			t=t.next;
		}
		System.out.println(t.ename+"  "+t.eid+"  "+t.edepartment+"  "+t.esalary);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		EmpList sl=new EmpList();
		sl.insert("ravi", "1123","java", 9000);
		sl.insert("pavan", "1912","python", 8054);
		sl.insert("kumar", "1842","Digital", 9904);
		sl.disp();
		sl.insert("sai", "1616","maths", 6500);
		sl.insert("naveen", "5432","science", 4097);
		sl.disp();

	}

}