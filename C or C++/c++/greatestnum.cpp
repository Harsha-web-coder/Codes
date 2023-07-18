#include <iostream>  
using namespace std;
void find_greatest(int a, int b, int c, int d)  
{  
    if (a > b) {
        if (a > c) {  
            if (a > d) {  
                cout << "a is greatest";  
            }  
            else {  
                cout << "d is greatest";  
            }  
        }  
    }  
    else if (b > c) {  
        if (b > d) {  
            cout << "b is greatest";  
        }  
        else {  
            cout << "d is greatest";  
        }  
    }  
    else if (c > d) {  
        cout << "c is greatest";  
    }  
    else {  
        cout << "d is greatest";  
    }  
}  
  
int main()  
{  
    int a,b,c,d;
    cin >>a>>b>>c>>d;
    cout << "a=" << a << " b=" << b << " c=" << c << " d=" << d;  
    cout << "\n";  
    find_greatest(a, b, c, d);   
    return 0;  
}
