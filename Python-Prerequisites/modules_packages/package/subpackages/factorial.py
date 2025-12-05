
def fact(n):
    """Calculate the factorial of a number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
