# Simple Detection Logic: Functions to handle nested and flat list structures
'''
1. Unpack data into category_names and category_items
2. Iterate over category_names with index, and print the category name
3. Determine(auto detect) if category_items is flat or nested list
4. Print each item in the list
'''
#⚠️ Empty Category: Reveals a potential bug (index out of range error)
'''
1. Handle completely empty category_items lists
2. Add Index Bounds Checking when accessing category_items by index
3. Add logic to Display items or indicate if empty
'''


def process_list_structure(data):
 # TODO 1: Unpack data into category_names and category_items
    # Tuple Unpacking Assignment Method 1: Direct unpacking (more Pythonic)
    # category_names, category_items = data 

    # Tuple Unpacking Assignment Method 2: Explicit assignment
    # category_names = data[0]
    # category_items = data[1]

    '''
        Tuple Unpacking Assignment Method 3: Direct indexing
            - The direct indexing unpacking pattern allows the function to accept a standardized data format where:
                - First element = list of category names
                - Second element = corresponding category items (either flat list for single category or nested lists for multiple categories)
    '''
    category_names, category_items = data[0], data[1]


    '''
        1. takes the data parameter (which is expected to be a tuple or list with at least 2 elements) and assigns
            - data[0] → category_names
            - data[1] → category_items
            - Example: Single Category Structure
                data = (
                            ["Fruits Category"],  # category_names
                            ["avocado", "pineapple", "plum", "grapes"] # category_items (flat list)
                        )
                        After unpacking:
                            - category_names = ["Fruits Category"]
                            - category_items = ["avocado", "pineapple", "plum", "grapes"]
             - Example: Mutiple Category Structure
                data = (
                            ["Fruits Category", "Colors Category"],  # category_names

                                    # category_items (nested lists)
                            [
                                ["avocado", "pineapple", "plum", "grapes"],  # items for Fruits Category
                                ["red", "blue", "green"]  # items for Colors Category
                            ]
                        )
                        After unpacking:
                            - category_names = ["Fruits Category", "Colors Category"]
                            - category_items = [["avocado", "pineapple", "plum", "grapes"], ["red", "blue", "green"]]
    '''

    # ⚠️ TODO 1: Handle empty category_items case
        # Prevents IndexError when accessing category_items[0]
    if not category_items:
        for category_name in category_names:
            print(f"Category: '{category_name}'")
            print("  (No items available)")
            print()
        return







    '''
        for each category_name in category_names, it prints the name and then:
            - determines if category_items is a flat list or nested lists
                - Nested Lists: uses the current index of category_name to get the corresponding category_items sublist
                    - category_names[0](first category) = category_items[0] (first sublist)
                    - category_names[1](second category) = category_items[1] (second sublist)
                - Flat List: uses the entire category_items list
            - takes the resulting flat list of items and prints each item under the category name
            - if there are multiple category_names, the for loop starts over for the next category

    '''

 # TODO 2: Iterate over category_names with index, and print the category name
    for i, category_name in enumerate(category_names):
        print(f"Category: '{category_name}'")
        
        
        '''
            Auto-Detection Logic: determine if category_items is a flat list or nested lists
                Step 1: Check if the first element of category_items is a lists
                    if isinstance(category_items[0], list):
                Step 2: Item Assignment Based on Detection
                        # category_items[i]: get the i-th sublist,uses the current index i to get the corresponding sublist
                            # SO FOR THE FIRST category_name, IT WILL GET THE FIRST SUBLIST FROM category_items
                            # items will be a flat list
                        items = category_items[i]  # Nested: If the first item is a list then get the corresponding sublist(there are multiple categories)
                    else:
                        # items will be a flat list
                        items = category_items      # Flat: If the first item is not a list then get the entire list(there is a single category)
                        
                    for item in items: # items will be a flat list
                        print(f"  - {item}")
                    print()
        '''
 # TODO 3: Determine(auto detect) if category_items is flat or nested list
            # if nested get the corresponding sublist, if flat get the entire list
        if isinstance(category_items[0], list):
            # items = category_items[i]  # Multiple categories


            # ⚠️ TODO 2: Add Index Bounds Checking: Multiple categories - check if current category has items
                # Prevents crashes when there are more category names than item lists and gracefully handles mismatched counts
            if i < len(category_items):
                items = category_items[i]
            else:
                items = []

        else:
            items = category_items      # Single category
        
 # TODO 4: Print each item in the list
        # for item in items:
        #     print(f"  - {item}")
        # print()
        

        # ⚠️ TODO 3: Add logic to Display items or indicate if empty
            #   Provides clear feedback when individual demos have no items
        if items:
            for item in items:
                print(f"  - {item}")
        else:
            print("  (No items available)")
        print()



# # Simple Detection Logic
# ✅ Empty category_items list
# ✅ Individual empty category lists
# ✅ Mismatched category names vs. items count
# ✅ Mixed scenarios (some categories with items, some without)
# def process_any_category(data):
#     category_names, category_items = data[0], data[1]
    
#     # Handle empty category_items case
#     if not category_items:
#         for category_name in category_names:
#             print(f"Category: '{category_name}'")
#             print("  (No items available)")
#             print()
#         return
    
#     for i, category_name in enumerate(category_names):
#         print(f"Category: '{category_name}'")
        
#         # Auto-detect structure and get items
#         if isinstance(category_items[0], list):
#             # Multiple categories - check if current category has items
#             if i < len(category_items):
#                 items = category_items[i]
#             else:
#                 items = []
#         else:
#             items = category_items      # Single category
            
#         # Display items or indicate if empty
#         if items:
#             for item in items:
#                 print(f"  - {item}")
#         else:
#             print("  (No items available)")
#         print()


def test_process_any_category():
    """
    Test handler function for process_any_category function.
    Tests both single category and multiple categories scenarios.
    """
    print("=" * 50)
    print("TESTING process_any_category FUNCTION")
    print("=" * 50)
    
    # Test Case 1: Single Category Structure
    print("\n--- Test Case 1: Single Category Structure ---")
    single_category_data = (
        ["Fruits Category"],  # category_names
        ["avocado", "pineapple", "plum", "grapes"]  # category_items (flat list)
    )
    
    print("Input data:")
    print(f"  Category names: {single_category_data[0]}")
    print(f"  Category items: {single_category_data[1]}")
    print("\nOutput:")
    process_list_structure(single_category_data)
    
    # Test Case 2: Multiple Categories Structure
    print("--- Test Case 2: Multiple Categories Structure ---")
    multiple_categories_data = (
        ["Fruits Category", "Colors Category", "Numbers Category"],  # category_names
        [
            ["avocado", "pineapple", "plum"],      # items for Fruits Category
            ["red", "green", "blue"],           # items for Colors Category
            ["one", "two", "three", "four"]     # items for Numbers Category
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {multiple_categories_data[0]}")
    print(f"  Category items: {multiple_categories_data[1]}")
    print("\nOutput:")
    process_list_structure(multiple_categories_data)
    
    # Test Case 3: Edge Case - Single Category with One Item
    print("--- Test Case 3: Edge Case - Single Category with One Item ---")
    single_item_category = (
        ["Single Item Category"],
        ["only_item"]
    )
    
    print("Input data:")
    print(f"  Category names: {single_item_category[0]}")
    print(f"  Category items: {single_item_category[1]}")
    print("\nOutput:")
    process_list_structure(single_item_category)
    
    # Test Case 4: Edge Case - Empty Category
    print("--- Test Case 4: Edge Case - Empty Category ---")
    empty_category = (
        ["Empty Category"],
        []
    )
    
    print("Input data:")
    print(f"  Category names: {empty_category[0]}")
    print(f"  Category items: {empty_category[1]}")
    print("\nOutput:")
    process_list_structure(empty_category)
    
    # Test Case 5: Edge Case - Multiple Categories with Some Empty
    print("--- Test Case 5: Edge Case - Multiple Categories with Some Empty ---")
    mixed_categories = (
        ["Fruits Category", "Empty Category", "Colors Category"],
        [
            ["avocado", "pineapple"],  # Fruits has items
            [],                   # Empty category
            ["red", "blue"]       # Colors has items
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {mixed_categories[0]}")
    print(f"  Category items: {mixed_categories[1]}")
    print("\nOutput:")
    process_list_structure(mixed_categories)
    
    # Test Case 6: Edge Case - Mismatched Category Names and Items Count
    print("--- Test Case 6: Edge Case - More Category Names Than Items ---")
    mismatched_categories = (
        ["Category 1", "Category 2", "Category 3"],  # 3 names
        [["item1"], ["item2"]]           # Only 2 item lists
    )
    
    print("Input data:")
    print(f"  Category names: {mismatched_categories[0]}")
    print(f"  Category items: {mismatched_categories[1]}")
    print("\nOutput:")
    process_list_structure(mismatched_categories)
    
    print("=" * 50)
    print("TESTING COMPLETED")
    print("=" * 50)


# Run the test handler function
if __name__ == "__main__":
    test_process_any_category()