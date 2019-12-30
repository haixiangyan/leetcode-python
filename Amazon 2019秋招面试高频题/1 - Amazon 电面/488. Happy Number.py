class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        store = set()

        # If n != 1 then get next happy number
        while n != 1:
            # Check if it is in the hash set
            if n in store:
                # Hash set contains this number, then return False
                return False
            # Add the hash set
            store.add(n)
            # Get happy number
            n = self.get_next_happy_number(n)

        # Return True
        return True

    def get_next_happy_number(self, n):
        next_happy = 0

        while n != 0:
            next_happy += (n % 10) * (n % 10)
            n = n // 10

        return next_happy
