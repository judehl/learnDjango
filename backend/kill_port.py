# -*- coding: utf-8 -*-
# @Time    : 2022/1/28 19:58
# @Author  : hk

import os
import argparse
import re


def kill_port(args):
    """
    删除某程序在后台的占用
    :param args:
    :return:
    """
    keyword_re = args.keyword
    keyword_re += r'\s+(\d+)\s+'

    if args.port:
        port_list = list()
        command = "lsof -i tcp:" + str(args.port)
        r = os.popen(command)
        out_data = r.read().split('\n')
        for line in out_data:
            if args.keyword in line:
                port_list = re.findall(keyword_re, line)
        l = len(port_list)
        if l == 1:
            command = 'kill -9 ' + port_list[0]
            os.system(command)
        elif l > 1:
            print('列表长度大于1，请确认后删除！')
        else:
            print(f'{args.keyword}不在后台进程中！')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', type=str, help='删除程序名称')
    parser.add_argument('-p', '--port', type=int, help="删除程序在后台占用端口号")
    parser.add_argument('-l', '--portList', type=list, help="删除端口列表")
    args = parser.parse_args()
    kill_port(args)
