from sympy import singularities, symbols, limit, Reals, Complement

class Calculus:
    def __init__(self, fx):
        self.x = symbols('x')
        self.fx = fx

    def get_domain(self):
        """ Summary: find the domain of the function
            Parameters:
                1.fx: function.
                2.x: variable.
            Returns:
            _list_: [singularity, domain] 
        """
        try:
            singularity = singularities(self.fx, self.x)
            domain = Complement(Reals, singularity)
            return [singularity, domain]

        except ZeroDivisionError as e:
            print(f"ZeroDivisionError : {e}")
        
    def continuous_function(self, x0):
        """ Check the continuity of the function at point x0.
            Parameters:
                x0 (float, int): The point at which continuity is checked.

            Returns:
                bool: Returns True if the function is continuous at x0, otherwise returns False.

            Process:
                1. Check if x0 is a singularity point of the function.
                2. Calculate the left-hand and right-hand limits of the function at x0.
                3. Compare the left-hand and right-hand limits with the function's value at x0 to determine continuity."""
        singularity = self.get_domain()
        
        # Check if the function is defined at x0
        if x0 in singularity[0]:
            print(f"The function is not continuous at {x0} because {x0} is a singularity point.")
            return False
        else:
            # Calculate the left-hand and right-hand limits at x0
            left_limit = limit(self.fx, self.x, x0, dir='-')
            right_limit = limit(self.fx, self.x, x0, dir='+')
            
            # Calculate the function value at x0
            value_at_x0 = self.fx.subs(self.x, x0)
            
            # Check continuity
            if left_limit == right_limit == value_at_x0:
                print(f"The function is continuous at {x0}")
                return True
            else:
                print(f"The function is not continuous at {x0} because the left/right limits do not equal the function value at {x0}")
                return False
