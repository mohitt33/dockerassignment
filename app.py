#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def get_hostname():
    return socket.gethostname()

if __name__ == '__main__':
    hostname = get_hostname()
    print(f'Hello from {hostname}')

