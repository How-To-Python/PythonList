#*****************************************LIST***************************************************************************************************************
#************************************len()**************************************************
#TODO: List start counting at 0
# the len() function starts counting at 1
my_num_list = [38, 205, 165, 19]#there are 4 items in the list but the index only goes to 3 
print(len(my_num_list))# returns 4
print(len(my_num_list) -1)# returns 3, gets the last items index





#*********************************max()***********************************************************
#built-in max() function in Python is a versatile utility used to determine the largest item among a set of values or within an iterable
# Max Value: iterates through the elements of the list and returns the element with the highest value
number_list = [38, 205, 165, 19, 57, 40, 58, 138, 29, 189]
highest_value = max(number_list)
print(highest_value)





#*****************************************LIST COMPREHENSIONS**********************************************************************************
# - **Keword Method:** `[new_item for item in list]`

#************************************FROM A LIST OF DICTIONARIES**************************************************************

user_list = [{"username": "Shannon", "userid": 836724, "usercolor": "purple"}, {"username": "Lisa", "userid": 917437, "usercolor": "red"}, {"username": "James", "userid": 567297, "usercolor": "yellow"}]

#***********************Create A List of Tulpes************************************
user_color_tuple_list = [(item['username'], item['usercolor']) for item in user_list]
print(user_color_tuple_list)# [('Shannon', 'purple'), ('Lisa', 'red'), ('James', 'yellow')]

#***********************Create A List of Dictionaries*******************************
user_color_dict_list = [{"user_name":item['username'], "user_color":item['usercolor']} for item in user_list]
print(user_color_dict_list)# [{'user_name': 'Shannon', 'user_color': 'purple'}, {'user_name': 'Lisa', 'user_color': 'red'}, {'user_name': 'James', 'user_color': 'yellow'}]
#******************************************************************************************************************************
#******************FROM A DICTIONARY*******************************************************************************************
bids = {
    "Shannon": 215.0,
    "Lisa": 124.0,
    "James": 119.0,
    "Molly": 220.0,
    "Mike": 212.0,
}

#*********************Create List of Dictionaries*********************
bids_dict_list = [{key:value} for (key, value) in bids.items()]
print(f"List of Dictionaries: {bids_dict_list}")#  [{'Shannon': 215.0}, {'Lisa': 124.0}, {'James': 119.0}, {'Molly': 220.0}, {'Mike': 212.0}]

#*********************Create List of Tuples***************************
bids_list = [item for item in bids.items()]
# list of tuples each with a key and value
print(f"List of Tuples: {bids_list}")# [('Shannon', 215.0), ('Lisa', 124.0), ('James', 119.0), ('Molly', 220.0), ('Mike', 212.0)]
#*********************Create List of Dictionary Values****************
bids_list = [value for (key, value) in bids.items()]
# list of all the values
print(f"List of Dictionary Values: {bids_list}")#  [215.0, 124.0, 119.0, 220.0, 212.0]

#*********************Create List of Dictionary Keys*******************
bids_list = [key for (key, value) in bids.items()]
# list of all the keys
print(f"List of Dictionary Keys: {bids_list}")#  ['Shannon', 'Lisa', 'James', 'Molly', 'Mike']


#***********************************************************************************************
# If a letter in my_list matches a key in my_dict, add that key's value to dict_values_list
my_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot'}
my_list = ['B', 'C', 'D']

#For each letter in my_list get the corresponding value from my_dict
#Use each letter from my_list as a key in my_dict
dict_values_list = [my_dict[letter] for letter in my_list]
print(dict_values_list)# ['Bravo', 'Charlie', 'Delta']
