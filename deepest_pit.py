# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#https://app.codility.com/c/run/MZBGKT-YSD


def deepest_pit(A):
    # write your code in Python 3.6
    size = len(A)

    if size < 3:
        return -1
    #bool increasing represents the previous changing trend, increasing (True) or decreasing (False)
    increasing = True
    #turnpoint is a point when it's a local min/max or it's value is equal to the value of point that is before it
    #turnpoint is reset when current increasing/decreasing trend changes, or the value of current point is equal to that of the point before it.
    turnpoint = 0

    #decrease represents the value that has been decreased (distance between A[turnpoint] and current point which is i-1)
    decrease = 0

    #return value
    rtn = 0
    for i in range(1, size):
        #strictly increasing

        if A[i] == A[i - 1]:
            #reset, since strict monotone is required
            turnpoint = i - 1
            decrease = 0
            increasing = True
            if not increasing:
                #then abandon all values and start next iteration
                continue


        else:
            #state represents if the current step is increasing (True) or decreasing (False)
            state = A[i] > A[i-1]
            if state != increasing:
                increasing = state
                decrease = A[turnpoint] - A[i - 1] if increasing else 0
                turnpoint = i - 1

        rtn = max(rtn, min(A[i] - A[turnpoint], decrease))
    return -1 if rtn == 0 else rtn
