import boto3
import json
import requests
import logging
import sys
import argparse
import time
import os

pid = os.getpid()

parser = argparse.ArgumentParser()
parser.add_argument('--end',type=int , default =10)
args = parser.parse_args()


logging.basicConfig(level=logging.INFO, format='From Client: %(asctime)s - %(process)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

start = 0
end = args.end

for j in range(start, end, 1):

    try:
        endpoint_name = 'all-in-one-ai-stable-diffusion-webui-in-2023-06-04-03-27-34-194'
        boto3_sm_run_client = boto3.client(
            "sagemaker-runtime",
            region_name='us-west-2',
        )
        response_model = boto3_sm_run_client.invoke_endpoint_async(
            EndpointName=endpoint_name,
            ContentType="application/json",
            InputLocation="s3://sagemaker-us-west-2-310850127430/sd.json" 
        )
        output = response_model["OutputLocation"]

    except Exception as e:
        traceback.print_exc()
