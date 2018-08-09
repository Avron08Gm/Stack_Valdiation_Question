def main():
    stack = list()     # Considering a simple list to be a stack
    top = -1           # index of topmost element. Initialized with -1 as no element is set as start

    ind = 0 

    a = [ 1,2,3,4,5 ]   # Order of the stack to be followed for push operation
    b = [ 1,4,3,5,2 ]   # Given order of elements after possible push operation(s)

    l = len(a)

    d = dict()          # Using dictionary of Python as a hashmap

    for i in range(l):
        d.update( { a[i] : [1,i] } )


    for i in range(l):
        d[ b[i] ][0] -= 1

        # addition of elements if stack is empty
        if len(stack) == 0 and d[ b[i] ][0] >= 0 :   
            stack += a[ ind : d[ b[i] ][1] + 1] 
          
            top += d[ b[i] ][1] + 1 - ind 
            ind = d[ b[i] ][1] + 1
           
            stack.pop()
            top -= 1
        
        # index (or position) based comparison of elements (and also for checking duplicate elements)
        elif d[ b[i] ][0] < 0 or d[ stack[top] ][1] > d[ b[i] ][1]: 
            print("\nOutput : INVALID STACK")
            return
        
        # addition of elements if stack is not empty and push operation(s) is occuring
        elif d[ stack[top] ][1] < d[ b[i] ][1]:
            stack += a[ ind : d[ b[i] ][1] + 1 ] 

            top += d[ b[i] ][1] + 1 - ind 
            ind = d[ b[i] ][1] + 1
            
            stack.pop()
            top -= 1
        
        else :
            stack.pop()
            top -= 1

    print("\nOutput : VALID STACK")
    return 


if __name__ == "__main__":
    main()