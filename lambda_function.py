import json 
import pymysql

endpoint = 'web-dio.cne1a4dp97zd.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'Rafaelav24'
database_name = 'PERMISSIONS_DB'

connection = pymysql.connect(host=endpoint, user=username, password=password, db=database_name)

def lambda_handler(event, context):
    
    cursor = connection.cursor()
    
    cursor.execute('select user.id, user.email, user.username, role.id AS role_id, role.name AS role_name from user join user_roles on (user.id=user_roles.user_id) join role on (role.id=user_roles.role_id)')
    
    rows = cursor.fetchall()
    
    return {
        'statusCode': 200,
        'body': json.dumps(rows)
    }