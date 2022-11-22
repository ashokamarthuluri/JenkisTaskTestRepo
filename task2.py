import logging
import boto3
from botocore.exceptions import WaiterError

ec2 = boto3.resource('ec2', region_name='us-east-1', aws_access_key_id='AKIA2RPDPUEDDB6LU2H4', aws_secret_access_key= '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')
instance_list = []

for instance in ec2.instances.all():
    if instance.platform != 'windows' and instance.state["Name"] == 'running':
        instance_list.append(instance.id)
print(instance_list)

ssm_client = boto3.client('ssm', region_name='us-east-1', aws_access_key_id='AKIA2RPDPUEDDB6LU2H4', aws_secret_access_key= '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')

response = ssm_client.send_command(
        InstanceIds = instance_list,
        DocumentName = "AWS-RunShellScript",
        Parameters = {
            'commands' : ['mkdir /home/ec2-user/sunil']
        }
    )
print(response)
