def reverse_string(input_string):
    # Convert the string into a list
    string_list = list(input_string)
    
    # Reverse the list
    string_list.reverse()
    
    # Convert the list back to a string
    reversed_string = ''.join(string_list)
    
    return reversed_string

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
