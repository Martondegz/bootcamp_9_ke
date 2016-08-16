"""
Your answer should be returned in an array containing
the min and max number, respectively.

"""
#### pseudocode
# loop through input and compare variables
# return size list if values/ elements are equal
# check for largest element in list
#check for smallest element in list
# append values and return list

def find_max_min(list):

  # check for whether all list elements are equal using inbuilf all()
  # looping through all elements in the list 
  if all(x == list[0] for x in list) == True:

    # if elements are equal, the length is appended to new_list
    new_list = []
    new_list.append(len(list))
    return new_list
  else:

    # m defines the maximum or largest element in the list
    maxx = max(list)
    
    # minn defines the minimum or smallest element in the list
    minn = min(list)

    list2 = []
    # the final empty list, list2 adds the minimum and maximum values respectively
    list2.append(minn)
    list2.append(maxx)
    
    return list2
  
