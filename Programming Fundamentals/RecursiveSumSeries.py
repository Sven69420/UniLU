def sum_series(n):
    """Function that gives back the sum of the series from 1 to n."""
    if n == 0:
        return 0
    else:
        return n + sum_series(n - 1)

print(sum_series(5))
