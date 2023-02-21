import java.util.*;

class Rodcutting_recur{
static int cutRod(int p[],int n){
if(n==0){
return 0;
}
int q=Integer.MIN_VALUE;
for(int i=1;i<=n;i++){
q=Math.max(q,p[i]+cutRod(p,n-i));
}
return q;
}


public static void main(String[] args){
int p[]=new int[]{0,1,5,8,9,10,17,17,20,24,30};
Scanner sc=new Scanner(System.in);
int n=4;
int maxprofit=cutRod(p,n);
System.out.println(maxprofit);
}
}