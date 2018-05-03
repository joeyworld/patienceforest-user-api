# Patience Forest(인내의 숲) User API
디프만 4기 2차 미니프로젝트 의 USER API 입니다.

## Installation

Python 3.4 이상과 호환 (Django 2.0 사용)

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

## Deployment

`stage` : either `dev` or `production`

```
$ zappa deploy <stage>
```

`master` 브랜치에 정상적으로 머지 시 자동 배포됨

## API Documentation
(WIP)

