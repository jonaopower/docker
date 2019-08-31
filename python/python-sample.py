#Importa biblioteca docker e json
import docker
import json

#Conecta no Docker Runtime do Host Docker
client = docker.from_env()

#Cria lista com todos os containers do Host
ct_ids = client.containers.list(all)

#Loop Para pegar atributos do container
for ct_list in client.containers.list(all=True):
    ct_status = ct_list.status
    ct_id = ct_list.short_id
    ct_name = ct_list.name
    ct_image = ct_list.image

#Imprime atributos container
print(ct_list.name)
info = client.containers.get(ct_id)
print(info)
