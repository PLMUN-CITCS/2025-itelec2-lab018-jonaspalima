import math

def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# Example usage
radius_value = 5
area_result = circle_area(radius_value)

print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
