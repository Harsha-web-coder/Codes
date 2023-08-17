/*that, given a positive integer N, 
prints the consecutive numbers from 1 to N, each on a separate line. 
However, any number which is a power of 2 should be replaced by the word PowER. 
For example, number 4 should be replaced by pOWEr, but number 5 should not. 
The function shouldn't return any value.
Examples:
Given N = 7, the function should print
POWER
POWER
3
POWER
5
6
7
Given N= 16, the function should print:
N=16

POWER
POWER
3
POWER
5
6
7
POWER
9
10
11
12
13
14
15
POWER

Etc..
*/
//2*2=4

function hello(N){
    for( let i=1;i<=N;i++ ){     
        
        if( (i & (i-1)) === 0 ){
            console.log("POWER");
        }
        else{
            console.log(i);
        }
    }

}
/*
//&&-logical AND
//&-Bitwise AND
const N = 7;
hello(N);

^-1-0-0

1 & 0 === 0
0 & 1 === 0
0 & 0 === 0
1 & 1 === 1
8 4 2 1
->0 0 1 1->3
->0 1 0 0->4
->0 0 0 0->0

->
4&5
->
0 1 0 0
0 1 0 1
->0 1 0 0
*/