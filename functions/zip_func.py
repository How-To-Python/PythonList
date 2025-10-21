'''
# Python zip() Function 
- a built-in utility used to combine multiple iterable objects (such as lists, tuples, or strings) into a single iterable of tuples
    1. Pass two or more lists, tuples, strings, or any other iterables to `zip()`
    2. zip() will pair elements from the corresponding positions of the input iterables
        - stops creating tuples when the shortest input iterable is exhausted(Example 4)
    3. Then a zip object(iterator) is created
       - the iterator aggregates elements from each of the input iterables, producing tuples containing one element from each iterable
       - element yielded by this iterator is a tuple containing one item from each of the input iterables, taken at the same index
       - Iterator Exhaustion: the zip object is an iterator itself, meaning it can be iterated over only once(Example 2)
    4. You can convert this zip object into a list or iterate over it directly in a loop
- Useful for parallel iteration over multiple sequences, combining related data, or transposing rows and columns in data structures
'''

'''
⚠️ Iterator Exhaustion: fundamental behavior of Python iterators to optimize memory usage
    - Iterators in Python are "one-time use"
    - once you consume them (convert to list, iterate through them, etc.), they become empty and cannot be reused
'''





names = ["Lisa", "Jim", "Lewis"]
favColors = ["yellow", "purple", "green"]

# Example 1: Zipping Two Lists
zip_two_list = zip(names, favColors)

print("\n")

# the iterator is not being consumed yet because we haven't converted it to a list or iterated over it
print(f'ZIP OBJECT: {zip_two_list}')  # Output: <zip object at 0x000002A43335A980>
print("=" * 60)

print(f'ZIP OBJECT TYPE: type({zip_two_list})')  # Output: <class 'zip'>
print("=" * 60)

# convert this zip object into a list, iterator is consumed here
print(f'TWO LIST ZIPPED: {list(zip_two_list)}') # Output: [('Lisa', 'yellow'), ('Jim', 'purple'), ('Lewis', 'green')]
print("=" * 60)


# Example 2: Attempting to reuse the exhausted iterator
zip_iterator_exhaustion = zip(names, favColors)
print(f'ITERATOR EXHAUSTION First consumption: {list(zip_iterator_exhaustion)}')  # Output: [('Lisa', 'yellow'), ('Jim', 'purple'), ('Lewis', 'green')] ← First consumption
print(f'ITERATOR EXHAUSTION Second consumption: {list(zip_iterator_exhaustion)}')  # Output: [] ← Second consumption, iterator is exhausted
# Fix: Recreate the iterator to reuse
print("=" * 60)




# Example 3: Using zip in a for loop to unpack values: iterate over it directly in a loop
print("FOR LOOP UNPACKING:")
for name, favColor in zip(names, favColors):
    print(f"{name}'s favorite color is {favColor}")
'''
Output:
    Lisa's favorite color is yellow
    Jim's favorite color is purple
    Lewis's favorite color is green

'''
print("=" * 60)

# unpacking operator (*)
# zip(*zipped_auto_type_count)
    # * unpacks it as separate arguments to zip()
    # Is equivalent to: zip(('cars', 247), ('trucks', 457))
# *zipped_auto_type_count: Unpacks the zipped object back into separate arguments


# tuple unpacking assignment
# unzipped_autos, unzipped_count: Assigns the two resulting tuples to separate variables



# Example 4: Unzipping(reversing)  unpacking operator (*) and tuple unpacking assignment
    # The * operator is used to unpack the zipped object back into individual lists
    # It effectively reverses the zipping process
    # When you use * on a zipped object, it separates the tuples back into their original components
    # This allows you to reconstruct the original lists from the zipped data
    # The result is a series of tuples, each containing elements from the original lists at the same index
# Step 1: Original data
autos = ["cars", "trucks"]
count = [247, 457]

# Step 2: Zip them together
zipped_auto_type_count = zip(autos, count)# Creates: [('cars', 247), ('trucks', 457)]

# Step 3: Unzip using * operator
# unpacking operator (*) unpacks to: ('cars', 247), ('trucks', 457)
# zip() groups the unpacks by position to : Position 0: ('cars', 'trucks') and Position 1: (247, 457)
# tuple unpacking assignment assigns them to separate variables
    # unzipped_autos gets ('cars', 'trucks')
    # unzipped_count gets (247, 457)
unzipped_autos, unzipped_count = zip(*zipped_auto_type_count)
print(unzipped_autos)
print(unzipped_count)

# Output:
# ('cars', 'trucks')
# (247, 457)


# Example 5: Handling Unequal Lengths
    # If the input iterables are of unequal lengths, 
        # zip() stops creating tuples when the shortest input iterable is exhausted
        # once the shortest iterable has no more elements, zip() stops completely
category_names = ["Fruits"]
category_items = ["apple", "banana", "orange"]  # Flat list
zipped_unequal = zip(category_names, category_items)
print(list(zipped_unequal))# [('Fruits', 'apple')]
# Output: [('Fruits', 'apple')]
    # Only one tuple is created because category_names has only one element
    # To handle this, we can use the List Wrapping Technique

### List Wrapping Technique
    # - wrapped single list into another list for uniform processing

correct_zip_pairs = zip(category_names, [category_items])
print(f'List Wrapping: {list(correct_zip_pairs)}')# [('Fruits', ['apple', 'banana', 'orange'])]