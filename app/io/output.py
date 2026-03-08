import pandas as pd


def output_text(text):
    """
    function to output text to the console

    :param text:(str) text that will be output to the console
    """
    print(text)


def write_file(file_path, text):
    """
    function to write to a file using python's built-in capabilities

    :param file_path:(str) The path to the file in which the text will be written.
    :param text:(str) The text to be written to the file.
    """
    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(text + "\n")


def write_file_pandas(file_path, text):
    """
    function to write to a file using the pandas library

    :param file_path:(str) The path to the file in which the text will be written.
    :param text:(str) The text to be written to the file.
    """
    return text.to_csv(file_path, index=False)
