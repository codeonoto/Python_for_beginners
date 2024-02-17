# Store key-value pairs

# number = {"john": 3434, "ria": 34234, "joy": 123213}

# Properties:
# Ordered
# Changeable
# Unindexed
# Duplicates not allowed
# Any Datatype

# Creating a dictinory
phones = {"john": 3434, "ria": 34234, "joy": 123213}

print(phones)

# Access item of dict
print(phones["john"])
print(phones.get("john"))

print(phones.keys())

# update value in dict
phones["john"] = 1111
print(phones)

# adding
phones["kia"] = 12123
print(phones)

