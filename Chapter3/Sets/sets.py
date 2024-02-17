# Sets --> container for storing multiple values in a variable
# names = {"John", "Merry", "Dev"}

# Unordered
# Mutable
# Unindexed
# Duplicate not allowed
# Any Datatype
# Mix of different data type

# creating a set
names = {"John", "Merry", "Dev"}

print(names)

# check length
print(len(names))

print(type(names))

# accessing items of set
for x in names:
    print(x)

# Existense
if "John" in names:
    print("John is in names")

if "Nisha" not in names:
    print("Nisha is not in a names")

# adding
names.add("Riya")
print(names)

# add another sequence in a set
names_list = ["Onoto", "SBlock"]
names.update(names_list)
print(names)

# Removing
names.remove("Merry")
print(names)
# Remove --> it will thorw an error if value is not present in the sets
# so we use discard

names.discard("Ramesh")
print(names)

# Joining 2 sets
s1 = {"a", "b", "c"}
s2 = {"d", "e", "a"}

print(s1, s2)

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

# keep only duplicates while joining
s1.intersection_update(s2)
print(s1)
