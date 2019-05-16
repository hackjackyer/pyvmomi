#!/usr/bin/env python 
import atexit 

from pyVim import connect 
from pyVmomi import vmodl 
from pyVmomi import vim 


def print_vm_info(virtual_machine): 
    for device in virtual_machine.config.hardware.device: 
        if (device.key >= 4000) and (device.key < 5000): 
            if device.macAddress == '00:50:56:00:00:00':
                # 需要查询的mac 
                print('device.macAddress==', device.macAddress) 
 
                summary = virtual_machine.summary 
                print("Name       : ", summary.config.name) 
                print("Template   : ", summary.config.template) 
                print("Path       : ", summary.config.vmPathName) 
                print("Guest      : ", summary.config.guestFullName) 
                print("Host       : ", summary.runtime.host.name) 
 
def main(): 
    try: 
    # 如果需要使用SSL证书，则用，这里没有使用
    #   service_instance = connect.SmartConnect(host="HOST", 
    #                                           user="administrator@vsphere.local", 
    #                                           pwd="密码", 
    #                                           port=端口，默认443)
        service_instance = connect.SmartConnectNoSSL(host="HOST", 
                                                user="administrator@vsphere.local", 
                                                pwd="密码", 
                                                port=端口，默认443) 
 
        atexit.register(connect.Disconnect, service_instance) 
 
        content = service_instance.RetrieveContent() 
 
        container = content.rootFolder  # starting point to look into 
        viewType = [vim.VirtualMachine]  # object types to look for 
        recursive = True  # whether we should look into it recursively 
        containerView = content.viewManager.CreateContainerView( 
            container, viewType, recursive) 
 
        children = containerView.view 
        for child in children: 
            print_vm_info(child) 
 
    except vmodl.MethodFault as error: 
        print("Caught vmodl fault : " + error.msg) 
        return -1 
 
    return 0 
 
# Start program 
if __name__ == "__main__": 
    main() 
