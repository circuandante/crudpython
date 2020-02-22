clients = 'Pablo, Ricardo'

def create_client(client_name):
    global clients
    if client_name not in clients:
         clients += ', ' + client_name + ','
    else:
        print('clients already exist')


def modified_client(client_name, update_client_name):
    global clients  
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ', ')
    else:
        print('no client found!')

def list_clients():
    global clients
    print(clients)


def _print_line():
    print('-' * 50)
    print('welcome to platzi sales')
    print('-' * 50 )
    print('what do you like to do today')
    print('[C] if you want create client')
    print('[D] if you want delete client')
    print('[U] if you want edit contact')


def _get_client_name():
    return input('what is the client name? ').capitalize()

if __name__ == '__main__':
    _print_line()
    command = input()
    command = command.upper()

    if (command == 'C'):
        client_name = _get_client_name()
        create_client(client_name)
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        new_client_name = input('new client name? ')
        modified_client(client_name, new_client_name)
    else :
        pass
        

    list_clients()

