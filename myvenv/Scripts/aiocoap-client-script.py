#!c:\users\������\desktop\board\django_react_board\myvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'aiocoap==0.3','console_scripts','aiocoap-client'
__requires__ = 'aiocoap==0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('aiocoap==0.3', 'console_scripts', 'aiocoap-client')()
    )
