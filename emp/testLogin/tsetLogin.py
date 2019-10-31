# -*- coding:utf-8 -*-
import requests,json,time
import unittest
from

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
                'custId': '22978355286016',
                'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        # self.assertEqual(r.json()['msg'],'登录成功')
        # return r.json()['result']['data']['token']
        if r.json()['msg'] =='登录成功':
            return r.json()['result']['data']['token']
        else:
            print(r.json()['msg'])

    def login_deptId():
        # 获取登录用户deptId
        loginUrl = 'https://testapi.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '22978355286016',
                'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['emp']['deptId']

    def test_01_loginCheck(self):
        # 用户登录打卡
        json_param = {
            'checkType': 1,
            'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
            'latitude': '39.908654',
            'longitude': '116.518779',
            'type': 1,
            'wifiMac': '',
            'wifiName': ''}
        print(login.login_token())
        headers = {'Content-Type':'application/json',
              'token':login.login_token()}
        requests1 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
        if requests1.json()['msg'] == '所在部门没有设置打卡地点':
            data1 = {
                'deptId':login.login_deptId() ,
                'actRadius': 2000,
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

    def test_02_loginCheck(self):
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
        print(requests1.json()['msg'])
        if self.assertEqual(requests1.json()['msg'],'打卡成功'):
            self.quit()
        elif requests1.json()['msg'] == '所在部门没有设置打卡地点':
            data1 = {
                'deptId':login.login_deptId() ,
                'actRadius': 2000,
                'locSetName': '测试易才集团',
                'locName': '北京市朝阳区建国路56号天洋运河F1栋',
                'longitude': '116.518779',
                'latitude': '39.908654'}
            r = requests.post(self.checkLocationUrl, data=json.dumps(data1), headers=headers)
            print(1, r.status_code, 'testcase:test_start', r.json()['msg'])
            self.assertEqual(r.json()['msg'], '考勤地点设置成功')
            # r.json()['msg'] == '考勤地点设置成功'
            requests2 = requests.post(self.checkUrl, data=json.dumps(json_param), headers=headers)
            print(self.assertEqual(requests2.json()['msg'].encode('utf-8'),'打卡成功'))
            # print(2, requests2.json()['msg'], requests2.json()['msg'].encode('utf-8'))



if __name__ == '__main__':
        unittest.main()
        result = BeautifulReport(suite)
        # filename -> 测试报告名称, 如果不指定默认文件名为report.html
        # description -> 测试报告用例名称展示
        # log_path='.' -> log文件写入路径
        result.report(filename="测试报告", description="测试deafult报告", log_path='report')
