def enhanced_processor(data):
    """
    Universal processor that handles any category structure
    """
    category_names = data[0]
    category_items = data[1]
    
    for i, category_name in enumerate(category_names):
        print(f"For '{category_name}':")
        
        # Determine if items are nested or flat
        if isinstance(category_items[i], list):
            # Multiple categories - use specific index
            items_to_process = category_items[i]
        else:
            # Single category - use all items
            items_to_process = category_items
        
        # Print each item
        for item in items_to_process:
            print(f"  - {item}")
        print()


def test_enhanced_processor():
    """
    Comprehensive test suite for enhanced_processor function.
    Tests various data structures and edge cases.
    """
    print("=" * 60)
    print("TESTING enhanced_processor FUNCTION")
    print("=" * 60)
    
    # Test Case 1: Single Category Structure
    print("\n--- Test Case 1: Single Category with Flat List ---")
    single_category_data = (
        ["Fruits"],  # category_names
        ["apple", "banana", "orange", "grape"]  # category_items (flat list)
    )
    
    print("Input data:")
    print(f"  Category names: {single_category_data[0]}")
    print(f"  Category items: {single_category_data[1]}")
    print("\nOutput:")
    enhanced_processor(single_category_data)
    
    # Test Case 2: Multiple Categories Structure
    print("--- Test Case 2: Multiple Categories with Nested Lists ---")
    multiple_categories_data = (
        ["Fruits", "Colors", "Animals"],  # category_names
        [
            ["apple", "banana", "orange"],     # items for Fruits
            ["red", "blue", "green", "yellow"], # items for Colors
            ["cat", "dog", "bird"]             # items for Animals
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {multiple_categories_data[0]}")
    print(f"  Category items: {multiple_categories_data[1]}")
    print("\nOutput:")
    enhanced_processor(multiple_categories_data)
    
    # Test Case 3: Single Item Categories
    print("--- Test Case 3: Single Item per Category ---")
    single_item_data = (
        ["Best Fruit", "Favorite Color", "Pet"],
        [["apple"], ["blue"], ["dog"]]
    )
    
    print("Input data:")
    print(f"  Category names: {single_item_data[0]}")
    print(f"  Category items: {single_item_data[1]}")
    print("\nOutput:")
    enhanced_processor(single_item_data)
    
    # Test Case 4: Empty Categories
    print("--- Test Case 4: Empty Categories ---")
    empty_categories_data = (
        ["Empty List 1", "Empty List 2"],
        [[], []]
    )
    
    print("Input data:")
    print(f"  Category names: {empty_categories_data[0]}")
    print(f"  Category items: {empty_categories_data[1]}")
    print("\nOutput:")
    enhanced_processor(empty_categories_data)
    
    # Test Case 5: Mixed Content Categories
    print("--- Test Case 5: Categories with Different Item Counts ---")
    mixed_content_data = (
        ["Short List", "Long List", "Medium List"],
        [
            ["item1"],                                    # 1 item
            ["a", "b", "c", "d", "e", "f", "g"],         # 7 items
            ["x", "y", "z"]                              # 3 items
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {mixed_content_data[0]}")
    print(f"  Category items: {mixed_content_data[1]}")
    print("\nOutput:")
    enhanced_processor(mixed_content_data)
    
    # Test Case 6: Categories with Different Data Types
    print("--- Test Case 6: Mixed Data Types ---")
    mixed_types_data = (
        ["Numbers", "Strings", "Mixed"],
        [
            ["1", "2", "3"],                    # number strings
            ["hello", "world", "python"],       # regular strings
            ["100", "text", "42"]               # mixed content
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {mixed_types_data[0]}")
    print(f"  Category items: {mixed_types_data[1]}")
    print("\nOutput:")
    enhanced_processor(mixed_types_data)
    
    # Test Case 7: Real-world Example - Programming Languages
    print("--- Test Case 7: Real-world Example - Programming Languages ---")
    programming_data = (
        ["Web Development", "Data Science", "Mobile Development"],
        [
            ["JavaScript", "HTML", "CSS", "React", "Node.js"],
            ["Python", "R", "Jupyter", "Pandas", "NumPy"],
            ["Swift", "Kotlin", "React Native", "Flutter"]
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {programming_data[0]}")
    print(f"  Category items: {programming_data[1]}")
    print("\nOutput:")
    enhanced_processor(programming_data)
    
    # Test Case 8: Food Categories
    print("--- Test Case 8: Food Categories ---")
    food_data = (
        ["Breakfast", "Lunch", "Dinner", "Snacks"],
        [
            ["cereal", "toast", "eggs", "coffee"],
            ["sandwich", "salad", "soup"],
            ["pasta", "chicken", "vegetables", "wine"],
            ["chips", "cookies", "fruit"]
        ]
    )
    
    print("Input data:")
    print(f"  Category names: {food_data[0]}")
    print(f"  Category items: {food_data[1]}")
    print("\nOutput:")
    enhanced_processor(food_data)
    
    print("=" * 60)
    print("ENHANCED PROCESSOR TESTING COMPLETED")
    print("=" * 60)


# Run the test function
if __name__ == "__main__":
    test_enhanced_processor()