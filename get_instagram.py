from instagram.client import InstagramAPI

from instagram_access_token import access_token

def get_photos():
    photos = []
    api = InstagramAPI(access_token=access_token[0])
    recent_media, next = api.user_recent_media(user_id=access_token[1]['id'], count=5)
    for media in recent_media:
        caption_text = ''
        if media.caption is not None:
            caption_text = media.caption.text
        photos.append([media.images['standard_resolution'].url, caption_text])
    return photos

if __name__ == '__main__':
    print get_photos()
