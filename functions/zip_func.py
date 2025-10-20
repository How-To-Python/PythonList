'''
# Python zip() Function 
- a built-in utility used to combine multiple iterable objects (such as lists, tuples, or strings) into a single iterable of tuples
    1. Pass two or more lists, tuples, strings, or any other iterables to `zip()`
    2. zip() will pair elements from the corresponding positions of the input iterables
    3. Then a zip object(iterator) is created
       - the iterator aggregates elements from each of the input iterables, producing tuples containing one element from each iterable
       - element yielded by this iterator is a tuple containing one item from each of the input iterables, taken at the same index
    4. You can convert this zip object into a list or iterate over it directly in a loop
- Useful for parallel iteration over multiple sequences, combining related data, or transposing rows and columns in data structures
'''

names = ["Lisa", "Jim", "Lewis"]
favColors = ["yellow", "purple", "green"]

# Example 1: Zipping Two Lists
zipped_data = zip(names, favColors)
print(zipped_data)  # Output: <zip object at 0x000002A43335A980>
print(type(zipped_data))  # Output: <class 'zip'>
print(list(zipped_data))

# Output: [('Lisa', 'yellow'), ('Jim', 'purple'), ('Lewis', 'green')]

# Example 2: Using zip in a for loop to unpack values: iterate over it directly in a loop
for name, favColor in zip(names, favColors):
    print(f"{name}'s favorite color is {favColor}")

# Output:
# Lisa's favorite color is yellow
# Jim's favorite color is purple
# Lewis's favorite color is green

# Example 3: Unzipping using the * operator
    # The * operator is used to unpack the zipped object back into individual lists
    # It effectively reverses the zipping process
    # When you use * on a zipped object, it separates the tuples back into their original components
    # This allows you to reconstruct the original lists from the zipped data
    # The result is a series of tuples, each containing elements from the original lists at the same index
autos = ["cars", "trucks"]
count = [247, 457]
zipped_auto_type_count = zip(autos, count)
unzipped_autos, unzipped_count = zip(*zipped_auto_type_count)
print(unzipped_autos)
print(unzipped_count)

# Output:
# ('cars', 'trucks')
# (247, 457)