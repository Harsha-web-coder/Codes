def count_substring(string, sub_string):
    res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]

    n=len(res)
    count=0
    for i in range(n):
        if res[i]==sub_string:
            count+=1
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

"""
Sample Input

ABCDCDC
CDC

Sample Output

2
"""
