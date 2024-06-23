import boto3

s3_client = boto3.client("s3",region_name = "ap-northeast-1")

try:
  s3_client.delete_bucket(
    Bucket = "config-421643133281",
    ExpectedBucketOwner='421643133281'
  )

except s3_client.exceptions.NoSuchBucket:
  print("The specified bucket does not exist.")

except boto3.exceptions.Boto3Error as e:
  print(f"An error occurred: {e}")

else:
  print("Bucket deleted successfully.")
finally:
  print('Finish')
