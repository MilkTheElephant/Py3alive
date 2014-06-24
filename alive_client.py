#!/usr/bin/python

import socket


class Py3status:
    def alive_client (self, i3status_output_json, i3status_config):
        
        response = {'full_text': '', 'name':'empty'}
        f = open('alive_client.conf', 'r') # open config file.
        address = f.readline() #read address
        port = f.readline() #read port
        f.close() #close file.
        add = address.strip() #string readlines
        prt = port.strip()
        s = socket.socket() #open socket
        connect = s.connect_ex((add,int(prt))) #connect on address+port
        if connect != 0: #If connecvtion failed, respond with failed.
             response ['full_text'] = "Cannot connect - Error: {0}".format(connect)
             response ['color'] = i3status_config['color_bad']
        elif connect == 0: # Else respond with succsessful.
            response ['full_text'] = "Connection to: {0}:{1} ".format(add,prt)
            response['color'] = i3status_config['color_good']
        else:
             response ['full_text'] = "Unknown Error."
        s.close()
        
        return (0,response)


