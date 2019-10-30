# -*- coding:utf-8 -*-
import requests,json,time
import unittest
#from emp_login import loginmain

class Testlogin(unittest.TestCase):

    def setUp(self):
        # 测试前需执行的操作
        print('========================start==========================')
        self.loginUrl = 'https://tautodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        self.checkUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        self.headers = {'Content-Type': 'application/json'}
        self.checkLocationUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/web/attSetLocation/saveAttSetLocation.mobileHr'

    def tearDown(self):
        # 测试用例执行完后所需执行的操作
        print('=========================stop===================================')

    def login_token():
        # 用户成功登陆后获取token
        loginUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '15921595797504',
                'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['token']

    def login_deptId():
        # 用户成功登陆后获取DeptId
        loginUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '98666751995904',
                'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013',
                'mobile': '13522535090',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['emp']['deptId']

    def test_1_login_token(self):
        # 用户成功登陆
        loginUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '15921595797504',
                'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        print(r.json()['msg'])

    def test_2_loginCheck(self):
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
              'token':Testlogin.login_token()}
        requests1 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
        if requests1.json()['msg'] ==  '打卡成功':
                print(3,requests1.json()['msg'])
        elif requests1.json()['msg'] == '所在部门没有设置打卡地点':
            data1 = {
                'deptId':Testlogin.login_deptId() ,
                'actRadius': 200,
                'locSetName': '接口脚本测试易才集团',
                'locName': '北京市朝阳区建国路56号天洋运河F1栋',
                'longitude': '116.518779',
                'latitude': '39.908654'}
            r = requests.post(self.checkLocationUrl, data=json.dumps(data1), headers=headers)
            print(1, r.status_code, 'testcase:test_start', r.json()['msg'])
            r.json()['msg'] == '考勤地点设置成功'
            requests2 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
            print(2, requests2.json()['msg'], requests2.json()['msg'].encode('utf-8'))
        else:
            print(4, requests1.json()['msg'])


if __name__ == '__main__':
        unittest.main()