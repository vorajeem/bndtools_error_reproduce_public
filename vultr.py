#!/usr/local/bin/python

import sys
import getopt
import urllib2
import json

from pprint import pprint

def main(argv):                         
    grammar = "kant.xml"
    try:                                
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
      
        if len(args) > 0: 
           command = args[0] 

           if command == "provision":
              provision()
              return

        usage()
    except getopt.GetoptError:
        print "debug/3"
        usage()
        sys.exit(2)                     

def usage():
    print "Usage: vultr COMMAND"
    print ""
    print "  where COMMAND is one of:"
    print "        provision: provisions a server"
    
def provision():
    print "   ... provisioning servers"
  
    plan = getPlan() 
#    region = getRegion()
#
#    if region == None:
#       print "Error provisioning servers: region not available"
#       return None
#
#    os = getOS('ubuntu', 'x64', 'Ubuntu 16.04 x64')
#
#    if os == None:
#       print "Error provisioning servers: Ubuntu 16.04 x64 not supported"
#       return None
#
#    print os

def getPlan():
    response = urllib2.urlopen("https://api.vultr.com/v1/plans/list")

    if response.getcode() != 200:
       print "Error retrieving plans list: ", response.getcode()
       return None

    if response.info()['content-type'] != 'application/json':
       print "Error retrieving plans list: invalid Content-Type"
       return None
    
    data = json.load(response)
 
    for id in data:
        plan = data[id]
        print " > ",plan['VPSPLANID'],plan['vcpu_count'],plan['ram'],plan['price_per_month']

    return None
    
def getRegion():
    response = urllib2.urlopen("https://api.vultr.com/v1/regions/list")

    if response.getcode() != 200:
       print "Error retrieving region list: ", response.getcode()
       return None

    if response.info()['content-type'] != 'application/json':
       print "Error retrieving region list: invalid Content-Type"
       return None
    
    data = json.load(response)
 
    for id in data:
        region = data[id]
        print "  > ",region['DCID'],region['name']

    return None

     

def getOS(family, architecture, name):
    response = urllib2.urlopen("https://api.vultr.com/v1/os/list")

    if response.getcode() != 200:
       print "Error retrieving operating system list: ", response.getcode()
       return None

    if response.info()['content-type'] != 'application/json':
       print "Error retrieving operating system list: invalid Content-Type"
       return None
    
    data = json.load(response)

    for id in data:
        os = data[id]
        if os['family'] == family:
           if os['arch'] == architecture:
              if os['name'] == name:
                 return os

    return None

if __name__ == "__main__":
    main(sys.argv[1:])
