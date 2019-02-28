from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

## Write code to insert food types into a data structure here. The data is in data.py. Put food types into a Hashmap 

types = sorted(types, reverse = True)

# Get distinct keys for the food types data
food_keys = []
for food_type in types:
  key = food_type[0]
  if key not in food_keys:
    food_keys.append(key)

# For each key, create a LinkedList; store all LinkedLists in a dictionary
food_type_lists = {}
for key in food_keys:
  food_type_lists[key] = LinkedList()
  current_list = food_type_lists[key]
  for food_type in types:
    if food_type[0] == key:
      current_list.insert_beginning(food_type)
  
# Put the dictionary of LinkedLists into a hash map
types_hash = HashMap(len(food_keys))
for i in food_type_lists:
    types_hash.assign(i, food_type_lists[i])



## Write code to insert restaurant data into a data structure here. The data is in data.py. Put into a LinkedList

# For each food type, put all restaurants into a single LinkedList
restaurant_lists={}
for food_type in types:
  restaurant_lists[food_type] = LinkedList()
  current_list = restaurant_lists[food_type]
  for resto in restaurant_data:
    if resto[0] == food_type:
      current_list.insert_beginning(resto)
      
# Create a master LinkedList of all cuisine's LinkedLists
restaurants_by_type = LinkedList()
for food_type in types:
  current_food_type_restaurant_list = restaurant_lists[food_type]
  restaurants_by_type.insert_beginning(current_food_type_restaurant_list)
  
  

  
## Data overview:
## types_hash:  A hashmap of all cuisines starting with a certain letter
## restaurants_by_type:  A LinkedList of LinkedLists of restaurants by cuisine

 


      
##Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower().strip()
        
    #Check for 'food type' match for user query in hash map##
    #Get relevant LinkedList from hashmap
    hash_key = user_input[0]
    cuisine_types_list = types_hash.retrieve(hash_key)
    
    #Storage for matches
    available_types = []    
    
    ## If a LinkedList was found in the hashmap, check for matches with the full user input 
    if cuisine_types_list:
      current_node = cuisine_types_list.get_head_node() # get into linkedList
      input_index = len(user_input)   # get number of letters to compare in food type
      
      # Go through all cuisine nodes and check for matches to user's full input
      while current_node.get_value():   
        if current_node.get_value()[:input_index] == user_input:
          available_types.append(current_node.get_value())
          current_node = current_node.get_next_node()
          
        else:
          current_node = current_node.get_next_node()
        
      # Inform user of matches & get their decision
      # - multiple matches (back to start)
      if len(available_types) > 1:
        print("With those beginning letters, your choices are  {0}. Please type one to confirm your choice, or select a new cuisine".format(available_types))
        available_types = []
        
      # - single match (confirm - if no then back to start, otherwise find restaurants)  
      elif len(available_types) == 1:
        user_confirmation = str(input("The only option with those beginning letters is {0}. Do you want to look at {0} restaurants? Enter 'y' for yes and 'n' for no.\n".format(available_types))).lower()
        
        if user_confirmation == 'n':
          available_types = [] 
        
        # print restos
        else:
          # After finding food type write code for retrieving restaurant data here
          # Check that a single choice has being made
          if len(available_types) == 1:
            chosen_type = available_types[0]

            # Get 1st node containing a LinkedList of Restaurants for the 1st cuisine type
            current_food_node = restaurants_by_type.get_head_node()
            current_food_linkedList = current_food_node.get_value()
            
					  # iterate through linked lists to find 1 for correct food type
            while current_food_linkedList: 	
              current_restaurant_node = current_food_linkedList.get_head_node()
              current_restaurant = current_restaurant_node.get_value()
              current_restaurant_type = current_restaurant[0]
              
              # List of restaurants found for cuisine type
              if current_restaurant_type == chosen_type:
                print('The {0} Restaurants in Soho are.....\n'.format(chosen_type))
                
                # Loop through the linked list to print items in pretty way:
                while current_restaurant:
                  print('*******************\n')
                  print('Name: {0}'.format(current_restaurant[1]))
                  print('Price: {0}'.format(current_restaurant[2]))
                  print('Rating: {0}'.format(current_restaurant[3]))
                  print('Address: {0}\n'.format(current_restaurant[4]))
                  
                  current_restaurant_node = current_restaurant_node.get_next_node()
                  current_restaurant = current_restaurant_node.get_value() 
                  
          
                # restart parent nodes
                current_food_node = None
                current_food_linkedList = None
                current_restaurant_node = None
                current_restaurant = None
                current_restaurant_type = None

                # Check if user wants to find more restaurants?
                user_restart = str(input('Do you want to find other restaurants? Enter \'y\' for yes and \'n\' for no.\n')).lower()
                if user_restart == 'n':
                  print('Goodbye!')
                  exit()
                  
                else:
                  available_types = []



              # Restaurant list not a match, go onto the next list
              else:
                # Update links to explore next LinkedList of restaurants
                current_food_node = current_food_node.get_next_node()
                current_food_linkedList = current_food_node.get_value()

                   
      #  - no match (back to start)    
      else:
        print("There were no matches for your search. Please try another cuisine")
          
      
    ## No LinkedList found due to incorrect first letter of cuisine search, return to beginning  
    else:
      print("There were no cuisines beginning with {0}. Please try another search".format(hash_key))
      
    
    
    
        
      
      
    
    



