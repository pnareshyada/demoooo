#txt = "Hello World"[::-1]
#print(txt)

import boto3
client=boto3.client('ec2')
res=client.describe_instances()
for i in res['Reservations']:
    # print("Sg Name= ",i['NetworkInterfaces'][0]['GroupName'],"Id= ",i['NetworkInterfaces'][0]['GroupId'])
    for j in i['Instances']:
        for ln in j['BlockDeviceMappings']:
            # print(ln['DeviceName'],ln['Ebs']['VolumeId'])
            for k in j['Tags']:
            # print("Instance Id=",j['InstanceId'],"Name=",k['Value'])
                for l in j['NetworkInterfaces'][0]['Groups']:
                    print("SgName= ",l['GroupName'],"|","Key_Pair= ",j['KeyName'],\
                        "|","InstanceType= ",j['InstanceType'],"|","EbsVolume= ",ln['Ebs']['VolumeId'])