<p align="center">
Copy output to clipboard. Cross-platform.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-jump-to-dir" target="_blank">tweet</a>.
</p>

## Installation

To install use pip:

```bash
xpip install xontrib-clp
# OR: xpip install -U git+https://github.com/anki-code/xontrib-clp
```

## Usage

```xsh
xontrib load clp
echo hello | clp   # Copy "hello\n" to clipboard
```

## Use cases

#### [pyperclip](https://pypi.org/project/pyperclip/)
```xsh
$XONTRIB_CLP_ALIAS = 'pyperclip'  # default
xontrib load clp
echo hello | clp   # Copy "hello\n" to clipboard using pyperclip
```

#### shutil
```xsh
$XONTRIB_CLP_ALIAS = 'shutil'  # default
xontrib load clp
echo hello | clp   # Copy "hello\n" to clipboard using platform-depending tool: pbcopy, xclip, etc
```

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
