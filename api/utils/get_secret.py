import boto3
import json
from functools import lru_cache

@lru_cache()  # Caché para evitar múltiples llamadas a AWS Secrets Manager
def get_aws_secret(secret_name:str,region_name:str="us-east-1"):
    try:
        # Crear cliente de AWS Secrets Manager
        client = boto3.client("secretsmanager", region_name=region_name)
        response = client.get_secret_value(SecretId=secret_name)

        # Convertir el secreto a un diccionario
        secret_dict = json.loads(response["SecretString"])

        # Construir el string de conexión con los valores obtenidos
        return f"postgresql+asyncpg://{secret_dict['username']}:{secret_dict['password']}@{secret_dict['host']}:{secret_dict['port']}/{secret_dict['dbname']}"
    
    except Exception as e:
        print(f"Error Getting AWS Secret: {e}")
        raise