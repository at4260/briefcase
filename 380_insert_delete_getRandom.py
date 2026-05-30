import random 

class RandomizedSet:
    def __init__(self):
        self.val_list = []
        self.val_dict = {}

    def insert(self, val) -> bool:
        if val in self.val_dict:
            return False        
        self.val_list.append(val)
        self.val_dict[val] = len(self.val_list) - 1 # list index
        return True
    
    def remove(self, val) -> bool:
        if val not in self.val_dict:
            return False        
        
        idx = self.val_dict.get(val)

        # handle separately if removing the last element in a list (list[-1]) so it doesn't swap with itself
        if idx == len(self.val_list) - 1:
            self.val_list.pop()
            del self.val_dict[val]
            return True

        # swap list positions with last element and update dict
        last_element_val = self.val_list[-1]
        last_element_idx = self.val_dict[last_element_val]
        self.val_list[idx] = last_element_val
        self.val_list[last_element_idx] = val

        del self.val_dict[val]
        self.val_dict[last_element_val] = idx

        self.val_list.pop()
        return True        
    
    def getRandom(self) -> int:
        if self.val_list:
            random_idx = random.randint(0, len(self.val_list) - 1)
            return self.val_list[random_idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
