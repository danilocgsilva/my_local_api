import os
import argparse

def main():
    os.system(
        set_os_command(get_port())
    )

def set_os_command(port = None) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pre_command = 'cd ' + dir_path + "; flask run"
    if port:
        pre_command += " --port " + port
    command = pre_command
    return command

def get_port():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port',
        '-p',
        required=False
    )
    args = parser.parse_args()
    return args.port

