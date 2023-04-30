def save_results(capacity):
    def decorator(func):
        results = {}
        def wrapper(n):
            if n not in results:
                results[n] = func(n)
                if len(results) >= capacity:
                    (k := next(iter(results)), results.pop(k))
            return results[n]
        
        return wrapper
    return decorator

@save_results(4)
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# קריאה לפונקציה עבור n=100
result = fibonacci(100)
print(result)