# Images with AWS Textract


import boto3
from boto3.s3.transfer import S3Transfer
import trp
import os
from pdf2Image import convert_pdf
from createbucket import create_bucket,upload_file_s3,textract_job

class Conversion:
    root_dir = 'C:/Users/lenovo/PycharmProjects/aws-textract/Data/'
    def convert_pdf_img(self):
        for i in os.listdir('C:/Users/lenovo/PycharmProjects/aws-textract/Data'):
            print(i)

            convert_pdf(self.root_dir + i, 'C:/Users/lenovo/PycharmProjects/aws-textract/Images/',res = 400)


class activate_s3_textract:
    def start_job(self):
        # creates a new s3 bucket with the name,region you mention
        #create_bucket(bucket_name='arthashastra-1',region='ap-south-1')
        # uploads the files to the given bucket
        #upload_file_s3()
        #starts the textract job and prints the table results
        textract_job()





if __name__ == '__main__':
    # pdf to image conversions
    #con = Conversion()
    #con.convert_pdf_img()

    # creating buckets , uploading files to s3 buckets and getting the results
    start = activate_s3_textract()
    start.start_job()
