# coding=gbk
import requests
import json
import configparser
from time import sleep

class AutoMarx:
    def __init__(self):

        conf = configparser.ConfigParser()
        conf.read('input.ini')
        wait_time = conf.get('init', 'wait_time')
        wait_time = int(wait_time)
        self.wait_time = wait_time
        data = {
            'startNow' : True
        }
        type = conf.get('init', 'type')
        if type == 0:
            data['paperId'] = 1803217583
            data['collections[0].answerContent'] = conf.get('user', 'username')
            data['collections[1].answerContent'] = conf.get('user', 'school')
        else:
            data['paperId'] = 1803217582
            data['collections[0].answerContent'] = conf.get('user', 'username')
            data['collections[1].answerContent'] = conf.get('user', 'school')
            data['collections[2].answerContent'] = conf.get('user', 'id')
            data['collections[3].answerContent'] = conf.get('user', 'institute')
            data['collections[4].answerContent'] = conf.get('user', 'class')
        url = 'https://www.qingsuyun.com/h5/actions/exam/execute/create-exam.json'
        result = self.post_response_body(url, data)
        self.answer_id = json.loads(result)['body']['answerId']
        url = 'https://www.qingsuyun.com/h5/actions/exam/execute/find-exam.json?answerId=' + str(self.answer_id) + '&queryItems=true'
        self.content = json.loads(self.get_response_body(url))


    @staticmethod
    # get
    def get_response_body(url):
        r = requests.get(url)
        return r.content.decode('UTF-8')

    @staticmethod
    # post
    def post_response_body(url, data):
        r = requests.post(url,data)
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
                result['题'+str(count)] = answer
            else:
                print('题'+str(count)+' success')
            count = count+1
            sleep(self.wait_time)
        return result

    def finish_exam(self):
        url = 'https://www.qingsuyun.com/h5/actions/exam/execute/finish-exam.json?answerId=' + str(self.answer_id) + '&interrupt=false'
        self.get_response_body(url)
        result_url = 'https://www.qingsuyun.com/h5/actions/exam/execute/find-exam.json'
        data = {
            'queryItems' : False,
            'queryScoreLevels' : True
        }
        data['answerId'] = self.answer_id
        result = self.post_response_body(result_url, data)
        query_code = json.loads(result)['body']['answerSheet']['queryCode']
        query_image = requests.get('https://www.qingsuyun.com/h5/qrcode/link/detail/exam-result/107515/' + str(query_code) + '.png')
        if query_image.status_code == 200:
            open('result.png', 'wb').write(query_image.content)
