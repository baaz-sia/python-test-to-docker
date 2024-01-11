import subprocess


def execute_code(code, language):
    # Create Docker command based on language
    docker_command = f'docker run -i --rm {language}-image /bin/sh -c "{code}"'

    # Execute code in Docker container
    process = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f'Error: {error.decode("utf-8")}')
    else:
        print(f'Output: {output.decode("utf-8")}')


# Call the function with user code and selected language
user_code = 'print("Hello, World!")'
execute_code(user_code, 'python')
