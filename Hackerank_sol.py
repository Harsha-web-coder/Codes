def solve(s):
    fn,ln = s.split(" ")
    a=fn[0].upper()
    b=ln[0].upper()
    A=a+fn[1:]
    B=b+ln[1:]
    C=A+" "+B
    print(C)
if __name__ == '__main__':
    s = input()
    result = solve(s)
