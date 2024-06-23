import boto3

s3_client = boto3.client("s3", region_name="ap-northeast-1")

try:
    # バケットのリスト取得
    response = s3_client.list_buckets(
        ExpectedBucketOwner='421643133281'  # 所有者のAWSアカウントIDを指定
    )
    # バケット名のリストを取得
    bucket_names = [bucket['Name'] for bucket in response.get('Buckets', [])]
    print("Buckets owned by 421643133281:", bucket_names)
except boto3.exceptions.Boto3Error as e:
    print(f"An error occurred: {e}")
