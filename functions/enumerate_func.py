'''
# Python enumerate() Function
- creates pairs of index and value from an iterable
- a built-in utility that adds a counter to an iterable and returns it as an enumerate object
    1. Pass an iterable (like a list, tuple, or string) to `enumerate()`
    2. Optionally, you can provide a second argument to specify the starting index (default is 0)
    3. The function returns an enumerate object, which yields pairs containing an index and the corresponding item from the iterable
    4. You can convert this enumerate object into a list of tuples or iterate over it directly in a loop
'''



category_names = ["Fruits", "Colors", "Numbers"]




print(enumerate(category_names))# <enumerate object at 0x00000238BB752020>
print(type(enumerate(category_names)))  # Output: <class 'enumerate'>

# enumerate(category_names): Creates pairs of tuples(index, value) for each item in the list
for i, category_name in enumerate(category_names):
    print(f"Category: '{category_name}'")

# Output:
# Category: 'Fruits'
# Category: 'Colors'
# Category: 'Numbers'
# You can also specify a starting index
for index, category_name in enumerate(category_names, start=1):
    print(f"Category {index}: '{category_name}'")
# Output:
# Category 1: 'Fruits'
# Category 2: 'Colors'
# Category 3: 'Numbers'


category_items = [["apple", "banana", "cherry"],
                  ["red", "green", "blue"],
                  [1, 2, 3, 4, 5]]

# Converting enumerate object to a list of tuples
enumerated_list = list(enumerate(category_names))
print(enumerated_list)  # Output: [(0, 'Fruits'), (1, 'Colors'), (2, 'Numbers')]


# Accessing items using the index from enumerate
for i, category_name in enumerate(category_names):
    items = category_items[i]  # Gets the i-th sublist for the i-th category
    print(f"Items in '{category_name}': {items}")
# Output:
# Items in 'Fruits': ['apple', 'banana', 'cherry']  
# Items in 'Colors': ['red', 'green', 'blue']
# Items in 'Numbers': [1, 2, 3, 4, 5]


# Handling cases where the number of categories and item lists differ
for i, category_name in enumerate(category_names):
    if i < len(category_items):
        items = category_items[i]
    else:
        items = []
    print(f"Items in '{category_name}': {items}")
# Output:
# Items in 'Fruits': ['apple', 'banana', 'cherry']  
# Items in 'Colors': ['red', 'green', 'blue']
# Items in 'Numbers': [1, 2, 3, 4, 5]
# Items in 'Animals': []    
# (since there is no corresponding sublist for 'Animals')
category_names.append("Animals")
category_items.append([])
for i, category_name in enumerate(category_names):
    if i < len(category_items):
        items = category_items[i]
    else:
        items = []
    print(f"Items in '{category_name}': {items}")
# Output:
# Items in 'Fruits': ['apple', 'banana', 'cherry']  
# Items in 'Colors': ['red', 'green', 'blue']
# Items in 'Numbers': [1, 2, 3, 4, 5]
# Items in 'Animals': []    # (now correctly shows an empty list for 'Animals')
