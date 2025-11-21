def sol():
    n = int(input())
    if n == 1:
        return 3
    elif n == 2:
        return 7
    else:
        D = [0 for _ in range(n+1)]
        D[1] = 3
        D[2] = 7
        for i in range(3, n+1):
            D[i] = 2*D[i-1]%9901 + D[i-2]%9901

        return D[n] % 9901


if __name__ == '__main__':
    print(sol())
