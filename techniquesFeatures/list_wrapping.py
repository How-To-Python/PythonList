'''
# Python List Wrapping Technique Demonstration
====================================

List wrapping is a technique used to ensure uniform handling of data structures, 
especially when dealing with lists that may vary in their nesting levels. It wraps
a single flat list into another list, creating a nested structure. This is 
particularly useful when you want to process lists of items that could
either be a single flat list or multiple nested lists.


Key Benefits of List Wrapping:
- Ensures consistent structure for processing
- Avoids mismatched pairs in iteration
- Simplifies downstream logic
'''

print("=" * 60)
print("PYTHON LIST WRAPPING DEMONSTRATION")
print("=" * 60)


# =======================================================================
# 1. BASIC LIST WRAPPING
# =======================================================================
print("\n================= 1. Basic List Wrapping ===================")

# Original flat list
colors = ["purple", "blue", "green"]
print("Original flat list:")
print(colors)# ["purple", "blue", "green"]
print("------------------------------------------------------------")

# Wrap the flat list into a nested list
colors_nested_list = [colors]
print("Wrap list into a nested list:")
print(colors_nested_list)# [['red', 'blue', 'green']]
print("------------------------------------------------------------")
# Wrap two flat lists into a nested list
user_names = ["James", "Anna", "Robert"]
user_names_nested_list = [user_names, colors]
print("Wrap two list into a nested list:")
print(user_names_nested_list)# [['James', 'Anna', 'Robert'], ['purple', 'blue', 'green']]
print("------------------------------------------------------------")

# =============================================================================
# 2. LIST WRAPPING IN ZIPPING: Demonstrating the importance of list wrapping in zipping
# =============================================================================
print("\n============== 2. List Wrapping in Zipping =================")
# Original data
category_names = ["Fruits"]
category_items = ["apple", "banana", "orange"]  # Flat list

'''Zip Without List Wrapping Technique
    - Only one tuple is created because category_names has only one element
    - To handle this, we can use the List Wrapping Technique
'''
# Without list wrapping, zipping would lead to incorrect associations and would NOT work correctly
wrong_category_zip_pairs = zip(category_names, category_items)
# zip pairs: ("Fruits", "apple"), ("banana", None), ("orange", None)
# Each item becomes a separate pair
print("❌ Zip Without List Wrapping:")
print(list(wrong_category_zip_pairs))# [('Fruits', 'apple')]
print("------------------------------------------------------------")


'''Zip With List Wrapping Technique
    - Prevents errors in processing loops
    - Facilitates scalability for future categories
    - Ensures consistent data structure for all categories
'''
# With list wrapping, zipping works correctly
correct_zip_pairs = zip(category_names, [category_items])
# prints category name with entire list of items pairs
print("✅ Zip With List Wrapping:")
print(list(correct_zip_pairs))# [('Fruits', ['apple', 'banana', 'orange'])]
print("------------------------------------------------------------")


# Example usage in a processing loop
print("\n==== 3. List Wrapping when Zipping in a processing loop ====")

'''Zip Without List Wrapping Technique in a processing loop
    - Leads to incorrect processing of items
    - Each item is treated as a separate entity
    - Results in unexpected output
'''
print("❌ Zip Without List Wrapping(processing loop):")
# This would NOT work correctly without list wrapping
for category_name, items in zip(category_names, category_items):
    print(f"'{category_name}': {', '.join(items)}")
    # Output: 'Fruits': a, p, p, l, e
print("------------------------------------------------------------")


'''Zip With List Wrapping Technique in a processing loop
    - Works correctly with list wrapping
    - Each category name is paired with its full list of items
    - Produces expected output
'''
print("✅ Zip With List Wrapping(processing loop):")
# This works correctly with list wrapping:
for category_name, items in zip(["Fruits"], [["apple", "banana", "orange"]]):
    print(f"'{category_name}': {', '.join(items)}")
    # Output: 'Fruits': apple, banana, orange
print("-------------------------------------------------------------")
