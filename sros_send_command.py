def get_cmd_output_v2(jh_ip, jh_user, jh_passwd, jh_int, l_tn, tn_user, tn_passwd, tn_type, l_commands, logfile):
    start = datetime.datetime.now()
    open(logfile, 'w')
    logging.basicConfig(level=logging.DEBUG, filename=logfile)
    port_ssh = 22
    jh = paramiko.SSHClient()
    jh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        jh.connect(jh_ip, username=jh_user, password=jh_passwd)
        # if jh.connect(jh_ip) is not None:
        print('>>> Connected to Jump Host')
        jht = jh.get_transport()
        if jht is not None:
            print('>>> Transport to Jump Host Established')
            '''
            Do the following when Connected to Jump Host
            1. Call open_channel for Data Transfer
            2. Use the channel as sock in netmiko ConnectHandler
            '''
            src_sock = (jh_int, port_ssh)
            d_r1 = {}
            for trgt_node in l_tn:
                dst_sock = (trgt_node, port_ssh)
                try:
                    jhc = jht.open_channel('direct-tcpip', dst_sock, src_sock, timeout=200)  # Call open_channel
                    tn = {
                        'device_type': tn_type,
                        'ip': 'n/a',  # will not be used as we have created channel to target node using open_channel
                        'username': tn_user,
                        'password': tn_passwd,
                        'auth_timeout': 200,
                        'banner_timeout': 200,
                        'sock': jhc  # use created channel as sock in netmiko
                    }
                    connect_tn = ConnectHandler(**tn)
                    if connect_tn.is_alive():
                        '''
                        When connected to Target Node, do the following,
                        '''
                        d_r2 = {}
                        print('\n>>> Connected to: ' + str(trgt_node))
                        for command in l_commands:
                            print('--- Executed Command: ' + str(command))
                            output_cmd = connect_tn.send_command(command)
                            d_r2[command] = output_cmd
                            print(output_cmd)
                        d_r1[trgt_node] = d_r2
                        connect_tn.disconnect()
                        print('>>> Disconnected from: ' + str(trgt_node))
                    else:
                        print('\n>>> Unable to Connect to Target Node: ' + str(trgt_node) + ' -- Exit 4')
                except:
                    print('\n>>> ConnectHandler to ' + str(trgt_node) + ' Failed')
                    print('>>> Check Target Node IP, User and Password, and Max Sessions')
                    print('>>> Exit 5')
                    d_r2 = {}
                    for command in l_commands:
                        print(command)
                        d_r2[command] = 'N/A --- Exit 5'
                    d_r1[trgt_node] = d_r2
                    continue
                # d_r1[trgt_node] = d_r2
            print(str(datetime.datetime.now() - start))
            return d_r1
        else:
            print('\n>>> get_transport returns "None" -- Exit 1')
            return {'get_transport Failed -- Exit1': {'exit1': 'exit1'}}
    except:
        print('\n>>> SSHClient.connect Failed -- Exit 3')
        return {'Failed to Connect to Jump Host -- Exit3': {'exit3': 'exit3'}}
        # sys.exit()
