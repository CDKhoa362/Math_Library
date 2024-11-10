from sympy import singularities, symbols, limit, Reals, Complement, solveset, sin, cos, simplify, N, sqrt, exp, pi, log, tan
from sympy.sets import FiniteSet


class Calculus:
    def __init__(self, fx, x):
        self.x = x
        self.fx = fx
        self.simplified_fx = simplify(fx)

    def get_domain(self):
        """ Summary: find the domain of the function
            Parameters:
                1.fx: function.
                2.x: variable.
            Returns:
            _list_: [singularity, domain] 
        """
        try:
            # Get singularities of the function before and after simplification
            initial_singularities = singularities(self.fx, self.x)
            simplified_singularities = singularities(self.simplified_fx, self.x)

            # Combine singularities from both expressions
            merged_singularity = initial_singularities.union(simplified_singularities)
            
            if merged_singularity:
                # Find the domain (excluding singularities)
                domain = Complement(solveset(self.fx, self.x, domain=Reals), merged_singularity)
                return merged_singularity, domain
            else:
                # No singularities return R.
                return FiniteSet(), Reals

        except Exception as e:
            print(f"Error in get_domain: {e}")
            return FiniteSet(), FiniteSet()
        
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
        if not isinstance(x0, (int, float)):
            print(f"Invalid input: {x0} is not a valid number.")
            return False
        
        singularities_set, _ = self.get_domain()

        # Check if x0 is a singularity
        if any(singularities_set.contains(x0) for singularity in singularities_set):
            print(f"The function is not continuous at {x0} because {x0} is a singularity point.")
            return False
        
        # Numerically check limits at x0 to improve performance
        left_limit = N(limit(self.simplified_fx, self.x, x0, dir='-'))
        right_limit = N(limit(self.simplified_fx, self.x, x0, dir='+'))

        try:
            value_at_x0 = N(self.simplified_fx.subs(self.x, x0))
        except Exception as e:
            print(f"Error computing function value at {x0}: {e}")
            return False
        
        # Continuity check: if the left and right limits are equal and equal to the function value at x0
        if left_limit == right_limit == value_at_x0:
            print(f"The function is continuous at {x0}")
            return True
        else:
            print(f"The function is not continuous at {x0} because the limits do not match the function value.")
            return False
