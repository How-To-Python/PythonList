'''
Python Tuple Unpacking Demonstration
====================================

Tuple unpacking is a powerful Python feature that allows you to assign values from a tuple
to multiple variables in a single operation. This technique enhances code readability,
reduces lines of code, and enables elegant data manipulation.

Why Tuple Unpacking is Better:
- Pythonic: The preferred Python way of handling multiple values
- Readable: Variable names are self-explanatory
- Maintainable: Easier to modify and understand
- Error Prevention: Reduces indexing mistakes
- Performance: Slightly more efficient


Key Benefits:
- Cleaner, more readable code
- Simultaneous assignment of multiple variables
- Elegant handling of function return values
- Efficient data structure manipulation
'''

print("=" * 60)
print("PYTHON TUPLE UNPACKING DEMONSTRATION")
print("=" * 60)

# =============================================================================
# 1. BASIC TUPLE UNPACKING
# =============================================================================

print("\n================= 1. Basic Tuple Unpacking =================")

# Basic example: Unpacking coordinates
coordinates = (10, 20)
x, y = coordinates  # Tuple unpacking
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")
print("------------------------------------------------------------")

# Multiple values
person_data = ("Alice", 25, "Engineer")
name, age, profession = person_data
print(f"Person Data: {person_data}")
print(f"Name: {name}, Age: {age}, Profession: {profession}")
print("------------------------------------------------------------")



'''
============ 2 and 3: Both loops produce identical output =====================
without tuple unpacking vs with tuple unpacking
Without tuple unpacking: 
    - must use indexing to access tuple elements, less readable and more verbose
    - item[0] and item[1] don't clearly indicate what they represent
    - easy to mix up indices
    - Hard to understand the purpose of each element
    - Performance:
        - Each indexing operation adds overhead, especially in large loops
            - Two indexing operations (item[0], item[1])
        - Creates additional attribute lookups

With tuple unpacking:
    - Direct variable access - no indexing needed
    - Descriptive variable names improve clarity
    - Reduces risk of index-related errors
    - Performance:
        - More efficient: Direct assignment without indexing
        - Cleaner memory usage: No intermediate tuple object handling

Key Differences:
1. What zip() Returns
    - Without unpacking: Each iteration yields a tuple
    - With unpacking: Each iteration directly assigns values to variables
2. Variable Assignment
   - Without unpacking: Must use indexing to access elements
   - With unpacking: Direct variable assignment improves readability
3. Data Access Method
   - Without unpacking: Access elements via indexing (e.g., item[0], item[1])
   - With unpacking: Access elements via direct variable names (e.g., index, fruit)
'''

# =============================================================================
# 2. ENUMERATE() WITH TUPLE UNPACKING
# =============================================================================

print("============ 2. Enumerate with Tuple Unpacking =============")

fruits = ["apple", "banana", "orange"]
# enumerate(fruits) returns: (0, 'apple'), (1, 'banana'), (2, 'orange')

print("Without tuple unpacking:")
for item in enumerate(fruits):
    # item receives the entire tuple from zip()
    # item = (0, 'apple')  # First iteration
    # Must use indexing:  (item[0], item[1]) to access individual elements
    print(f"Index: {item[0]}, Value: {item[1]}")
print("------------------------------------------------------------")


print("\nWith tuple unpacking:")
for index, fruit in enumerate(fruits):  # Tuple unpacking here!
    # Automatically unpacks: index = 0, fruit = 'apple'  # First iteration
    # Direct access to values(no indexing needed) using descriptive variable names(index, fruit)
    print(f"Index: {index}, Value: {fruit}")
print("------------------------------------------------------------")

# =============================================================================
# 3. ZIP() WITH TUPLE UNPACKING
# =============================================================================

print("\n=============== 3. Zip with Tuple Unpacking =============== ")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

print("Without tuple unpacking:")
for item in zip(names, ages, cities):
    print(f"Name: {item[0]}, Age: {item[1]}, City: {item[2]}")
print("------------------------------------------------------------")


print("\nWith tuple unpacking:")
for name, age, city in zip(names, ages, cities):  # Tuple unpacking!, Easy to add more variables if zip() includes more lists
    print(f"Name: {name}, Age: {age}, City: {city}")
print("------------------------------------------------------------")

# =============================================================================
# 4. FUNCTION RETURN VALUES UNPACKING
# =============================================================================

print("\n==================== 4. Function Return Values Unpacking ====================")

def get_user_info():
    """Returns multiple values as a tuple"""
    return "John Doe", 28, "Developer", "john@email.com"

def calculate_stats(numbers):
    """Returns statistical data as a tuple"""
    return min(numbers), max(numbers), sum(numbers), len(numbers)

# Unpacking function return values
user_name, user_age, user_job, user_email = get_user_info()
print(f"User: {user_name}, {user_age}, {user_job}, {user_email}")
print("------------------------------------------------------------")

numbers = [1, 5, 3, 9, 2, 7]
min_val, max_val, total, count = calculate_stats(numbers)
print(f"Stats: Min={min_val}, Max={max_val}, Total={total}, Count={count}")
print("------------------------------------------------------------")


# =============================================================================
# 5. DICTIONARY ITEMS() UNPACKING
# =============================================================================

print("\n--- 5. Dictionary Items Unpacking ---")

student_grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

print("Without tuple unpacking:")
for item in student_grades.items():
    print(f"Student: {item[0]}, Grade: {item[1]}")

print("\nWith tuple unpacking:")
for student, grade in student_grades.items():  # Tuple unpacking!
    print(f"Student: {student}, Grade: {grade}")

# # =============================================================================
# # 6. NESTED TUPLE UNPACKING
# # =============================================================================

# print("\n--- 6. Nested Tuple Unpacking ---")

# # Nested tuples
# nested_data = (("Alice", "Bob"), (25, 30), ("Engineer", "Designer"))

# # Unpacking nested tuples
# (name1, name2), (age1, age2), (job1, job2) = nested_data
# print(f"Person 1: {name1}, {age1}, {job1}")
# print(f"Person 2: {name2}, {age2}, {job2}")

# # Complex nested structure
# company_data = (
#     "TechCorp",
#     ("Alice", "CTO"),
#     ("Bob", "Developer"),
#     (2020, 50)  # year founded, employees
# )

# company_name, (cto_name, cto_title), (dev_name, dev_title), (year, employees) = company_data
# print(f"Company: {company_name}")
# print(f"CTO: {cto_name} ({cto_title})")
# print(f"Developer: {dev_name} ({dev_title})")
# print(f"Founded: {year}, Employees: {employees}")

# # =============================================================================
# # 7. VARIABLE SWAPPING WITH TUPLE UNPACKING
# # =============================================================================

# print("\n--- 7. Variable Swapping ---")

# # Traditional swapping (requires temporary variable)
# a = 10
# b = 20
# print(f"Before traditional swap: a={a}, b={b}")
# temp = a
# a = b
# b = temp
# print(f"After traditional swap: a={a}, b={b}")

# # Elegant swapping with tuple unpacking
# x = 100
# y = 200
# print(f"Before tuple unpacking swap: x={x}, y={y}")
# x, y = y, x  # Tuple unpacking swap!
# print(f"After tuple unpacking swap: x={x}, y={y}")

# # Multiple variable swapping
# p, q, r = 1, 2, 3
# print(f"Before: p={p}, q={q}, r={r}")
# p, q, r = r, p, q  # Rotate values
# print(f"After rotation: p={p}, q={q}, r={r}")

# # =============================================================================
# # 8. UNPACKING WITH ASTERISK (*) - EXTENDED UNPACKING
# # =============================================================================

# print("\n--- 8. Extended Unpacking with Asterisk (*) ---")

# # Unpacking first, last, and rest
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# first, *middle, last = numbers
# print(f"First: {first}")
# print(f"Middle: {middle}")
# print(f"Last: {last}")

# # Unpacking with specific patterns
# data = ("Alice", 25, "Engineer", "Python", "JavaScript", "React")

# name, age, job, *skills = data
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Job: {job}")
# print(f"Skills: {skills}")

# # Head and tail unpacking
# head, *tail = [1, 2, 3, 4, 5]
# print(f"Head: {head}, Tail: {tail}")

# # =============================================================================
# # 9. PRACTICAL EXAMPLES - DATA PROCESSING
# # =============================================================================

# print("\n--- 9. Practical Data Processing Examples ---")

# # Example 1: Processing CSV-like data
# csv_data = [
#     ("Alice", "25", "Engineer", "95000"),
#     ("Bob", "30", "Designer", "85000"),
#     ("Charlie", "28", "Developer", "90000")
# ]

# print("Employee Data Processing:")
# for name, age, position, salary in csv_data:
#     annual_salary = int(salary)
#     monthly_salary = annual_salary // 12
#     print(f"{name} ({age}): {position} - ${monthly_salary:,}/month")

# # Example 2: Coordinate system calculations
# points = [(0, 0), (3, 4), (6, 8), (9, 12)]

# print("\nDistance from Origin:")
# for x, y in points:
#     distance = (x**2 + y**2) ** 0.5
#     print(f"Point ({x}, {y}): Distance = {distance:.2f}")

# # Example 3: Key-value pair processing
# config_settings = [
#     ("database_host", "localhost"),
#     ("database_port", "5432"),
#     ("debug_mode", "True"),
#     ("max_connections", "100")
# ]

# print("\nConfiguration Settings:")
# for setting, value in config_settings:
#     print(f"{setting.upper()}: {value}")

# # =============================================================================
# # 10. COMPARISON: WITH vs WITHOUT TUPLE UNPACKING
# # =============================================================================

# print("\n--- 10. Comparison: With vs Without Tuple Unpacking ---")

# # Sample data
# employee_records = [
#     ("Alice", "Engineering", 95000, "Senior"),
#     ("Bob", "Marketing", 75000, "Junior"),
#     ("Charlie", "Engineering", 85000, "Mid")
# ]

# print("\n❌ WITHOUT Tuple Unpacking (verbose, harder to read):")
# total_salary_without = 0
# for record in employee_records:
#     name = record[0]
#     department = record[1]
#     salary = record[2]
#     level = record[3]
#     total_salary_without += salary
#     print(f"  {name} from {department}: ${salary:,} ({level})")

# print(f"Total Salary (without unpacking): ${total_salary_without:,}")

# print("\n✅ WITH Tuple Unpacking (clean, readable):")
# total_salary_with = 0
# for name, department, salary, level in employee_records:
#     total_salary_with += salary
#     print(f"  {name} from {department}: ${salary:,} ({level})")

# print(f"Total Salary (with unpacking): ${total_salary_with:,}")

# # =============================================================================
# # 11. COMMON PITFALLS AND BEST PRACTICES
# # =============================================================================

# print("\n--- 11. Common Pitfalls and Best Practices ---")

# # Pitfall 1: Length mismatch
# print("\n⚠️  Pitfall 1: Length Mismatch")
# try:
#     data = (1, 2, 3)
#     a, b = data  # Error: too many values to unpack
# except ValueError as e:
#     print(f"Error: {e}")

# # Solution: Match the number of variables
# a, b, c = data  # Correct
# print(f"Correct unpacking: a={a}, b={b}, c={c}")

# # Best Practice: Use underscore for unused values
# print("\n✅ Best Practice: Use underscore for unused values")
# person_info = ("Alice", 25, "Engineer", "Unused Data")
# name, age, job, _ = person_info  # Use _ for unused value
# print(f"Used values: {name}, {age}, {job}")

# # Best Practice: Descriptive variable names
# print("\n✅ Best Practice: Use descriptive variable names")
# rgb_color = (255, 128, 0)
# red, green, blue = rgb_color  # Clear and descriptive
# print(f"RGB Color: Red={red}, Green={green}, Blue={blue}")

# print("\n" + "=" * 60)
# print("TUPLE UNPACKING DEMONSTRATION COMPLETED")
# print("=" * 60)

# =============================================================================
# SUMMARY
# =============================================================================
"""
TUPLE UNPACKING SUMMARY:

1. Basic Syntax: a, b = (1, 2)
2. Works with any iterable: lists, tuples, strings
3. Common uses:
   - enumerate(): for i, value in enumerate(list)
   - zip(): for a, b in zip(list1, list2)
   - dict.items(): for key, value in dict.items()
   - Function returns: x, y = function_returning_tuple()

4. Advanced features:
   - Nested unpacking: (a, b), (c, d) = ((1, 2), (3, 4))
   - Extended unpacking: first, *rest, last = sequence
   - Variable swapping: a, b = b, a

5. Benefits:
   - Cleaner, more readable code
   - Reduces indexing operations
   - Enables elegant data manipulation
   - Pythonic way of handling multiple values

6. Best practices:
   - Match variable count with tuple length
   - Use _ for unused values
   - Choose descriptive variable names
   - Prefer unpacking over indexing when possible
"""