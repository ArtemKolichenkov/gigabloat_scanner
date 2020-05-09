# Gigabloat File Manager

## Development
You need to add this to zhrc to be able to switch environments and use poetry  
`eval "$(pyenv init -)"`

```shell
pyenv install 3.8.2
pyenv local 3.8.2
```

Tests should be run with makefile since testing absolute paths fucks up (I guess)

Write up what to do with DS_Store, it will fuck up the tests


Configure VScode workspace settings to get black and pylint path
`poetry env info --path`
```json
{
    "python.formatting.blackPath": "<poetry_env_path>/bin/black",
    "python.formatting.provider": "black",
    "python.linting.pylintPath": "<poetry_env_path>/bin/pylint"
}
```

## General algorithm

`scanDirectory` is called with directory to scan.
for it we:
- create dummy `Directory` with just path name for now (and parent if provided)
1. get list of files (in dir, no subdirs)
    - create `File` objects for each
    - increment total files in scan with number of these files
2. get list of subdirs
    - recursively apply `scanDirectory` again
3. update dummy `Directory` with `File`s and sub`Directories`
4. add directory to `self.directories` list
5. if we end up at this point and figure out that we're in root
    - assing `self.root_directory` for easy access
6. return the `Directory` to be used in step 2

## TODO

- [ ] License
- [ ] Progressbar
- [ ] Add empty directory finder
- [ ] Count the file size for each extension
- [ ] Directory/File paths must be absolute  
If you give absolute path it will make use of abs path. However it would be nice to give relative path via CLI and get abs path in return.
- [ ] Get all files method?  
I wonder if it makes sense since we could query/filter for all files from the main Scanner object. However, it might be good to be able to do it via CLI. Not sure.
- [ ] filetypes/categories are not counted with subdirs in mind. Should be counted I guess (with destinciton if its directly in the folder or deeper inside).
- [ ] Space on the disk thing (4kb minimum on macOS even if file is like 2 Bytes?)
- [ ] We can actually maintain multiple scans easily i guess
- [ ] Tests' expected results could be just a proper scanfile

## Proposed CLI interface

Command `gigabloat scan`  
Get general stats  
Options:  
`--dir <directory>` @required  
directory to scan  
`--json`  
provide json output  
`--table`  
provide tabulat output  
`--pyobj`  
provide pyobj output  
`--nofile`  
do not save report file after scan is finished  

Command `gigabloat filter`  
Filter some specific stat  
`--f <file>` @required  
specify report file  
`--ext <ext>`  
give stats for files with .<ext> extension  
`--bd`  
show biggest directory (by size)  
`--bf`  
show biggest file (by size)  
`--photos`  
show amount and size of photos  
`--videos`  
show amount and size of videos  
`--audio`  
show amount and size of audio  
`--media`  
show amount and size of media files (phtos, images, audio)  


## Non-MVP ideas

- Add new categories by user (just list of extensions)