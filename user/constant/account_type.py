class AccountType:
    FACEBOOK = '1'
    GOOGLE = '2'


class VerboseAccountType:
    FACEBOOK = 'facebook'
    GOOGLE = 'google'


AccountTypeChoices = (
    (AccountType.FACEBOOK, VerboseAccountType.FACEBOOK),
    (AccountType.GOOGLE, VerboseAccountType.GOOGLE)
)
