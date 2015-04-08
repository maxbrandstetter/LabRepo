"""
The following code determine if a set of 4 values is a square or a rectangle
"""

def determine_square_or_rectangle(a=0, b=0, c=0, d=0):
        """
        Determine if the given sides form a square or rectangle

        :param a: line a
        :type a: float or int

        :param b: line b
        :type b: float or int
        
        :param c: line c
        :type c: float or int
        
        :param d: line d
        :type d: float or int

        :return: "square", "rectangle", or "invalid"
        :rtype: str
        """
	if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
		return "invalid"	
	
	if a <= 0 or b <= 0 or c <= 0 or d <= 0:
		return "invalid"
	
	if a == b and b == c and c == d:
		return "square"
		
	if a == b and c == d or a == c and b == d or a == d and b == c:
		return "rectangle"
