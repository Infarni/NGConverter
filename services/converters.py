import subprocess


def convert(format_file: str, file_path: str) -> str:
    new_path = "".join(file_path.split('.')[:-1]) + f".{format_file}"

    command = ["unoconv", "-f", format_file, "-o", new_path, file_path]
    subprocess.run(command)

    return new_path
