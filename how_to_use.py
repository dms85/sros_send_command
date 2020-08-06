list_cmd = ['show system information', 'show router interface']

Jump_Server_IP, Jump_Server_User, Jump_Server_Password, Jump_Server_Internal_Interface = '1.1.1.1','root','root','1.1.1.1'
target_node = [target_node1, target_node2, target_node3]
target_node_user = 'admin'
target_node_password = 'admin'

dict_out = get_cmd_output_v2(Jump_Server_IP,
                             Jump_Server_User, Jump_Server_Password, Jump_Server_Internal_Interface,
                             target_node,
                             target_node_user, target_node_password, 'alcatel_sros',
                             list_cmd,
                             'log.txt')

key1_ip = list(dict_out.keys())
key2_cmd = list(dict_out[key1_ip[0]])

for _ip in key1_ip:
    for _command in key2_cmd:
        print(dict_out[_ip][_command]
        
      
