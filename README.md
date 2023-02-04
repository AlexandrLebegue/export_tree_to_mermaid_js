
# Export_tree_to_mermaid
This script exports the file hierarchy in a Mermaid graph format.
Python format.

## Parameters
* `file_in` : The file name to write the output to.
* `folder_path` (optional) : The path of the folder to be parsed. Defaults to None.
* `options` (optional) : The options to be applied. Defaults to {}. Not used for now.

## Usage

```
export_tree_to_mermaid -f FILE_TO_FILL_THE_GRAPH -p PATH_TO_PARSE
```

## Functions

### `export_to_mermaid()`

This function exports the file hierarchy in a Mermaid graph format.

### `recursive_dir_parse_and_write()`

This function recursively goes through the directory tree and writes mermaid links to the given file.
