class List():
    def __init__(self):
        self.mylist = []

    def set_list_items(self, new_list):
        self.mylist = new_list
    
    def target_func(self, target):
        results = []
        for i in range(len(self.mylist)):
            second_item = target - self.mylist[i] 
            if second_item in self.mylist:
                results.append([i, self.mylist.index(second_item)])
        
        return results if len(results) > 0 else -1


newListObj = List()
newListObj.set_list_items([1, 2, 3, 4, 5])
print(newListObj.target_func(5))
