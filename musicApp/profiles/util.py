from profiles.models import Profile


def get_profile() -> Profile | None:
    return Profile.objects.first()
