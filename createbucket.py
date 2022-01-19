import boto3
from boto3.s3.transfer import S3Transfer
import os
import logging
from botocore.exceptions import ClientError
import trp
from display import main

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        print(1)
        logging.error(e)
        return False
    return True


def upload_file_s3():
    # upload file to s3 bucket
    bucket = 'arthashastra-1'
    s3_client = boto3.client('s3')
    transfer = S3Transfer(s3_client)
    rootdir = 'C:/Users/lenovo/PycharmProjects/aws-textract/Images/'

    for folder in os.listdir(rootdir):

        folderdir = rootdir+folder
        for pages in os.listdir(folderdir):
            print('pages :' + pages)
            keys = folder+'/'+pages
            print(keys)
            transfer.upload_file(folderdir+'/'+pages,bucket,  keys)
        print('==============')
    #return "ALL FILES SUCCESSFULLY UPLOADED"




def textract_job():
    s3_client = boto3.client('s3')
    tess = boto3.client('textract', region_name='ap-south-1')
    bucket = 'arthashastra-1'


    output_file = 'Output.csv'
    path = 'C:/Users/lenovo/PycharmProjects/aws-textract/Images'
    with open(output_file, "wt") as fout:
        files = os.listdir(path)
        for file in files:
            fle = os.listdir(path+'/'+file)
            for f in fle:
                file_name = path+'/'+file+'/'+f
                print(f)
                main(file_name,fout)


        #printing Table Data
        ''' response = tess.analyze_document(
            Document = {
                #'Bytes' = bytes_image
                'S3Object' :{
                    'Bucket' : bucket,
                    #'Name': 's3://mybuck-artha2/img-1.jpg'
                    'Name': key
                }
            },
            FeatureTypes = [ 'TABLES'])

        #print(response)
        doc = trp.Document(response)
        print("============== TABLE DATA ================" , key)
        for page in doc.pages:
            for table in page.tables:
                for r,row in enumerate(table.rows):
                    iterName = ""
                    for c,cell in enumerate(row.cells):
                        print("Table[{}][{}] = {}".format(r,c,cell.text))
                        



#create_bucket('arthashastra-2','ap-south-1')
#upload_file_s3()
#textract_job()  '''