def fib(n):
    if (n == 1 or n == 2):
        result = 1;
    else:
        result = fib(n - 1) + fib(n - 2);
    return result;

def fib_memo(n, memo):
    if (memo == None):
        memo = [None] * (n + 1);

    if (memo[n] != None):
        return memo[n];

    if (n == 1 or n == 2):
        result = 1;
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
    memo[n] = result;
    return result;

print(fib_memo(100, None));