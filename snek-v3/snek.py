"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]

"""
import docopt
import pkg_resources

normal_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

fancy_snek = """\
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
"""


def get_sneks():
    sneks = {
        'normal': normal_snek,
        'fancy': fancy_snek,
    }

    # It will iterate over all entry_points named snek_types installed on the current system.
    # If other packages define entry_points called "snek_types" in setup.py,
    # they will be dynamically loaded when snek runs.
    for entry_point in pkg_resources.iter_entry_points('snek_types'):
        print("Loading entry point: {}".format(entry_point.name))
        sneks[entry_point.name] = entry_point.load()

    return sneks


def main():
    args = docopt.docopt(__doc__)
    snek_type = args['--type'] or 'normal'
    print(get_sneks()[snek_type])


if __name__ == '__main__':
    main()
