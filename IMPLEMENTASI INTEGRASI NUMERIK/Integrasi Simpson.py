import time

def f(x):
    return 4 / (1 + x**2)

def simpson_one_third_integration(a, b, N):
    h = (b - a) / N
    x = [a + i * h for i in range(N + 1)]
    y = [f(x_val) for x_val in x]
    
    integral_sum = y[0] + y[N]  # f(a) + f(b)
    
    # Sum for even indices
    for i in range(1, N, 2):
        integral_sum += 4 * y[i]
    
    # Sum for odd indices
    for i in range(2, N-1, 2):
        integral_sum += 2 * y[i]
    
    integral_sum *= h / 3
    
    return integral_sum

def main():
    a = 0  # Lower limit
    b = 1  # Upper limit
    reference_pi = 3.14159265358979323846
    
    N_values = [10, 100, 1000, 10000]
    
    for N in N_values:
        start_time = time.time()
        integral_result = simpson_one_third_integration(a, b, N)
        end_time = time.time()
        
        error = abs(integral_result - reference_pi)
        
        print(f"For N = {N}:")
        print(f"Integral result: {integral_result}")
        print(f"Error: {error}")
        print(f"Execution time: {end_time - start_time} seconds")
        print()

if __name__ == "__main__":
    main()
