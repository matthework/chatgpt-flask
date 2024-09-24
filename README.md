# chatgpt-flask

This backend Flask app handles API calls to OpenAI’s ChatGPT model, processes the request, and returns the response to the frontend app.

## How to start app and test locally

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

```
gunicorn -b 127.0.0.1:5000  server:app
```

## How to deploy to AWS Lambda

Need to set up AWS account and install AWS CLI first , then assign required permissions to IAM role.

```
zappa deploy prod
```

```
zappa update prod
```
