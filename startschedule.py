import os
from model import configlogger

if __name__ == '__main__':
    curdir = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(curdir, 'logs')
    configlogger.ConfigLogger(logdir)
