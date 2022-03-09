import boto3
from logger import logger
from botocore.exceptions import NoCredentialsError
from decouple import config
import uuid

ACCESS_KEY = config('S3_ACCESS_KEY')
SECRET_KEY = config('S3_SECRET_KEY')
BUCKET_NAME = config('S3_BUCKET_NAME')

def get_client():
    s3 = boto3.client('s3',  aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    return s3

S3_CLIENT = get_client()

def upload_file(local_file, s3_file, bucket=BUCKET_NAME, client=S3_CLIENT):
    '''
        Upload file from local to S3 
        Params:
            client: s3 client
            local_file: dir of local file 
            s3_file: dir of corresponding local file on S3
            bucket: bucket_name
    '''

    try:
        client.upload_file(local_file, bucket, s3_file)
        print("Upload Successfully")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download_file(local_file, s3_file, bucket=BUCKET_NAME, client=S3_CLIENT):
    '''
        Download file from  S3 to local
        Params:
            client: s3 client
            local_file: dir of local file 
            s3_file: dir of corresponding local file on S3
            bucket: bucket_name
    '''
    try:
        client.download_file(bucket, s3_file, local_file)
        print("Download Successfully")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def upload_project_data(data, user_id, project_id, ext='.csv', bucket=BUCKET_NAME, client=S3_CLIENT):
    prefix = f"user-data/{user_id}/{project_id}/"
    resource = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    bucket_obj = resource.Bucket(BUCKET_NAME)
    files = [obj.key for obj in bucket_obj.objects.filter(Prefix=prefix)]
    while True:
        file_name = str(uuid.uuid4()) + ext
        if file_name not in files:
            client.upload_fileobj(data, bucket, prefix+file_name)
            return file_name

if __name__=="__main__":
    upload_file()
