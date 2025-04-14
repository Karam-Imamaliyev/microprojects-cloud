#  File Uploader to S3

Watch a folder (`to_upload`) and automatically upload files to AWS S3.  
Uploaded files are moved to `uploaded/` for tracking.

## Tech
- Python
- boto3
- watchdog
- AWS S3

## Run Instructions
1. `aws configure`
2. Run `file_uploader.py`
3. Drop files in `to_upload/`


