from http import client
import docker
import time
import json
import subprocess
import shlex
import sys

def main():
    #obj = docker_main.DockerSDK()
    client = docker.DockerClient("unix://var/run/docker.sock")
    client_api = docker.APIClient("unix://var/run/docker.sock")
    #cont_create = client.containers.create(image="alpine",command ="sh",tty=True, stdin_open=True, name="dockeralpine", restart_policy={"Name": "on-failure"})
    #print(cont_create.start())
    #obj = client.containers(filters={"id":"0f2617e2f0bd"},size = True, trunc = True)
    #output = obj[0]
    #print(json.dumps(obj[0],indent=3))
    #keys = ['Command', 'CreatedAt', 'ID', 'Image', 'Labels', 'LocalVolumes', 'Mounts', 'Names', 'Networks', 'Ports', 'RunningFor', 'Size', 'State', 'Status']
    '''
    output_dict = {}
    output_dict["Command"] = output["Command"]
    output_dict["CreatedAt"] = output["Created"]
    output_dict["ID"] = output["Id"]
    output_dict["Image"] =output["Image"]
    #output_dict["Labels"] = output
    '''

    #print(client.images.load("alpine.tar.gz"))
    #container = client_api.containers(filters={"id":"aa79d3f0585"},size = True, trunc = True)
    #print(container)
    #print(json.loads(container[0]))
    #print(dict(sorted(container[0].items())))
    #containers = client.containers(all=True,quiet=True)
    #print(container)
    #print([container["Id"][0:12] for container in containers])
    #print(client.start("aa79d3f05856"))
    #print(client.images("5d0da3dc9764"))
    #print(client.remove_image("f8179d8a4d7d",forc))
    #exec_cmd = client.exec_create("aa79d3f05856",cmd="ls")
    #exec_id = exec_cmd['Id']
    #print(exec_cmd)
    #exec_output = client.exec_start(exec_id,demux=True)[0].decode()
    #subprocess.run([sys.executable, "-c", "print('exec_cmd')"])
    #print(client.logs("aa79d3f05856").decode())
    #print(client.containers(size=True,filter={"id":"aa79d3f05856"}))
    #print(client.containers(size=True,filters={'id':'aa79d3f05856'})[0])
    #info = client_api.info()
    #f = open("info.txt","w")
    #f.write(json.dumps(info,sort_keys=True, indent=3))
    #jo = json.dumps(info,sort_keys=True, indent=3)
    #print(json.dumps(info,sort_keys=True).strip())
    #stats = client.stats("0f2617e2f0bd",stream=False)
    #print(json.dumps(stats,sort_keys=True,indent = 3))
    #img = client.images.get("alpine:latest")
    #print(img.save(named = True))
    #bin = "/Users/aukkalam/Desktop/python_constructs/Docker_sdk/trial_sdk/centos.tar"
    #print(client.images.load(data=bin))

if __name__=='__main__':
    main()
