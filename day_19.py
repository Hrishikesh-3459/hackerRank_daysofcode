class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
import math
class Calculator(AdvancedArithmetic):
    def divisorSum(self, x):
        x = []
        i = 1
        while i <= math.sqrt(n): 
            if (n % i == 0) : 
                if (n / i == i) : 
                    x.append(i)
                else : 
                    x.append(i)
                    x.append(n/i)
            i = i + 1
        return int(sum(x))

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
