import boto3

'''
corrected implementation of atomic counter in boto3
aws code examples repository 
https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/dynamodb#code-examples
update_item
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_item.html
'''

client = boto3.client('dynamodb')
table_name = 'your-table-name-here'

def lambda_handler(event, context): 
    data = client.get_item(TableName=table_name,
                                Key={'id': {"S":"0"}},
                                AttributesToGet=['views-count']
                                )

    current_views =  data["Item"]["views-count"]["N"]

    response = client.update_item(
        TableName = table_name,
        Key = {"id": {"S" : "0"} },
        UpdateExpression = 'SET #vc = #vc + :val',
        ExpressionAttributeNames = {"#vc" : "views-count"},
        ExpressionAttributeValues={':val': {'N': '1'}},
        ReturnValues = "UPDATED_NEW"
        )

    new_views = response["Attributes"]["views-count"]["N"]
    
    return new_views