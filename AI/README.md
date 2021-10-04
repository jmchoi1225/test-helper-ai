# test-helper AI
( 비고 ) README 및 폴더 구조는 나중에 변경될 것 같습니다 !! 


## How to start
### 1. 가상환경 만들기
#### 1-1. virtual env 로 생성
```
$ python3 -m venv venv
$ source ./venv/bin/activate
```
<br />

#### 1-2. anaconda로 생성
```
$ conda create -n venv python=3
$ activate venv
```
<br />
<br />

### 2. requirements.txt 다운받기
`$ pip install -r requirements.txt`
<br />
<br />


### 3. root 폴더에 .env 파일 생성 후, key 넣기
(아직 넣을 일 없지만, api 가져올 때 필수 !)
<br />
<br />


### 4. flask 실행하기
#### 4-1. deployment
`$ export FLASK_ENV=deployment`
<br />

#### 4-2. flask run
`$ flask run`
<br />

#### 4-3. localhost:5000 접속 
browser에 http://localhost:5000 입력하여 접속하여 small test helper 결과 보기 !!
<br />