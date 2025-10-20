# Basic try-except structure
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    #except TypeError:
        #return "Error: Please provide numbers only"
    except Exception as e:
        return f"An unexpected error occurred: {e}" 

# Testing error handling
print(safe_divide(10, 2))    # Returns 5.0
print(safe_divide(10, 0))    # Returns error message
print(safe_divide("10", 2))  # Returns error message
 


