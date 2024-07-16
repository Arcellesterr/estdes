# Initialize the dictionary
old_hashes_valid = {}

# Add entries to the dictionary
old_hashes_valid['hash1'] = True
old_hashes_valid['hash2'] = False

# Check if a specific hash is valid
hash_to_check = 'hash1'
if hash_to_check in old_hashes_valid:
    is_valid = old_hashes_valid[hash_to_check]
    print(f"Hash {hash_to_check} is valid: {is_valid}")
else:
    print(f"Hash {hash_to_check} not found in the dictionary.")

# Update the validation status of an existing hash
old_hashes_valid['hash1'] = False

# Remove an entry from the dictionary
del old_hashes_valid['hash2']

# Iterate over the dictionary
for hash_value, is_valid in old_hashes_valid.items():
    print(f"Hash: {hash_value}, Valid: {is_valid}")
