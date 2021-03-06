def achar_porta_livre():
    import socket
    from contextlib import closing
    '''
    https://stackoverflow.com/questions/1365265/on-localhost-how-do-i-pick-a-free-port-number
    '''
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]