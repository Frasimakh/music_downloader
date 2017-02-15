import argparse
import os
import vk

from urllib.request import urlretrieve

# Parsing of arguments in command line
parser = argparse.ArgumentParser()
parser.add_argument("app_id", help="id of vk.com application. Example: 5579204", type=int)
parser.add_argument("user_login", help="your login. Example: +380668955648", type=str)
parser.add_argument("user_password", help="your password. Example: 12qr8789", type=str)
args = parser.parse_args()

# creating a folder for music
audio_folder = 'downloaded_audios'
if not os.path.exists(audio_folder):
    os.mkdir(audio_folder)

# authorization to vk.com
session = vk.AuthSession(app_id=args.app_id, user_login=args.user_login, user_password=args.user_password,
                         scope='audio')
api = vk.API(session)


audio_list = api.audio.get()
for track in audio_list:
    try:
        urlretrieve(track['url'], audio_folder + '/' + track['artist'] + ' - ' + track['title'] + '.mp3') # downloading of a track
    except Exception:
        print('Error during downloading {}'.format(track['title']))
    else:
        print(track['title'] + ' - was downloaded')
print('\nDownloading was finished')
