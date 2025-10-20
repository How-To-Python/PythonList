
'''
data = [
    ["Fruits", "Colors"],
    [
     ["avocado", "pineapple", "plum", "grapes"],  # items for Fruits Category
     ["purple", "blue", "green"]  # items for Colors Category
    ]
'''
def compact_processor(data):
    category_names, category_items = data[0], data[1]
    
    # Handle both single flat list and multiple nested lists
    if not isinstance(category_items[0], list):
        items_lists = [category_items]  # Wrap single list
    else:
        items_lists = category_items    # Use nested lists
    
    # Process each category
    # tuple unpacking with the zip() function to iterate through two lists simultaneously
    # for category_name, items in zip(category_names, items_lists):
        # zip(category_names, items_lists): Combines elements from category_names and items_lists into pairs
            # category_name, items: Unpacks each pair into separate variables
                # category_name gets the category name from category_names
                # items gets the corresponding list of items from items_lists
            # ("Fruits", ["avocado", "pineapple", "plum", "grapes"])
            # ("Colors", ["purple", "blue", "green"])

        # {', '.join(items)}: Joins all items in the list with commas and spaces
            # .join(): Converts a list like ["peach", "pear"] into a string "peach, pear"
        # print(f"'{category_name}': {', '.join(items)}")

    for category_name, items in zip(category_names, items_lists):
        print(f"'{category_name}': {', '.join(items)}")






# **Line 33:** `for category_name, items in zip(category_names, items_lists):`
# - **`zip(category_names, items_lists)`**: Creates paired tuples from both lists simultaneously
# - **`category_name, items`**: Tuple unpacking assigns each pair to separate variables
# - **Synchronized iteration**: Ensures each category name matches its corresponding item list

# **Line 34:** `print(f"'{category_name}': {', '.join(items)}")`
# - **`f"'{category_name}':`**: Formats category name with single quotes
# - **`{', '.join(items)}`**: Joins list items into comma-separated string
# - **`.join()` method**: Converts `["apple", "banana"]` → `"apple, banana"`






# Example usage:
favorites = [
    ["Fruits", "Colors"],
    [
     ["avocado", "pineapple", "plum", "grapes"],  # items for Fruits Category
     ["purple", "blue", "green"]  # items for Colors Category
    ]
]
compact_processor(favorites)