# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return n
        return self.guessRange(1,n)
    
    def guessRange(self,cn,n):

        #if range is within 1 e.g. x,x+1
        if (n-cn) == 1:
            return cn if guess(cn) == 0 else n
            
        #if range more than one
        mid = int((cn+n)/2.0)
        result = guess(mid)
        print("Guess N=%d,r=%d,min=%d,max=%d,mid=%d" %(cn,result,cn,n,mid))        
        if result == 0:
            return mid
        elif result > 0:
            
            return self.guessRange(mid,n)
        else:
            return self.guessRange(cn,mid)

