# 目的:指定したS3バケットからオブジェクトをGETし、Rekognitionでコンテンツを検出する

import pprint
import boto3

my_session = boto3.Session(profile_name='sekigaku')
s3 = my_session.client("s3")
recognition = my_session.client('rekognition')

env_bucket = "boto3-bucket-takehiro1111"

def main():
  response = s3.list_objects_v2(
    Bucket= env_bucket,
  )
  #pprint.pprint(response)
  for i in response['Contents']:
    object_name = i["Key"]
    print(object_name)

    image_label = recognition.detect_labels(
      Image={
        'S3Object': {
          'Bucket': env_bucket,
          'Name': object_name,
        }
      }
    )
    pprint.pprint(image_label)

# 関数の呼び出し
main()
