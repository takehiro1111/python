import boto3

s3_client = boto3.client("s3",region_name = "ap-northeast-1")

s3_client.create_bucket(
  Bucket = "test-test-20240623",
  # us-east-1以外の場合は必要なパラメータ
  CreateBucketConfiguration = {
    'LocationConstraint' : 'ap-northeast-1'
  }
)

