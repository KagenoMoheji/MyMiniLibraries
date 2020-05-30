# go_listpkgs
This command-option shows installed packages list of Golang. 
This is using package `flag`. 
But this has many issues…. 

### Setup
1. Set `github.com`, `golang.org` and `standardpkgs` in `listpkgs.json` following the rules below.
    - You can set the environmental values of your pc like `${GOPATH}`.
    - You must set your github-name in `ignoreFolderNames` because this cli reseach under the folder `GOPATH\src\github.com\`.
    - You must set only folder-name in `ignoreFolderNames`. Don't set Pathes there.
    - You have to set the higher layer in `golang.org` and `standardpkgs`.
    - Example below.
```
{
    "github.com": "${GOPATH}\\src\\github.com",
    "golang.org": "${GOPATH}\\src\\golang.org\\x\\tools\\cmd",
    "standardpkgs": "${GOROOT}\\src",
    "ignoreFolderNames": [
        "KagenoMoheji"
    ]
}
```
2. Input commands.
    - You have to input options before `listpkgs`.

### DEMO
```
$ gosample listpkgs
Installed
 ├─ sqs
 │   ├─ goreturns
 ├─ uudashr
 │   ├─ gopkgs
 ├─ acroca
 │   ├─ go-symbols
 ├─ rogpeppe
 │   ├─ godef
 ├─ karrick
 │   ├─ godirwalk
 ├─ mdempsky
 │   ├─ gocode
 ├─ ramya-rao-a
 │   ├─ go-outline
 ├─ pkg
 │   ├─ errors
 ├─ nsf
 │   ├─ gocode
 ├─ labstack
 │   ├─ echo
 │   ├─ gommon
 ├─ mattn
 │   ├─ go-colorable
 │   ├─ go-isatty
 ├─ valyala
 │   ├─ fasttemplate
 ├─ golang
 │   ├─ dep
 │   ├─ lint
 ├─ go-delve
 │   ├─ delve
 ├─ derekparker
 │   ├─ delve
```
```
$ gosample -h listpkgs
  -all
        Show installed and standard packages.
  -h    Show help of 'listpkgs' options.
  -standard
        Show only standard packages.
```
```
$gosample -standard -listpkgs
Standard
 ├─ src
 │   ├─ archive
 │   ├─ bufio
 │   ├─ builtin
 │   ├─ bytes
 │   ├─ cmd
 │   ├─ compress
 │   ├─ container
 │   ├─ context
 │   ├─ crypto
 │   ├─ database
 │   ├─ debug
 │   ├─ encoding
 │   ├─ errors
 │   ├─ expvar
 │   ├─ flag
 │   ├─ fmt
 │   ├─ go
 │   ├─ hash
 │   ├─ html
 │   ├─ image
 │   ├─ index
 │   ├─ internal
 │   ├─ io
 │   ├─ log
 │   ├─ math
 │   ├─ mime
 │   ├─ net
 │   ├─ os
 │   ├─ path
 │   ├─ plugin
 │   ├─ reflect
 │   ├─ regexp
 │   ├─ runtime
 │   ├─ sort
 │   ├─ strconv
 │   ├─ strings
 │   ├─ sync
 │   ├─ syscall
 │   ├─ testdata
 │   ├─ testing
 │   ├─ text
 │   ├─ time
 │   ├─ unicode
 │   ├─ unsafe
```
```
$ gosample -all listpkgs
Installed
 ├─ nsf
 │   ├─ gocode
 ├─ labstack
 │   ├─ echo
 │   ├─ gommon
 ├─ mattn
 │   ├─ go-colorable
 │   ├─ go-isatty
 ├─ go-delve
 │   ├─ delve
 ├─ karrick
 │   ├─ godirwalk
 ├─ uudashr
 │   ├─ gopkgs
 ├─ mdempsky
 │   ├─ gocode
 ├─ derekparker
 │   ├─ delve
 ├─ ramya-rao-a
 │   ├─ go-outline
 ├─ acroca
 │   ├─ go-symbols
 ├─ valyala
 │   ├─ fasttemplate
 ├─ pkg
 │   ├─ errors
 ├─ sqs
 │   ├─ goreturns
 ├─ golang
 │   ├─ dep
 │   ├─ lint
 ├─ rogpeppe
 │   ├─ godef
Standard
 ├─ src
 │   ├─ archive
 │   ├─ bufio
 │   ├─ builtin
 │   ├─ bytes
 │   ├─ cmd
 │   ├─ compress
 │   ├─ container
 │   ├─ context
 │   ├─ crypto
 │   ├─ database
 │   ├─ debug
 │   ├─ encoding
 │   ├─ errors
 │   ├─ expvar
 │   ├─ flag
 │   ├─ fmt
 │   ├─ go
 │   ├─ hash
 │   ├─ html
 │   ├─ image
 │   ├─ index
 │   ├─ internal
 │   ├─ io
 │   ├─ log
 │   ├─ math
 │   ├─ mime
 │   ├─ net
 │   ├─ os
 │   ├─ path
 │   ├─ plugin
 │   ├─ reflect
 │   ├─ regexp
 │   ├─ runtime
 │   ├─ sort
 │   ├─ strconv
 │   ├─ strings
 │   ├─ sync
 │   ├─ syscall
 │   ├─ testdata
 │   ├─ testing
 │   ├─ text
 │   ├─ time
 │   ├─ unicode
 │   ├─ unsafe
Tools
 ├─ cmd
 │   ├─ benchcmp
 │   ├─ bundle
 │   ├─ callgraph
 │   ├─ compilebench
 │   ├─ cover
 │   ├─ digraph
 │   ├─ eg
 │   ├─ fiximports
 │   ├─ getgo
 │   ├─ go-contrib-init
 │   ├─ godex
 │   ├─ godoc
 │   ├─ goimports
 │   ├─ gomvpkg
 │   ├─ gopls
 │   ├─ gorename
 │   ├─ gotype
 │   ├─ goyacc
 │   ├─ guru
 │   ├─ html2article
 │   ├─ present
 │   ├─ splitdwarf
 │   ├─ ssadump
 │   ├─ stress
 │   ├─ stringer
 │   ├─ toolstash
```