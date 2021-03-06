''' Question from CODEWARS
Arr.diff(8kyu):
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
ex: 
    It should remove all values from list a, which are present in list b.
    array_diff([1,2],[1]) == [2]
    
    If a value is present in b, all of its occurrences must be removed from the other:
    array_diff([1,2,2,2,3],[2]) == [1,3]
    
    https://www.codewars.com/kata/array-dot-diff 
    
'''    
    
    Code:
    
    def array_diff(a, b):
    return [value for value in a if value not in b]
