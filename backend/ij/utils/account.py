from ij.models import City, UserProfile

def get_or_create_user_by_email(email):
    print('Creating--'+email)
    try:
        user = UserProfile.objects.get(username=email)
        return user
    except:
        user = UserProfile()
        user.publicname = email
        user.username = email
        user.set_password('123456')
        user.save()
        return user
