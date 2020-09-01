import cx_Freeze
import os


def get_include_file(filename):
    filepath = os.path.join('data', filename)
    return (filepath, filepath)


# Specify any executables that should be generated
# the filename should be the name of the file with
# the app entry point
filename = 'main.py'
icon = os.path.join('data', 'sudoku.ico')
executables = [cx_Freeze.Executable(filename, icon=icon)]

# the name of the app
app_name = 'HSCS Sudoku'

# an explixit list of all the packages used by our app
packages = ['pygame']

# # a list of any data files used by the app (i.e. images, etc.)
# # the get_path method assumes resources are stored
# #  in the sub-directory 'data'
include_files = [get_include_file('sudoku_winner_spritesheet.png'),
                 get_include_file('background.mp3'),
                 get_include_file('cell_select.wav')]


exclude_files = ["tkinter",
                 "PyQt4.QtSql",
                 "sqlite3",
                 "scipy.lib.lapack.flapack",
                 "PyQt4.QtNetwork",
                 "PyQt4.QtScript",
                 "numpy.core._dotblas",
                 "PyQt5",
                 "asyncio",
                 "email",
                 "html",
                 "xml",
                 "logging",
                 "unittest",
                 "test",
                 "xmlrpc",
                 "http",
                 "urllib",
                 "pydoc_data"]


cx_Freeze.setup(
    name=app_name,
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files,
            "excludes": exclude_files,
            "optimize": 2
        }
    },
    executables=executables
)
