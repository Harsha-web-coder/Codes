def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:len(prefix) - 1]
            if not prefix:
                return ""
    
    return prefix

# Prompt the user to enter a list of strings
strs = input("Enter a list of strings (separated by commas): ").split(",")

# Strip whitespace from each string in the list
strs = [s.strip() for s in strs]

# Call the function to find the longest common prefix
result = longest_common_prefix(strs)

# Print the result
print("Longest common prefix: ", result)