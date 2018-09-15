# deoplete-notmuch

Deoplete-notmuch offers asynchronous completion of email addresses using `notmuch address`.
Based on @paretje's [deoplete-notmuch](https://github.com/paretje/deoplete-notmuch), which was inspired by @fszymanski and @frbor's abook sources.

## Installation

To install `deoplete-notmuch`, use your favourite plugin manager.

#### Using [vim-plug](https://github.com/junegunn/vim-plug) on neovim

```vim
Plug 'Shougo/deoplete.nvim', {'do': ':UpdateRemotePlugins'}
Plug 'Valodim/deoplete-notmuch', {'for': 'mail'}
```

## Configuration
```vim
" notmuch address command to fetch completions. in theory, any command that
" outputs addresses one per line is compatible.
" must be --format=text. note that --output=recipients is very slow!
let g:deoplete#sources#notmuch#command = ['notmuch', 'address', '--format=text', '--deduplicate=address', '*']
```
