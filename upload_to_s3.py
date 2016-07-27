from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
from datetime import datetime
import sys

date=datetime.now()
cur_date_time=date.strftime('%Y%m%d-%H%M')


log_dir='/var/log/mysql'
AWS_ACCESS_KEY_ID='XXXX'
AWS_SECRET_KEY='XXXXXX'
bucket_name='nadeem3680'
conn=S3Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_KEY)

''' create a new  bucket if not exists '''
def create_bucket():
   try:
      conn.create_bucket('nadeem3680')
   except Exception as e:
      print e

''' upload files to s3 bucket '''
bucket=conn.get_bucket('nadeem3680')
key=Key(bucket)
def upload_to_s3():
  try:
     for file in os.listdir(log_dir):
        if os.path.isfile(os.path.join(log_dir,file)):
           key.key=file+cur_date_time
           key.set_contents_from_filename(os.path.join(log_dir,file))
     print "OK"
     sys.exit(0)
  except Exception as e:
    print "WARNING - %s" % e
    sys.exit(1)
upload_to_s3()
