import math

def P(object):
    """
    A Method to:
    ------------
    - print the given object
    """
    print(object)

class Normal:
    """
    A Class for a Normal Distribution.
    """
    def __init__(self, mean, variance):
        """
        A Method to:
        ------------
        - initialize the Normal distribution with mean and variance
        - calculate and store the standard deviation
        """
        if variance > 0:
            self.mean = mean
            self.variance = variance
            self.standard_deviation = (variance)**(1/2)
            return
        raise ValueError("Invalid Value(s)")
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Normal distribution's parameters
        - returns the string
        """
        return f"Normal({self.mean}, {self.variance})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()


    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer/distribution to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - add another Normal distribution, float or int to the distribution
        '''
        if isinstance(other, Normal) and (self.variance>0) and (other.variance>0):
            return Normal(self.mean + other.mean, self.variance + other.variance)
        if (isinstance(other, float) or isinstance(other, int)) and (self.variance>0):
            return Normal(self.mean + other, self.variance)
        raise ValueError("Invalid Value(s)")
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - subtract another Normal distribution, float or int from the distribution
        '''
        if isinstance(other, Normal) and (self.variance>other.variance) and (other.variance>0):
            return Normal(self.mean - other.mean, self.variance - other.variance)
        if (isinstance(other, float) or isinstance(other, int)) and (self.variance>0):
            return Normal(self.mean - other, self.variance)
        raise ValueError("Invalid Value(s)")
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - multiply the distribution by a float or int
        '''
        if (isinstance(other, float) or isinstance(other, int)) and (self.variance>0) and (other>0):
            return Normal(self.mean * other, self.variance * ((other)**(2)))
        raise ValueError("Invalid Value(s)")
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
        A Method to:
        ------------
        - divide the distribution by a float or int
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.multiply(1 / other)
        return NotImplemented
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - return 0 as the probability of a continuous distribution
        '''
        if (self.variance>0):
            return 0
        raise ValueError("Invalid Value(s)")
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than other
        - return the probability
        '''
        x = other
        if (self.variance>0):
            standard_deviation = (self.variance)**(1/2)
            z_x = (x - self.mean)/standard_deviation
            firstpart = (math.sqrt(math.pi)*math.erf(z_x/(math.sqrt(2))))/math.sqrt(2) - (math.sqrt(math.pi)*math.erf(math.inf/(math.sqrt(2))))/math.sqrt(2)
            probability = 1/math.sqrt(2*math.pi)*firstpart + 1
            return probability
        raise ValueError("Invalid Value(s)")
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than or equal to other
        - return the probability
        '''
        return self.less_than(other)
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than other
        - return the probability
        '''
        x = other
        if (self.variance>0):
            standard_deviation = (self.variance)**(1/2)
            z_x = (x - self.mean)/standard_deviation
            firstpart = (math.sqrt(math.pi)*math.erf(math.inf/(math.sqrt(2))))/math.sqrt(2) - (math.sqrt(math.pi)*math.erf(z_x/(math.sqrt(2))))/math.sqrt(2)
            probability = 1/math.sqrt(2*math.pi)*firstpart
            return probability
        raise ValueError("Invalid Value(s)")
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than or equal to other
        - return the probability
        '''
        return self.greater_than(other)
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

class Binomial:
    """
    A Class for a Binomial Distribution.
    """
    def __init__(self, number_of_trials, probability_of_success):
        """
        A Method to:
        ------------
        - initialize the Binomial distribution with number of trials and probability of success
        - calculate and store the mean, variance, and standard deviation
        """
        self.number_of_trials = number_of_trials
        self.probability_of_success = probability_of_success
        self.mean = self.number_of_trials * self.probability_of_success
        self.variance = self.mean * (1-self.probability_of_success)
        self.standard_deviation = self.variance ** 0.5
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Binomial distribution's parameters
        - returns the string
        """
        return f"Binomial({self.number_of_trials}, {self.probability_of_success})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()



    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - add two binomial distributions together
        - return an error if any other calculation is attempted
        '''
        if isinstance(other, Binomial) and self.probability_of_success == other.probability_of_success:
            return Binomial(number_of_trials = self.number_of_trials + other.number_of_trials, probability_of_success = self.probability_of_success)
        raise ValueError("Will not produce a Binomial output")
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - call the add function on the negative value
        - return an error if not an integer or float
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.add(other * -1)
        return NotImplemented
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - return an error - this is not possible for binomial distributions
        '''
        return NotImplemented
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
         A Method to:
        ------------
        - return an error - this is not possible for binomial distributions
        '''
        return NotImplemented
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - caluclate the probability of success
        '''
        probability = math.comb(self.number_of_trials, other) * (self.probability_of_success ** other) * ((1 - self.probability_of_success) ** (self.number_of_trials - other))
        return probability
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than other
        '''
        if not (isinstance(other, int)):
            raise ValueError("must be an integer")
        probability = 0.0
        for i in range(other):
            probability += math.comb(self.number_of_trials, i) * (self.probability_of_success ** i) * ((1 - self.probability_of_success) ** (self.number_of_trials - i))
        return probability
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than or equal to other
        '''
        return self.less_than(other + 1)
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than other
        '''
        return 1 - self.less_than_equal_to(other)
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than or equal to other
        '''
        return 1 - self.less_than(other)
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

class Geometric:
    """
    A Class for a Geometric Distribution.
    """
    def __init__(self, p):
        """
        A Method to:
        ------------
        - initialize the Geometric distribution with probability of success
        - calculate and store the mean, variance, and standard deviation
        """
        if 0<p<1:
            self.p = p
            self.mean = (1-p)/p
            self.variance = (1-p)/(p**2)
            self.standard_deviation = self.variance ** 1/2
        else:
            raise ValueError("Invalid Value(s)")
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Geometric distribution's parameters
        - returns the string
        """
        return f"Geometric({self.p})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()


    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - raise an error as this is not possible for geometric distributions
        '''
        raise TypeError("Does not produce a Geometric output")
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - raise an error as this is not possible for geometric distributions
        '''
        raise TypeError("Does not produce a Geometric output")
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - raise an error as this is not possible for geometric distributions
        '''
        raise TypeError("Does not produce a Geometric output")
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
        A Method to:
        ------------
        - raise an error as this is not possible for geometric distributions
        '''
        raise TypeError("Does not produce a Geometric output")
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - return P(X==1)
        '''
        return "P(X==1)"
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than other
        - return the probability
        '''
        x = other
        if (0<self.p<1) and (x>1):
            x = x-1
            probability = 1 - (1-self.p)**(x)
            return probability
        raise ValueError("Invalid Value(s)")
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than or equal to other
        - return the probability
        '''
        x = other
        if (0<self.p<1) and (x>0):
            probability = 1 - (1-self.p)**(x)
            return probability
        raise ValueError("Invalid Value(s)")
    
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than other
        - return the probability
        '''
        x = other
        if (0<self.p<1) and (x>1):
            x = x-1
            probability = (1-self.p)**(x)
            return probability
        raise ValueError("Invalid Value(s)")
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than or equal to other
        - return the probability
        '''
        x = other
        if (0<self.p<1) and (x>0):
            probability = (1-self.p)**(x)
            return probability
        raise ValueError("Invalid Value(s)")
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

class Poisson:
    """
    A Class for an Example Distribution.
    """
    def __init__(self, rate):
        """
        A Method to:
        ------------
        - initialize the Poisson distribution with a rate parameter
        - calculate and store the mean, variance, and standard deviation
        """
        self.rate = rate
        self.mean = self.rate
        self.variance = self.rate
        self.standard_deviation = self.rate ** 0.5
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Poisson distribution's parameters
        - returns the string
        """
        return f"Poisson({self.rate})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()

    def poisson_pmf(k, rate):

        '''
        A Method to:
        ------------
        - Calculate the pmf of a distribution.
        - checks if k and rate are greater than or equal to 0.
        - if so it returns the pmf.
        - if not it raises the "Invalid Value(s)" error.
        '''
        if (k>=0 and rate>=0):
            
            return (rate**k * math.exp(-rate)) / math.factorial(k)

        else:
            raise ValueError("Invalid Value(s)")

    '''----------------------------------------------------------------------------------------------------------------------'''

    def poisson_cdf(k, rate):

        '''
        A Method to:
        ------------
        - Calculate the cdf of a distribution.
        - checks if k and rate are greater than or equal to 0.
        - if so it returns the cdf.
        - if not it raises the "Invalid Value(s)" error.
        '''
        cdf = 0
        if (k>=0 and rate>=0):
            
            for i in range(k+1):
                cdf += Poisson.poisson_pmf(i,rate)
            return cdf
        else:
            raise ValueError("Invalid Value(s)")

    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - Add two poisson distributions.
        - if not it raises the "Invalid Value(s)" error.
        '''
        if isinstance(other,Poisson):
            return Poisson(self.rate + other.rate)
        raise ValueError("Invalid Value(s)")
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - subtract a value from the poisson distribution
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.add(other * -1)
        return NotImplemented
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - returns not implemented
        '''
        return NotImplemented
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
        A Method to:
        ------------
        - returns not implemented
        '''
        return NotImplemented
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - return P(X==1)
        '''
        return "P(X==1)"
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than other
        - return the probability
        '''
        k = other
        if k>1 and self.rate>0:
            return Poisson.poisson_cdf(k-1,self.rate)
        else:
            raise ValueError("Invalid Value(s)")
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than or equal to other
        - return the probability
        '''
        k = other
        if k>0 and self.rate>0:
            return Poisson.poisson_cdf(k,self.rate)
        raise ValueError("Invalid Value(s)")
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than other
        - return the probability
        '''
        k = other
        if k>0 and self.rate>0:
            return 1 - Poisson.poisson_cdf(k,self.rate)
        raise ValueError("Invalid Value(s)")
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than or equal to other
        - return the probability
        '''
        k = other
        if k>1 and self.rate>0:
            return 1 - Poisson.poisson_cdf(k-1,self.rate)
        raise ValueError("Invalid Value(s)")
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

class Uniform:
    """
    A Class for a Uniform Distribution.
    """
    def __init__(self, a, b):
        """
        A Method to:
        ------------
        - initialize the Uniform distribution with parameters a and b
        - calculate and store the mean, variance, and standard deviation
        """
        if a >= b:
            raise ValueError("Inavlid value(s).")
        self.a = a
        self.b = b
        self.mean = (a+b)/2
        self.variance = ((b-a)**2)/12
        self.standard_deviation = self.variance ** (1/2)
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Uniform distribution's parameters
        - returns the string
        """
        return f"Uniform({self.a},{self.b})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()


    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - add a float or int to the distribution
        '''
        if isinstance(other, int) or isinstance(other, float):
            return (self.a + other, self.b + other)
        return NotImplemented
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - subtract a float or int from the distribution
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.add(other * -1)
        return NotImplemented
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - multiply the distribution by a float or int
        '''
        if isinstance(other, int) or isinstance(other, float):
            return (self.a * other, self.b * other)
        return NotImplemented
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
        A Method to:
        ------------
        - divide the distribution by a float or int
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.multiply(1 / other)
        return NotImplemented
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - return 0 as the probability of a continuous distribution
        '''
        return 0 #as continuous
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than other
        - return the probability
        '''
        n = other
        if n <= self.a:
            return 0.0
        elif n >= self.b:
            return 1.0
        else:
            return (n - self.a) / (self.b - self.a)
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being less than or equal to other
        - return the probability (which is the same as less than for continuous distributions)
        '''
        return self.equal_to(other)
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than other
        - return the probability
        '''
        return (1 - self.equal_to(other))
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - calculate the probability of a value being greater than or equal to other
        - return the probability
        '''
        return self.greater_than(other)
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

class Exponential:
    """
    A Class for an Example Distribution.
    """
    def __init__(self, rate):
        """
        A Method to:
        ------------
        - initialize the Exponential distribution with a rate parameter
        - calculate and store the mean, variance, and standard deviation
        """
        self.rate = rate
        self.mean = 1 / rate
        self.variance = 1 / (rate ** 2)
        self.standard_deviation = self.variance ** 0.5
    def parameters(self):
        """
        A Method to:
        ------------
        - create a string representation of the Exponential distribution's parameters
        - returns the string
        """
        return f"Exponential({self.rate})"
    def __repr__(self):
        """
        A Method to:
        ------------
        - call the parameters method when the object is represented as a string
        """
        self.parameters()


    """
    Functionality for algebra of the distributions.
    """
    """ Addition and subtraction of a float/integer to a distribution, with operand overloading"""
    def add(self,other):
        '''
        A Method to:
        ------------
        - returns not implemented
        '''
        return NotImplemented
    def __add__(self,other): # "+"
        return self.add(other)
    def __radd__(self,other): #reverse "+"
        return other.add(self)
    def subtract(self,other):
        '''
        A Method to:
        ------------
        - returns not implemented
        '''
        return NotImplemented
    def __sub__(self,other): # "-"
        return self.subtract(other)
    def __rsub__(self,other): #reverse "-"
        return self.multiply(-1).add(other)
    """ Multiplication and division of a float/integer to a distribution, with operand overloading"""
    def multiply(self,other):
        '''
        A Method to:
        ------------
        - multiply the distribution by a float or int by modifying the rate
        '''
        if isinstance(other, int) or isinstance(other, float):
            return Exponential(self.rate / other)
        return NotImplemented
    def __mul__(self,other): # "*"
        return self.add(other)
    def __rmul__(self,other): #reverse "*"
        return other.add(self)
    def divide(self,other):
        '''
        A Method to:
        ------------
        - divide the distribution by a float or int
        '''
        if isinstance(other, int) or isinstance(other, float):
            return self.multiply(1 / other)
        return NotImplemented
    def __div__(self,other): # "/"
        return self.divide(other)


    """
    Functionality for calculations of probability
    """
    """Probability equal to a value, with operand overloading"""
    def equal_to(self,other): # "=="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being equal to other
        - return the probability
        '''
        return self.rate * math.exp(-1 * self.rate * other)
    def __eq__(self,other):
        return self.equal_to(other)
    def __req__(self,other): # reverse "=="
        return other.equal_to(self)
    """Probability less than [or equal to] to a value, with operand overloading"""
    def less_than(self,other): # "<"
        '''
        A Method to:
        ------------
        - return P(X<1)
        '''
        return "P(X<1)"
    def __lt__(self,other): # "<"
        return self.less_than(other)
    def __rlt__(self,other): # reverse "<"
        return other.greater_than(self)
    def less_than_equal_to(self,other):
        '''
        A Method to:
        ------------
        - return P(X<=1)
        '''
        return "P(X<=1)"
    def __le__(self,other): # "<="
        return self.less_than_equal_to(other)
    def __rle__(self,other): # reverse "<="
        return other.greater_than_equal_to(self)
    """Probability greater than [or equal to] to a value, with operand overloading"""
    def greater_than(self,other):
        '''
         A Method to:
        ------------
        - return P(X>1)
        '''
        return "P(X>1)"
    def __gt__(self,other): # ">"
        return self.greater_than(other)
    def __rgt__(self,other): # reverse ">"
        return other.less_than(self)
    def greater_than_equal_to(self, other):
        '''
        A Method to:
        ------------
        - return P(X>=1)
        '''
        return "P(X>=1)"
    def __ge__(self,other): # ">="
        return self.greater_than_equal_to(other)
    def __rge__(self,other): # reverse ">="
        return other.less_than_equal_to(self)
    """Probability between [or equal to] two values"""
    def between(self, lower, upper): # "< <"
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between lower and upper
        '''
        return (self.less_than(upper) - self.less_than(lower))
    def between_equal_to(self, lower, upper): #"<= <="
        '''
        A Method to:
        ------------
        - calculate the probability of a value being between and equal to lower and upper
        '''
        return (self.less_than_equal_to(upper) - self.less_than_equal_to(lower - 1))

