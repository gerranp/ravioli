import ravioli

'''
A test file, created to ensure functionality of our program.
Due to the large scope of the library this only contains functionality for testing the normal class and functions,
however the similarity in functionality of the classes means this could be scaled up with minor adjustments to cover all distributions. 
'''

def test_framework():
    '''
    This is a defunct test, purely to create a standardised structure for the below tests.
    '''
    normal_distribution_1 = ravioli.Normal(1,0)
    normal_distribution_2 = ravioli.Normal(1,0)
    new_normal_distribution = normal_distribution_1
    expected_outcome_normal_distribution = ravioli.Normal(1,0)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_addition_two_distributions():
    '''
    This tests the addition capabilities for the binomial class - two distributions
    '''
    normal_distribution_1 = ravioli.Normal(mean=2,variance=5)
    normal_distribution_2 = ravioli.Normal(mean=4,variance=10)
    new_normal_distribution = normal_distribution_1.add(normal_distribution_2)
    expected_outcome_normal_distribution = ravioli.Normal(mean=6,variance=15)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_addition_float():
    '''
    This tests the addition capabilities for the binomial class - addition of a float
    '''
    normal_distribution_1 = ravioli.Normal(mean=2,variance=5)
    new_normal_distribution = normal_distribution_1.add(1.5)
    expected_outcome_normal_distribution = ravioli.Normal(mean=3.5,variance=5)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_subtraction_two_distributions():
    '''
    This tests the subtraction capabilities for the binomial class - two distributions
    '''
    normal_distribution_1 = ravioli.Normal(mean=15,variance=20)
    normal_distribution_2 = ravioli.Normal(mean=4,variance=10)
    new_normal_distribution = normal_distribution_1.subtract(normal_distribution_2)
    expected_outcome_normal_distribution = ravioli.Normal(mean=11,variance=10)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_subtraction_float():
    '''
    This tests the subtraction capabilities for the binomial class - subtraction of a float
    '''
    normal_distribution_1 = ravioli.Normal(mean=7,variance=15)
    new_normal_distribution = normal_distribution_1.subtract(2)
    expected_outcome_normal_distribution = ravioli.Normal(mean=5, variance=15)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_multiplication_float():
    '''
    This tests the functionality of multiplying a Normal class by a float
    '''
    normal_distribution_1 = ravioli.Normal(mean=4,variance=1)
    new_normal_distribution = normal_distribution_1.multiply(3)
    expected_outcome_normal_distribution = ravioli.Normal(mean=12,variance=9)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"

def test_normal_division_float():
    '''
    This tests the functionality of dividing a Normal class by a float
    '''
    normal_distribution_1 = ravioli.Normal(mean=24, variance=16)
    new_normal_distribution = normal_distribution_1.divide(4)
    expected_outcome_normal_distribution = ravioli.Normal(mean=6,variance=1)
    result_boolean = (new_normal_distribution.mean == expected_outcome_normal_distribution.mean) and (new_normal_distribution.variance == expected_outcome_normal_distribution.variance)
    assert result_boolean, "Function did not return expected output"


def test_normal_equal_to():
    '''
    A test to confirm functionality of P(X=x)
    This should return 0 as it is a continuous distribution.
    '''
    normal_distribution_1 = ravioli.Normal(mean=9,variance=2)
    calculated_result = normal_distribution_1.equal_to(7)
    expected_outcome = 0
    result_boolean = calculated_result == expected_outcome
    assert result_boolean, "Function did not return expected output"

def test_normal_less_than():
    '''
    A test to confirm functionality of P(X<x) and, by extension, P(X<=x) as these are identical
    '''
    normal_distribution_1 = ravioli.Normal(mean=5,variance=6)
    calculated_result = normal_distribution_1.less_than(2)
    expected_outcome = 0.11033568095992352
    result_boolean = calculated_result == expected_outcome
    assert result_boolean, "Function did not return expected output"

def test_normal_greater_than():
    '''
    A test to confirm functionality of P(X>x) and, by extension, P(X>=x) as these are identical
    '''
    normal_distribution_1 = ravioli.Normal(mean=7,variance=4)
    calculated_result = normal_distribution_1.greater_than(3)
    expected_outcome = 0.9772498680518208
    result_boolean = calculated_result == expected_outcome
    assert result_boolean, "Function did not return expected output"

def test_normal_between_values():
    '''
    A test to confirm functionality of P(x1<X<x2) and, by extension, P(x1<=X<=x2) as these are identical
    '''
    normal_distribution_1 = ravioli.Normal(mean=2,variance=7)
    calculated_result = normal_distribution_1.between(lower=1,upper=9)
    expected_outcome = 0.6431960211476119
    result_boolean = calculated_result == expected_outcome
    assert result_boolean, "Function did not return expected output"


test_normal_addition_two_distributions()
test_normal_addition_float()
test_normal_subtraction_two_distributions()
test_normal_subtraction_float()
test_normal_multiplication_float()
test_normal_division_float()
test_normal_equal_to()
test_normal_greater_than()
test_normal_less_than()
test_normal_between_values()