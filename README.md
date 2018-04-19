# 理想之光app卡尔马克思杯 自动答题
直接发送请求进行答题 不设置延时大概需要10s完成

# 运行环境
#### Python版本
>Python 3.6.4
#### HTTP 请求库
>requests  安装方法
```
pip install requests
```
#### 抓包
>fiddler4 百度可以找到很多如何PC用fiddler抓取手机的包
>>抓完包后记得关闭fiddler 因为证书问题 可能无法发送请求

# 使用方法
### 修改find-exam.json
找到发往https://www.qingsuyun.com/h5/actions/exam/execute/find-exam.json的请求
```
python main.py
```
会显示没有成功提交的题目的答案
如果显示全部成功 直接在手机上提交 虽然他会提示你只做了0题 但是实际在他们服务器上已经完全做好了
可以先练习测试一下

# 你可以修改的配置 input.ini
只有一个wait_time 设置延时 单位秒
不设置延时不确定会不会封 但是我在3点到4点一直狂答同一份试卷没有被封

# 感想
本来
