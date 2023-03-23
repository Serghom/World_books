#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebBooks.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    test = "              ┌m \n\
                ▒,       ,▄▌  \n\
                 ▒@▌  ▐▌ ▓▓▓ █L \n\
                  ▐▒▒▄█▓▓▓▓▓▓▓▌░░╖  ▄▒@m \n\
                 ,║▒▒▒▒▒▓▒░░░░░╢╢▒▒█▒▒▒▌, \n\
                @░░░▒░░░░░░░░░░░║▒▒▒▒▒▒▒▒@ \n\
              |▒░░░░░░░░░░░║▒▒▒▒▒▒▒▒▒▒▒▒▒░k▄▒▒▄m ▄▄▄▄ \n\
             ▒Ñ░░░░░░░░░▒▒▒▒▒░░░▄░╢▒▒▒▒▒▀░▒▒▒▒▒▓█▒▒▒▒ \n\
             ▒░░░░░K░║▒▒▒░░░████▓█▓▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▌` \n\
             ▒░░░░░░╓╓▒▒▒▓▓▓▀▒h  ▓▓▓▒▒▒░░▒▒▒▒▒▒▒▒▒▄gg \n\
             ▒░░░░░░░█▒▒▒▓▓▓,▒h ,▒░▒▒▒░░░▒▒▒▒▒▒▒▓▒▒▒▒ \n\
              ├▒░░░░▄▒▒▒▒▓▓▓▓▒@@▒▒▒▒░░░╟▒▒▒▒▒▒▒▒▒▒▒▒\" \n\
              |▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒░░▒▒▒▒▒▒▒▓▒▒L \n\
                ║░░░░▀▀▒▒▒▒▒▒▒▒▒▒▒░░║░░░▒▒▒▒▒█▒▒▒▒Γ ,,,,,,,,, \n\
                `║░░░║░░░░░░░░▒▒▒░░║░░░▒▒▒▒▒▒▒▒▒▓▒╗m░░░░░░░░░╗ \n\
              ,~ ▒▒░▒░░░░▒░░░░▒▓▄╓▒▒░░░▒▒▒▒▒▒▓▓▓▀▓▌▄░░░░░░░░░░░░╓ \n\
                N░░░░░░▒▒ÑÑÑÑ ▐▓▓ ╢▒░░░░▒▒▒▒▓▓▌,,▓▓▓,Ñ░░░░░░░░░░▒ \n\
                 `````        '\"▄▄█▒▒▒▒▒▒▒▒██▒▓▓▓▓▓▓▓ '╙║░░░░░░░▒░km \n\
                             µµ▄▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓   ╝░░░░░░░▒░║▒, \n\
                          ▐██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒    ▒░░░░║▒░║░░▒ \n\
                          ▐▒▒▒▒▒▒▒▒▒▒▒▒▌\"\"\"▀▒▒▒▒▒▒▒▒▒    ▒░░░╖░░░▒░░▒░km \n\
                          ▐▒▒▒▒▒▒▒▓▓▀▀▀▀     ▒▓▒▒▒▒▒▒▒▒▒▒░░░▒░░░▒░░▒░░║▒ \n\
                          ▐▒▒▒▒▒▒▒▒▌         ▓▒▒▒▒▒▒▒▒▒▒░║║░░░░▒░░║▒░░░░@ \n\
                           \"░▒▒▒▒▒▒▒W░        ▐▒▒▒▒▒▒▒▒▒▒▄░░╖░░░░╖░░░░░░▒ \n\
                             ░░▒░▒▒▒▒░         ░▒░▒▒▒▒▒▒▒▒▒▒░░░░╢░░░░░░░▒ "
    print(test)
    main()
