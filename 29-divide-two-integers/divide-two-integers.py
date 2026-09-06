class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        # Try the largest powers of 2 first
        for i in range(31, -1, -1):

            if (b << i) <= a:
                a -= (b << i)
                quotient += (1 << i)

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient
        