#!/bin/sh
# 理想之光
# author:whzcorcd

echo "仅限于 macOS，使用前最好能全局代理外网，开始配置环境..."
shell_path=$(cd `dirname $0`;pwd)
#echo $shell_path

if [ ! -w "$shell_path" ]
then
echo -e "\n\n为了配置环境，请输入su密码 ： "
sudo chown -R $(whoami) "$shell_path"
fi

command -v brew >/dev/null 2>&1 || 
{ 
    echo "尝试安装 Homebrew..."
    echo `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` 
}
command -v python3 >/dev/null 2>&1 || 
{ 
    echo "尝试安装 python3..."
    echo `brew install python3`
}
echo `python3 --version`
command -v pip3 >/dev/null 2>&1 || 
{ 
    echo "尝试安装 pip3..."
    echo `python3 get-pip.py`
}
echo "安装 requests 库..."
echo `pip3 install requests`

echo "环境配置完成"
read -t 150 -p "是否已修改 input.ini 为个人正确信息？[y/n]:" result

if [[ "$result" == 'y' ]]; then
   echo `python3 main.py`
fi
