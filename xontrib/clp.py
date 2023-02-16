"""Copy output to clipboard. Cross-platform. """

from xonsh.built_ins import XSH

_clp_alias = XSH.env.get('XONTRIB_CLP_ALIAS', 'pyperclip')

if _clp_alias == 'pyperclip':
    import pyperclip as _pclp

    def _clp(args, stdin, stdout):
        if stdin is None:
            print('No input. Example: `echo hello | clp`')
            return -1
        txt = ''
        for line in stdin.readlines():
            txt += line
        _pclp.copy(txt)
        return 0
    aliases['clp'] = _clp    
    del _clp

elif _clp_alias == 'shutil':
    import shutil as _shutil

    if _shutil.which('pbcopy'):  # DARWIN
        aliases['clp'] = 'pbcopy'
    elif _shutil.which('xclip'):  # LINUX
        aliases['clp'] = 'xclip -sel clip'
    elif _shutil.which('clip.exe'):  # WINDOWS
        aliases['clp'] = 'clip.exe'
    elif _shutil.which('CLIP.EXE'):  # WINDOWS
        aliases['clp'] = 'CLIP.EXE'
    else:
        from xonsh.platform import ON_LINUX, ON_DARWIN #, ON_WSL, ON_CYGWIN, ON_MSYS, ON_POSIX, ON_FREEBSD, ON_DRAGONFLY, ON_NETBSD, ON_OPENBSD
        if ON_LINUX:
            print('xontrib-clp: install xclip')
        elif ON_DARWIN:
            print('xontrib-clp: install pbcopy')
        elif ON_WINDOWS:
            print('xontrib-clp: clip.exe not found')

else:
    print(f'xontrib-clp: unknown alias: {_clp_alias}')
