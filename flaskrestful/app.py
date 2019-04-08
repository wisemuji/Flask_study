from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
CORS(app)
title = 'my homepage'
api = Api(app=app)


class HealthCheck(Resource):

def get(self):
'''
사용자가 보낸 parameter를 통해
데이터를 보내줍니다.
:return:
'''
return {'msg': 'get ok'}

def post(self):
'''
사용자가 보낸 session 정보를 통해
수정 역할을 합니다.
:return: 수정 여부를 반환합니다.
'''
return {'msg': 'post ok'}

def put(self):
'''
사용자가 보낸 데이터를 저장한다.
:return:
'''
return {'msg': 'put ok'}

def delete(self):
'''
데이터를 삭제한다.
:return:
'''
return {'msg': 'delete ok'}


api.add_resource(HealthCheck, '/v0.0/test')

if __name__ == '__main__':
app.run(debug=True, port=5002)
