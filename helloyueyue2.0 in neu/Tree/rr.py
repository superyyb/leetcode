
def f(n):
    if n==0:
        return 1
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum

def main():
    i=6
    res=f(i)
    print(res)

if __name__ == "__main__":
    main()