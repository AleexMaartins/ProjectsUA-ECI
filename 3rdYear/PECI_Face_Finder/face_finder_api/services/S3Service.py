import io
from PIL import Image
from dotenv import load_dotenv
from models.Photo import Photo
import boto3
import os


load_dotenv()
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
s3_client = boto3.client('s3',
                         region_name=os.getenv("AWS_REGION_NAME"),
                         aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                         aws_secret_access_key=os.getenv(
                             "AWS_SECRET_ACCESS_KEY")
                         )


class S3Service:
    def get_photo_url(self, imageKey: str):
        url = s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': S3_BUCKET_NAME,
                'Key': imageKey,
                'ResponseContentType': 'image/jpeg'
            },
            ExpiresIn=3600,
        )
        return url

    def upload_image(self, fileKey, fileBytes):
        s3_client.put_object(Bucket=S3_BUCKET_NAME,
                             Key=fileKey, Body=fileBytes)

    async def get_image_by_key(self, fileKey):
        bucket = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=fileKey)
        image = bucket['Body'].read()
        return Image.open(io.BytesIO(image))

    def delete_image(self, fileKey):
        s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=fileKey)

    def create_person_dir(self, user_id, album_id, person_name):
        s3_client.put_object(Bucket=S3_BUCKET_NAME,
                             Key=f'{user_id}/{album_id}/{person_name}/')
        
    def delete_thumbs(self, user_id, album_id):
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=f"{user_id}/{album_id}/album_thumbnail/")
        if 'Contents' in response:
            for obj in response['Contents']:
                s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=obj['Key'])

    def download_image(self, file_key):
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=file_key)
        return response['Body'].read()
    