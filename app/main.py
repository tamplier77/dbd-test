from flask import Flask
import boto3

table_name='devops-challenge'
region='us-east-1'
code_name='thedoctor'

conn = boto3.resource('dynamodb', region_name=region,aws_access_key_id=id,aws_secret_access_key=key)

app = Flask(__name__)

@app.route("/")
def main():
    return "Looks OK."

@app.route("/secret")
def secret():
    table = conn.Table(table_name)
    response = table.get_item(Key={'code_name': 'thedoctor'})
    item = "{ secret_code: " + response['Item']['secret_code'] + "}"
    return item

@app.route("/health")
def health():
    return "{ status: healthy, container: https://hub.docker.com/r/tamplier77/challenge/, project: github.com/tamplier77/dbd-test }"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

