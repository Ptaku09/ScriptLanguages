import os
import sys


def display_all_catalogs():
    path_dirs = os.environ['PATH'].split(os.pathsep)

    for catalog in path_dirs:
        print(catalog)


def display_all_catalogs_with_subfiles():
    path_dirs = os.environ['PATH'].split(os.pathsep)

    for catalog in path_dirs:
        if os.path.exists(catalog):
            executables = [f for f in os.listdir(catalog) if
                           os.path.isfile(os.path.join(catalog, f)) and os.access(os.path.join(catalog, f), os.X_OK)]

            if executables:
                print(catalog)
                for exe in executables:
                    print(f"  {exe}")


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-s':
        display_all_catalogs_with_subfiles()
    else:
        display_all_catalogs()
