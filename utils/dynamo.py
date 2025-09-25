import os
import boto3
from boto3.dynamodb.conditions import Key
from typing import Dict, Any

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE", "FinancialResearch")

# boto3 client/resource will use AWS credentials available in the environment or IAM role (Lambda).
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
_table = dynamodb.Table(DYNAMO_TABLE)

def put_item(item: Dict[str, Any]):
    """
    Put an item into DynamoDB table.
    Table must exist and have at least string PK 'pk' and SK 'sk' (or adjust keys).
    """
    if not DYNAMO_TABLE:
        raise EnvironmentError("DYNAMO_TABLE not set")
    return _table.put_item(Item=item)

def get_item(pk: str, sk: str):
    resp = _table.get_item(Key={"pk": pk, "sk": sk})
    return resp.get("Item")

def query_by_pk(pk: str):
    resp = _table.query(KeyConditionExpression=Key("pk").eq(pk))
    return resp.get("Items", [])
