class SelectionSort:
    def __init__(self, lst):
        """
        Initialize the SelectionSort class with a list.
        """
        self.lst = lst

    def sort(self):
        """
        Perform selection sort on the list and return the sorted list.
        """
        # get the length of the list provided 
        length = len(self.lst)
        
        # iterate over the list
        for i in range(length-1):
            # i - in each iteration represents the first element of the unsorted array 
            
            min_index = i # consider the index of the first element of the unsorted array as the index for the minimum element
            
            # iterate over the array to the right of the first element of the unsorted array 
            for j in range(i+1,length):
                # find the minimum element 
                if(self.lst[j]<self.lst[min_index]):
                    min_index=j
            
            # Since i - represents the index of the first element of the unsorted array and the min_index represents the index of the minimum element in the unsorted array , we can SWAP them now 
            self.lst[i], self.lst[min_index] = self.lst[min_index], self.lst[i]
            
        return self.lst

if __name__=="__main__":
    input_array = [64, 25, 12, 22, 11]
    sorter = SelectionSort(input_array)
    sorted_array = sorter.sort()

    print("Input array:", input_array)
    print("Sorted array:", sorted_array) 
                
            