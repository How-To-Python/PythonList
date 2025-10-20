# [`process_list_structure()`](./processListStructure.py)
**Processes categorized data with automatic structure detection and comprehensive error handling for various edge cases.**

## 🔭 Overview

The `processListStructure.py` file contains a robust data processing function that intelligently handles both single and multiple category list structures. It's designed to automatically detect the data format and process it accordingly, making it versatile for different data organization patterns.

## 🔑 Key Functionality
1. **Smart Data Processing** 
2. **Flexible Input Format** 
3. **Robust Error Handling** 
4. **Comprehensive Testing**

### 🗒️ 1. **Smart Data Processing**
- the function `process_list_structure()` automatically detects whether it's dealing with a single category (flat list) or multiple categories (nested lists) and processes them accordingly
- **Single Category**: Handles flat lists for one category
    - `[["Fruits Category"],["avocado", "pineapple", "plum", "grapes"] ]`
- **Multiple Categories**: Handles nested lists for multiple categories
    - `["Fruits Category", "Colors Category"],[["avocado", "pineapple", "plum"], ["red", "blue", "green"]]`

### 🔤 **Flexible Input Format:**
- Accepts data in a standardized tuple format where the first element contains category names and the second contains the corresponding items.
- **Input Data Structure**: 
    - `(["Category Names"], [category_items])`
    - `[["Category Names"], [category_items]]`


### ❎ **Robust Error Handling**
- Handles various edge cases like empty categories, mismatched counts between category names and items, and index out-of-bounds scenarios.
- **Empty Categories**: Gracefully handles completely empty category lists
- **Index Bounds Checking**: Prevents crashes when category names outnumber item lists
- **Mixed Scenarios**: Handles cases where some categories have items and others don't

### 🧪 **Comprehensive Testing:** 
- Includes a thorough test suite with 6 different text cases to validate the function's behavior.
- **Test Functionality**
    1. **Single Category Structure** - Standard flat list
    2. **Multiple Categories Structure** - Standard nested lists
    3. **Single Item Category** - Edge case with one item
    4. **Empty Category** - Completely empty data
    5. **Mixed Categories** - Some empty, some populated
    6. **Mismatched Counts** - More names than item lists

### 📝 Processing Logic
1. **Data Unpacking**: Extracts category names and items from input data
2. **Empty Check**: Handles cases where no items exist at all
3. **Structure Detection**: Determines if dealing with flat or nested lists
4. **Index Validation**: Ensures safe access to category items
5. **Output Generation**: Formats and displays categorized data

### 🧭 Edge Cases Handled
- **Completely Empty Categories**: No items in any category
- **Individual Empty Categories**: Some categories have no items
- **Mismatched Counts**: More category names than item lists
- **Single Item Categories**: Categories with only one item
- **Mixed Scenarios**: Combination of populated and empty categories

## 💙 Use Cases
**Useful for applications that need to handle flexible data structures while providing consistent, user-friendly output formatting**
- **Data Categorization**: Organizing items into logical groups
- **Dynamic Content Display**: Handling variable data structures
- **Configuration Processing**: Processing structured configuration data
- **Report Generation**: Creating categorized reports from various data sources
