import os 
import sys
import getopt

MERMAID_HEADER = "graph LR\n"
MERMAID_INDENT = "    "
MERMAID_LINK_DIR = MERMAID_INDENT +"{} --> {}\n"
MERMAID_LINK_FILE = MERMAID_INDENT +"{} --- {}\n"
def recursive_dir_parse_and_write(file_to_write, folder_path, options = {}):
    """
    Recursively goes through the directory tree and writes 
    mermaid links to the given file.

    Parameters:
        file_to_write (file): File to write the mermaid links to
        folder_path (string): Path of the folder with the directory tree
    """
    for dir in os.listdir(folder_path):
        sub_dir = folder_path+"/"+dir
        if os.path.isdir(sub_dir):
            dep1 = sub_dir.split("/")[-2]
            dep2 = sub_dir.split("/")[-1]
            file_to_write.write(MERMAID_LINK_DIR.format(dep1, dep2))
            recursive_dir_parse_and_write(file_to_write, sub_dir)
        else:
            pass

def export_to_mermaid(file_in ,folder_path = None, options = {}):
    """
    This function exports the file hierarchy in a Mermaid graph format.

    Parameters: 
        file_in (str): The file name to write the output to.
        folder_path (str, optional): The path of the folder to be parsed. Defaults to None.
        options (dict, optional): The options to be applied. Defaults to {}.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the execution.
    """
    try:
        with open(file_in, "w+") as file_to_write:
            file_to_write.write(MERMAID_HEADER)
            recursive_dir_parse_and_write(file_to_write, folder_path)
    except Exception as e :
        print("Error during execution", e)


def help():
    print("Example of utilization :")
    print("export_tree_to_mermaid -f FILE_TO_FILL_THE_GRAPH -p PATH_TO_PARSE")
    print("Good luck :)")

if __name__ == "__main__":
    try:                                
        opts, args = getopt.getopt(sys.argv[1:], "hf:p:", ["help", "file", "path"])
    except getopt.GetoptError:          
        help()                         
        sys.exit()                     
    
    file_in = "example.mmd"
    folder_path = os.getcwd()

    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            help()                     
            sys.exit()  
        elif opt in ("-f", "--file"):   
            file_in = arg
        elif opt == "-p":
            folder_path = arg                             
            
    export_to_mermaid( file_in ,folder_path)
