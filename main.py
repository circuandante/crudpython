import sys
clients = [
        {
            'name': 'Pablo',
            'company' : 'facebook',
        },
        {
            'name': 'Ricardo',
            'company': 'google',
        }
    ]

def create_client(client_name):
    global clients
    if client_name not in clients:
         clients.append(client_name)
    else:
        print('clients already exist')


def delete_client(client):
    global clients
    if client in clients:
        clients.remove(client)
    else:
        return print('the client not exist')


def search_client(client):
    
    for clientL in clients:
        if clientL != client:
            continue
        else:
            return True


def modified_client(client_name, update_client_name):
    global clients  
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client_name
    else:
        print('no client found!')


def list_clients():
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx, client['name']))


def _print_line():
    print('-' * 50)
    print('welcome to platzi sales')
    print('-' * 50 )
    print('what do you like to do today')
    print('[C] if you want create client')
    print('[D] if you want delete client')
    print('[U] if you want edit contact')
    print('[S] if you want search a client')


def _get_client_field(field):
    field = none
    
    while not field:
        field = input('what is the client {}?'.format(field))


def _get_client_name():
    name = None

    while not name:
        name = input('what is the client name? ')
        if name == 'exit':
            name = None
            break
    if not name: 
            sys.exit()

    return name.capitalize()

if __name__ == '__main__':
    _print_line()
    command = input()
    command = command.upper()

    if (command == 'C'):
        client = {
            'name' : _get_client_field('name')
            'company': _get_client_field('company')
        }            
        create_client(client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        new_client_name = input('new client name? ')
        modified_client(client_name, new_client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('found it')
        else:
            print('client not found')
    else :
        pass
        

    list_clients()

