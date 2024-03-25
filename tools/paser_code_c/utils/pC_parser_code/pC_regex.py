from pathlib import Path

class pC_Element:
    def __init__(self) -> None:
        pass

class pC_ParserCode:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def parser(self):
        try:
            with open(self.file_path, 'r') as file:
                # Read the entire contents of the file
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"The file '{self.file_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    path = "data/rufus/src/cpu.h"
    pr = pC_ParserCode(path)
    pr.parser()

