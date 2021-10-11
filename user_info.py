from find_bad_guys import bad_guys
import instaloader


def get_info(username: str, password: str) -> object:
    
    """
    Get bad guys and some info about IG user
    
    You may extend functionality of this module if you wish
    """
    
    bguys = bad_guys(username, password)

    session = instaloader.Instaloader()
    session.login(username, password)
    profile = instaloader.Profile.from_username(session.context, username)
    user_id = profile.userid
    # number of posts in profile
    media_count = profile.mediacount

    return {'User id': user_id, 'Media count': media_count, 'Bad guys count': len(bguys), 'Bad guys': bguys}


if __name__ == '__main__':
    username = input('username: ')
    password = input('password: ')

    print('Now HTTP session is opened')
    print(get_info(username, password))
    print('Execution completed')
