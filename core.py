# coding=gbk
import requests
import json
import configparser
from time import sleep

class AutoMarx:
    def __init__(self):
        ''' 甚至不需要伪装
        conf = configparser.ConfigParser()
        conf.read('input.ini')
        hsid = conf.get('cookie', 'hsid')
        if self.is_empty(hsid):
            raise BaseException('input.ini is incomplete')
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate,br',
            'Accept-Language': 'zh-CN,en-US;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        }
        self.cookies = {
            'hsid': hsid
        }
        '''

        conf = configparser.ConfigParser()
        conf.read('input.ini')
        wait_time = conf.get('init', 'wait_time')
        try:
            wait_time = int(wait_time)
        except:
            wait_time = 0
        self.wait_time = wait_time
        file = 'find-exam.json'
        self.content = json.load(open(file, encoding='utf-8'))


    def get_response_body(self, url):
        r = requests.get(url)
        return r.content.decode('UTF-8')

    @staticmethod
    def is_empty(s):
        if (s.strip() == '') or (not s.strip()):
            return True
        return False

    @staticmethod
    def array_to_string(array):
        s = ''
        for i in range(len(array)):
            if i == 0:
                s = s + str(array[i])
            else:
                s = s + ',' + str(array[i])
        return s

    def submit_answer(self, answer_id, question_id, answer):
        # 甚至get后面只跟了答题信息 完全没有验证这个题是谁答的 甚至不需要延时 甚至根本不会封
        url = 'https://www.qingsuyun.com/h5/actions/exam/execute/submit-answer.json?'
        s = self.array_to_string(answer)
        url = url + 'answerId=' + str(answer_id) + '&questionId=' + str(question_id) + '&answerContent=' + s
        result = self.get_response_body(url)
        if result.find('SUCCESS') == -1:
            return False
        else:
            return True

    def auto_answer(self):
        count = 1
        result = {}
        body = self.content['body']
        answer_id = body['answerSheet']['id']
        for item in body['examItems']:
            question = item['jsonData']
            question_id = item['questionId']
            if question.get('single'):
                options = question['single']['options']
            if question.get('multiple'):
                options = question['multiple']['options']
            answer = [x['sortIndex'] for x in options if x['rightAnswers'] == True]
            res = self.submit_answer(answer_id,question_id,answer)
            if not res:
                result['题目'+str(count)] = answer
            else:
                print('题' + str(count) + ' success')
            count = count+1
            sleep(self.wait_time)
        return result


