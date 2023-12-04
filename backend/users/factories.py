import datetime
import factory

from . import objects


class AccountFactory(factory.Factory):
    class Meta:
        model = objects.User

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)


class ProfileFactory(factory.Factory):
    class Meta:
        model = objects.UserProfile

    account = factory.SubFactory(AccountFactory)
 #   gender = factory.Iterator([objects.Profile.GENDER_MALE, objects.Profile.GENDER_FEMALE])
 #   firstname = 'John'
 #   lastname = 'Doe'