import requests,json

def loginmain():

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