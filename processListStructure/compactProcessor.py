
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


        '''
            Why wrap the single list?
            - zip() function later in the code expects to pair each category name with a list of items


            - When there's only one category with a flat list of items, we need to wrap that list into another list
            so that it matches the expected structure of multiple categories with nested lists. This ensures that when we use zip() to pair category names with their items, each category name correctly
            corresponds to a list of items, even if there's only one category.
            - zip() pairs each category name with its full item list
            
            
            
            
            
            
            
            
            
              - Ensures consistent structure for processing
            - Avoids mismatched pairs in iteration
            - Simplifies downstream logic
            - Enables uniform handling of categories
            - Prevents errors in processing loops
            - Facilitates scalability for future categories
            
        '''
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