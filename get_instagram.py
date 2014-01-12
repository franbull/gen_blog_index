from instagram.client import InstagramAPI

from instagram_access_token import access_token

def get_photos():
    photos = []
    api = InstagramAPI(access_token=access_token[0])
    recent_media, next = api.user_recent_media(user_id=access_token[1]['id'], count=10)
    for media in recent_media:
        photos.append([media.images['standard_resolution'].url, media.caption.text])
    return photos

if __name__ == '__main__':
    print get_photos()
