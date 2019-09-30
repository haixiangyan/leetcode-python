class Solution:
    """
    @param emails:
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        emailSet = set()
        for email in emails:
            user, domain = email.split('@')
            localUser = ''.join(user.split('+')[0].split('.'))
            emailSet.add(localUser + '@' + domain)
        return len(emailSet)
