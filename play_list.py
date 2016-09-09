# coding: utf-8
import sys
import subprocess
import urllib
import re
import datetime
import os
import time
import signal
import glob


current_directory = os.path.dirname(os.path.abspath( __file__ ))


def cleanDataDir():
    """
    データ置き場の掃除
    """
    for file in glob.glob('%s/data/*.mp3' % current_directory):
        if re.match('\d\d\d\d_\d\d_\d\d_\d\d_\d\d_\d\d_\d\d\d\d\d\d.mp3', os.path.basename(file)):
            os.system('rm %s' % file)


def play(filename):
    """
    クロスフェードのためにさらにサブプロセスを生成している。
    raspberry piではうまく動かないので調整が必要。
    """
    proc = subprocess.Popen('python %s/fade_play.py %s/%s 3000 3000' % (current_directory, current_directory, filename), shell=True)
    return proc


def main():
    """
    引数で与えられたurlリストの再生を行う。
    """
    file_list = sys.argv[1:]
    proc = None
    counter = 0
    stopped = [False]
    index = 0

    cleanDataDir()

    # 親プロセスとの通信
    def stop(num, frame):
        if proc:
            proc.kill()
        stopped[0] = True

    signal.signal(signal.SIGTERM, stop)

    while True:
        if stopped[0]:
            break
        if counter % 29 == 0:
            filename = file_list[index % len(file_list)]
            proc = play(filename)
            index += 1
        time.sleep(1)
        counter += 1

    cleanDataDir()


main()
