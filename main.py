import socket_server
import os

def conf_msg_callback(bytedata):
    return writeConf(bytedata)

def writeConf(contextByte):
    contextStr = str(contextByte)
    print 'Context: ' + contextStr

    # write to profile
    ipsec_conf = open('ipsec.conf', 'w')
    ipsec_conf.write(contextStr)
    ipsec_conf.write('\n')
    ipsec_conf.close()
    # strongswan operations
    # print "strongswan reload && strongswan up " + conn_name
    # os.system("strongswan reload && strongswan up " + conn_name)
    info = 'write to ipsec.conf: success!'
    print info
    return contextStr + info

def start():
    os.system("echo > ipsec.conf")
    # os.system("strongswan restart")

    config_server = socket_server.socket_server(2020, conf_msg_callback)

    config_server.start()
    # print "Agent is running..."

    while True:
        if str(raw_input()) == "exit":
            break

    config_server.stop()
    # print "Agent has been closed."

    # os.system("strongswan stop")
    # os.system("echo > ipsec.conf")
    exit()


start()
