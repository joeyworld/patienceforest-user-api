# Patience Forest(인내의 숲) User API
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/a10c88041cf70d60a4b4)

디프만 4기 2차 미니프로젝트 의 USER API 입니다.

## Base URL
https://0t1s29k5b5.execute-api.ap-northeast-2.amazonaws.com/dev/users/  
(Production stage 는 데이터베이스 설정중에 있습니다)

## Installation

Python 3.4 이상과 호환 (Django 2.0 사용),  
pip 10.0 이하와 호환 (pip 10.0 사용시 `zappa` 관련 이슈가 있습니다)

```
$ pip3 install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

가상환경이 정상적으로 활성화 되지 않으면, 다음 명령어로 가상환경 다시 설치
```
$ sudo apt-get install python3-venv
```

pip 버전이 10 이상일 경우, 다음 명령어로 다운그레이드
```
(venv) $ pip install pip==9.0.3
```

## Deployment

`stage` : either `dev` or `production`

```
$ zappa deploy <stage>
```

`master` 브랜치에 정상적으로 머지 시 자동 배포됨

## API Documentation
- Postman docs : [여기](https://documenter.getpostman.com/view/3135479/user-api/RW1ekdSp)서 보실 수 있습니다
- Postman collection : [여기](https://www.getpostman.com/collections/a10c88041cf70d60a4b4)서 다운받으세요

`{{host}}` 를 알맞게 설정하시길 바랍니다!
