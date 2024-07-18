# Initialize an empty result dictionary
result = {}

# Check if the item's value is not in the result dictionary
item = "key1"
value = "value1"
if value not in result.values():
    # Add the key-value pair into the result dictionary
    result[item] = value

# Print the updated result dictionary
print(result)
