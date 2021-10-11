import instaloader
from typing import List


def bad_guys(username: str, password: str) -> List[str]:
    followers = []
    followees = []

    session = instaloader.Instaloader()
    session.login(username, password)

    profile = instaloader.Profile.from_username(session.context, username)
    for i in profile.get_followees():
        followees.append(i.username)

    for i in profile.get_followers():
        followers.append(i.username)

    for user in followers:
        if user in followees:
            followees.remove(user)

    return followees
