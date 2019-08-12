import boto3
import instabot
from instabot import Bot 

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    LOCAL_PATH='/backup/s3'
    for record in event['Records']:
        bucket=record['s3']['object']['name']
        key=record['s3']['object']['key']
        keyStr = str(key)
        local_file=LOCAL_PATH+keyStr
        if not os.path.exists(local_file):
            bucket.download_file(key, local_file)
        status = post_to_insta(local_file)


def post_to_insta(self, filename) :
    bot = Bot()
    with open(filename, 'rb') as f:
        imgData=f.read()
    caption = imgData[:-4].split(" ")
    caption = " ".join(caption[1:])
    print("upload: " + caption)
    bot.upload_photo(pic, caption=caption)
    if bot.api.last_response.status_code != 200:
        print(bot.api.last_response)
            # snd msg
        break