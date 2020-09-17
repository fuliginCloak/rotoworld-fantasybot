import json
import urllib.request


# outer function that wraps the inner function with json file as obj and the key 
def extract(json_obj,key):
    # Empty  array
    arr = []
    
    # inner function json file as obj, empty array  and key
    def player_path(json_obj, arr, key):
        # confirms the json_obj is of data type dictionary
        if isinstance(json_obj, dict):
            # for all items in json_obj dictionare
            for k , v in json_obj.items():
                #  if the value is a list or a dictionary
                if isinstance(v,(dict, list)):
                    # then get the value and key
                    player_path(v, arr, key)
                # if not a data type dictionary or list then just get key 
                elif k == key:
                    # and add that key to out empty array
                    arr.append(v)
        # confirms the json_obj is of data type list
        elif isinstance(json_obj,list):
            # if it is a list then take all the items in that list
            for item in json_obj:
                # add it to empty arry
                player_path (item, arr, key)
        # return array
        return arr


    # the inner function got the array and now calls itself with the new returned array instead of the initial empty array
    results = player_path(json_obj,arr,key)
    return results

    extract()
    






