#!/usr/bin/python

import vymgmt

def createinterface(eth1,ip1,desc1):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("interfaces ethernet %s address '%s'" %(eth1,ip1))
        vyos.set("interfaces ethernet %s description '%s'" %(eth1,desc1))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def readinterface():
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        print (vyos.run_op_mode_command("show interfaces"))
        y = vyos.run_op_mode_command("show interfaces")
        vyos.logout()
        return y

def delinterface(eth):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces ethernet %s" %(eth))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def updateinterface(eth,eth1,ip1,desc1):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces ethernet %s" %(eth))
        vyos.set("interfaces ethernet %s address '%s'" %(eth1,ip1))
        vyos.set("interfaces ethernet %s description '%s'" %(eth1,desc1))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

