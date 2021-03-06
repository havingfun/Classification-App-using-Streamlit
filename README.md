# Classification-App-Structure-with-Flask-Streamlit
A DS app structure inspired by CookieCutter with Streamlit for fast UI iteration and Flask for app

![Screenshot](https://raw.githubusercontent.com/havingfun/Classification-App-Structure-with-Flask-Streamlit/master/references/prediction.png)

## How to Run

## With Docker
Build docker image
```
docker build . -t classificationapp:latest
```
Run build image
```
docker run -p 8501:8501 classificationapp
```
Project will be running on
```
http://localhost:8501/
```

## Without Docker
Install the requirements
```
pip install -r requirements.txt
```
Go to the streamlit directory
```
cd streamlit
```
Run streamlit app
```
streamlit run app.py
```
Project will be running on
```
http://localhost:8501/
```
Incase your firewall is enabled, you will have to allow your system to open default streamlit port 8501 by doing
```
ufw allow 8501
```

