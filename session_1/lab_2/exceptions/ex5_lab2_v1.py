from typing import Union

#region exceptions
class IntException(Exception):
    ''' Class Exception pour les erreurs avec les entiers. '''
    def __init__(self, message = 'Rentrez une valeur positive et non nul.'):
        self.message = message
        super().__init__(self.message)

class CmdException(Exception):
    ''' Class Exception pour les erreurs avec les commandse. '''
    def __init__(self, message = 'Rentrez une commande P ou S, case sensitive.'):
        self.message = message
        super().__init__(self.message)
#endregion exceptions

#region functions
def get_cmd() -> Union[str, CmdException]:
    ''' Function pour prendre et retourner une commande P/p ou S/s.
    Sinon, retourne une exception cmdException. '''
    cmd_input = input('P/S: ')
    if cmd_input in ('P', 'p', 'S', 's'):
        return cmd_input
    raise CmdException()

def get_int() -> Union[int, IntException]:
    ''' Function pour prendre et retourner un entier.
    Sinon, retourne une exception intException. '''
    try:
        int_input = int(input('Entrez un côté: '))
    except ValueError as exc:
        raise IntException() from exc
    if int_input > 0:
        return int(int_input)
    raise IntException()
#endregion functions

#region programme
print('Entrez P/p pour le périmètre et S/s pour la surface du carré.')

keep_running = True
while keep_running:
    try:
        square_side = get_int()
        cmd = get_cmd()
        if cmd in ('P', 'p'):
            print('Périmètre du carré:', square_side * 4)
        elif cmd in ('S', 's'):
            print('Surface du carré:', square_side * square_side)
    except CmdException:
        print(CmdException().message)
    except IntException:
        print(IntException().message)
    else:
        keep_running = False
print('Programme executé avec succès...')
#endregion programme
