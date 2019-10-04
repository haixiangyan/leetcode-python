class Solution:
    instance = None
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance
