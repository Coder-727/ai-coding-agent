from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_dir="calculator"
    # response=get_files_info(working_dir)
    # print(response)

    # response=get_files_info(working_dir,"pkg")
    # print(response)

    # response=get_files_info(working_dir,"/bin")
    # print(response)

    # response=get_files_info(working_dir,"../")
    # print(response)

    # response=get_file_content(working_dir,"lorem.txt")
    # print(response)

    # response=get_file_content(working_dir,"main.py")
    # print(response)

    # response=get_file_content(working_dir,"pkg/calculator.py")
    # print(response)

    # response=get_file_content(working_dir,"/bin/cat")
    # print(response)

    # response=get_file_content(working_dir,"pkg/does_not_exist.py")
    # print(response)

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file(working_dir,"main.py"))
    print(run_python_file(working_dir,"main.py", ["3 + 5"]))
    print(run_python_file(working_dir,"tests.py"))
    print(run_python_file(working_dir,"../main.py"))
    print(run_python_file(working_dir,"nonexistent.py"))

if __name__ == "__main__":
    main()