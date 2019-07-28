# -*-coding:utf8-*-

import os
import os.path
import json
import sys


def read_text_file(file_name):
    f = open(file_name, "r")
    file_content = f.read()
    f.close()
    return file_content


def get_path(dir, sub_dir):
    if str(dir).endswith("/"):
        return dir + sub_dir
    else:
        return dir + "/" + sub_dir


def get_short_dir_name(dir):
    rindex = str(dir).rindex("/")
    return dir[rindex + 1:]


def get_relative_name(root_dir, dir):
    index = str(dir).index(root_dir)
    return dir[len(root_dir) + index:]


def generate(root_dir, dir, lst, level):
    if os.path.isdir(dir):

        short_dir_name = get_short_dir_name(dir)
        relative_name = get_relative_name(root_dir, dir)

        generate_readme_file(dir, short_dir_name)

        left = level * "  " + "- " + "[" + short_dir_name + "]"
        right = "(" + get_path(relative_name, "") + "README.md" + ")"
        lst.append(left + right)

        for sub_dir in os.listdir(dir):
            generate(root_dir, get_path(dir, sub_dir), lst, level + 1)
    else:
        if str(dir).endswith("README.md"):
            return
        if not str(dir).endswith(".md"):
            return

        short_dir_name = get_short_dir_name(dir)
        relative_name = get_relative_name(root_dir, dir)
        left = level * "  " + "* " + "[" + short_dir_name + "]"
        right = "(" + relative_name + ")"
        lst.append(left + right)


def generate_readme_file(dir, short_dir_name):
    readme_file = get_path(dir, "") + "README.md"
    if not os.path.exists(readme_file):
        f = open(readme_file, "w")
        f.write(short_dir_name)
        f.close()


def main(root_dir):
    book_json_file_name = root_dir + "book.json"
    book_json_file_content = read_text_file(book_json_file_name)
    book_json = json.loads(book_json_file_content)
    ignores = book_json["ignores"]
    print("忽略的文件夹：", ignores)

    final_dirs = []
    file_names = os.listdir(root_dir)
    for name in file_names:
        if name in ignores:
            continue

        full_name = root_dir + name
        if not os.path.isdir(full_name):
            continue
        final_dirs.append(full_name)
    
    final_dirs.sort()
    print("需要处理的文件夹", final_dirs)

    final_list = []

    for dir in final_dirs:
        generate(root_dir, dir, final_list, 0)

    str = "* [Introduction](README.md)\n"
    for i in final_list:
        str += i + "\n"

    print(str)
    f = open(root_dir + "_sidebar.md", "w")
    f.write(str)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        dir_name = sys.argv[1]
    else:
        dir_name = "./"
    main(dir_name)
