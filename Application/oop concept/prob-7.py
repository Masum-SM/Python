"""  
Write a Python class to get all possible unique subsets from a set of integers.
Input  : [4, 5, 6] 
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]


"""


class create_subset:
    def sort_list(self, my_list):
        return self.finding_subset([], sorted(my_list))
    
    def finding_subset(self, present, my_list):
        if my_list:
            return self.finding_subset(present, my_list[1:]) + self.finding_subset(present + [my_list[0]], my_list[1:])
        return [present]
    
sorted_list = create_subset().sort_list([4,5,6])

print(sorted_list)


