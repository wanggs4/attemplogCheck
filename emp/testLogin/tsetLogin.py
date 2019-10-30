# -*- coding:utf-8 -*-
import requests,json,time
import unittest

class login(unittest.TestCase):

    def setUp(self):
        print('========================start==========================')
        self.loginUrl = 'https://testapi.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        self.checkUrl = 'https://testapi.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        self.headers = {'Content-Type': 'application/json'}
        self.checkLocationUrl = 'https://testapi.ctgpayroll.com/ehr_saas/web/attSetLocation/saveAttSetLocation.mobileHr'

    def login_token():
        # 获取登录用户token
        loginUrl = 'https://testapi.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '98666751995904',
                'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['token']

    def login_deptId():
        # 获取登录用户deptId
        loginUrl = 'https://testapi.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '98666751995904',
                'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['emp']['deptId']

    def test_loginCheck_01(self):
        # 用户登录打卡
        json_param = {
            'checkType': 1,
            'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
            'latitude': '39.908654',
            'longitude': '116.518779',
            'type': 1,
            'wifiMac': '',
            'wifiName': ''}
        headers = {'Content-Type':'application/json',
              'token':login.login_token()}
        requests1 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
        if requests1.json()['msg'] == '所在部门没有设置打卡地点':
            data1 = {
                'deptId':login.login_deptId() ,
                'actRadius': 200,
                'locSetName': '测试易才集团',
                'locName': '北京市朝阳区建国路56号天洋运河F1栋',
                'longitude': '116.518779',
                'latitude': '39.908654'}
            r = requests.post(self.checkLocationUrl, data=json.dumps(data1), headers=headers)
            print(1, r.status_code, 'testcase:test_start', r.json()['msg'])
            r.json()['msg'] == '考勤地点设置成功'
            requests2 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
            print(2, requests2.json()['msg'], requests2.json()['msg'].encode('utf-8'))
        elif requests1.json()['msg'] ==  '打卡成功':
                print(3,requests1.json()['msg'])
        else:
            print(4, requests1.json()['msg'])

        print(requests1.text)



if __name__ == '__main__':
        unittest.main()