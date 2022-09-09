#Function for the solution of https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
def catAndMouse(x, y, z):
    A=abs(x-z)
    B=abs(y-z)
    if A>B:
        print('Cat B')
        return("Cat B")
    elif B>A:
        print('Cat A')
        return ("Cat A")
    elif A==B:
        print('Mouse C')
        return("Mouse C")
