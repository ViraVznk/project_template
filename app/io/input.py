import pandas as pd


def input_text():
    """
    Function for entering text from the console

    :return:(str) The text entered by the user
    """
    text = input("Введіть текст: ")
    return text


def read_file(file_path):
    """
    Function to read from a file using python built-ins

    :param file_path:(str) file path
    :return:(str) Text from the file
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def read_file_pandas(file_path):
    """
    Function for reading from a file using the pandas library.

    :param file_path:(str) file path
    :return:(str) Text from the file
    """
    df = pd.read_csv(file_path)
    return df
