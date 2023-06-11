import six as six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user,timestamp):
        return (
                six.text_type(user['phone']) + six.text_type(timestamp) +six.text_type(user['code'])
        )


account_activation_token = TokenGenerator()
Reg_Token = TokenGenerator()
