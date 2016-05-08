" Indent automatically depending on filetype                                   
filetype plugin indent on                                                      
set tabstop=4                                                                  
set shiftwidth=4                                                               
set expandtab                                                                  
set clipboard=unnamed                                                          
                                                                               
" Turn on line numbering. Turn it off with "set nonu"                          
set linebreak                                                                  
set number                                                                     
set numberwidth=2                                                              
                                                                               
" Ignore case when searching                                                   
set ignorecase                                                                 
                                                                               
" " When searching try to be smart about cases                                 
set smartcase                                                                  
                                                                               
" " Highlight search results                                                   
set hlsearch                                                                   
                                                                               
" " Makes search act like search in modern browsers                            
set incsearch arch                                                                  
                                                                               
" " Don't redraw while executing macros (good performance config)              
set lazyredraw                                                                 
                                                                               
nmap <c-A> ggvG$                                                               
                                                                               
" --Hotkey mappings--                                                          
" Jump easily between windows                                                  
nnoremap <C-J> <C-W><C-J>                                                      
nnoremap <C-K> <C-W><C-K>                                                      
nnoremap <C-L> <C-W><C-L>                                                      
nnoremap <C-H> <C-W><C-H>                                                      
" Start e: %%/ will expand the file from the current directory                 
cabbr <expr> %% expand('%:p:h')                                                
                                                                               
nmap <Esc><Esc> :w<CR>                                                         
                                                                               
map <leader>rr :source ~/.vimrc<CR>                                            
" Pythor maps                                                                  
nnoremap <buffer> <F9> :exec '!python' shellescape(@%, 1)<cr>                  
                                                                               
" Set syntax and color options                                                 
syntax enable                                                                  
set t_Co=256                                                                   
set background=dark                                                            
" let g:solarized_termcolors=256                                               
" colorscheme solarized                                                        
colorscheme zenburn                                                            
set colorcolumn=79                                                             
                                                                               
highlight ColorColumn ctermbg=0                                                
                                                                               
nnoremap <C-y> "+y     
