#!/usr/bin/env bash
#################################################
# Please do not make any changes to this file,  #
# change the variables in webui-user.sh instead #
#################################################

use_venv=1
venv_dir="venv"
#source ./venv/bin/activate
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
printf "Script Dir: ${SCRIPT_DIR}\n"


if ! command -v xterm &> /dev/null
then
    echo -e "\033[31m Xterm not found. Trying to install (might need sudo) \033[0m"
    apt install xterm
fi

if ! which python3.10 &> /dev/null
then
    printf "\n%s\n" "${delimiter}"
    printf "\e[1m\e[31mERROR: python3.10 needed, but is not installed? Trying to install (might need sudo)...\e[0m"
    printf "\n%s\n" "${delimiter}"
    sudo apt update
    sudo apt install software-properties-common -y
    sudo apt upgrade -y
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt update
    sudo apt install python3.10 -y
    sudo apt install python3.10-distutils -y
fi

if ! which python3.10 &> /dev/null
then
    printf "\n%s\n" "${delimiter}"
    printf "\e[1m\e[31mERROR: python3.10 needed, but can't reach it through python3.10 command. Aborting.'...\e[0m"
    printf "\n%s\n" "${delimiter}"
    exit 1
fi

if ! dpkg-query -W -f='${Status}' python3.10-venv | grep " installed" &> /dev/null
then
    echo -e "\033[31m python3.10-venv not found. Trying to install (needs sudo) \033[0m"
    sudo apt install  python3.10-venv -y
    rm -R ${SCRIPT_DIR}/venv
fi

if ! dpkg -l | grep python3.10-distutils &> /dev/null
then
    echo -e "\033[31m python3.10-distutils not found. Trying to install (might need sudo) \033[0m"
    apt install python3.10-distutils -y
fi

if ! ldconfig -p | grep libxcb-cursor &> /dev/null
then
    echo -e "\033[31m libxcb-cursor not found. Trying to install (needs sudo) \033[0m"
    sudo apt-get install libxcb-cursor0
fi


# If run from macOS, load defaults from webui-macos-env.sh
if [[ "$OSTYPE" == "darwin"* ]]; then
    if [[ -f "$SCRIPT_DIR"/webui-macos-env.sh ]]
        then
        source "$SCRIPT_DIR"/webui-macos-env.sh
    fi
fi

# Set defaults
# Install directory without trailing slash
if [[ -z "${install_dir}" ]]
then
    install_dir="$SCRIPT_DIR"
fi

# Name of the subdirectory (defaults to stable-diffusion-webui)
if [[ -z "${clone_dir}" ]]
then
    clone_dir="Deforumation"
fi

# python3 executable
if [[ -z "${python_cmd}" ]]
then
    python_cmd="python3.10"
fi

# python3 venv without trailing slash (defaults to ${install_dir}/${clone_dir}/venv)
if [[ -z "${venv_dir}" ]] && [[ $use_venv -eq 1 ]]
then
    venv_dir="venv"
fi


# Do not reinstall existing pip packages on Debian/Ubuntu
export PIP_IGNORE_INSTALLED=0
# Pretty print
delimiter="################################################################"

if [[ $use_venv -eq 1 ]] && ! "${python_cmd}" -c "import venv" &>/dev/null
then
    printf "\n%s\n" "${delimiter}"
    printf "\e[1m\e[31mERROR: python3-venv is not installed, aborting...\e[0m"
    printf "\n%s\n" "${delimiter}"
    exit 1
fi

printf "\n----------\n${VIRTUAL_ENV}\n-------------\n"
if [[ $use_venv -eq 1 ]] && [[ -z "${VIRTUAL_ENV}" ]];
then
    printf "\n%s\n" "${delimiter}"
    printf "Create and activate python venv"
    printf "\n%s\n" "${delimiter}"
    cd "${install_dir}"/ || { printf "\e[1m\e[31mERROR: Can't cd to %s/%s/, aborting...\e[0m" "${install_dir}" "${clone_dir}"; exit 1; }
    if [[ ! -d "${venv_dir}" ]]
    then
        "${python_cmd}" -m venv "${venv_dir}"
     first_launch=1
    fi
    # shellcheck source=/dev/null
    if [[ -f "${venv_dir}"/bin/activate ]]
    then
        printf "${install_dir}/${venv_dir}"/bin/activate
        source "${venv_dir}"/bin/activate
    else
        printf "\n%s\n" "${delimiter}"
        printf "\e[1m\e[31mERROR: Cannot activate python venv, aborting...\e[0m"
        printf "\n%s\n" "${delimiter}"
        exit 1
    fi
else
    #source "${install_dir}/${venv_dir}"/bin/activate
    printf "\n%s\n" "${delimiter}"
    printf "python venv already activate or run without venv: ${VIRTUAL_ENV}"
    printf "\n%s\n" "${delimiter}"
fi

KEEP_GOING=1
export SD_WEBUI_RESTART=tmp/restart
while [[ "$KEEP_GOING" -eq "1" ]]; do
    printf "\n%s\n" "${delimiter}"
    printf "Launching stuff..."
    printf "\n%s\n" "${delimiter}"
        #prepare_tcmalloc
        #"${python_cmd}" -u "${LAUNCH_SCRIPT}" "$@"
    #fi

    if [[ ! -f tmp/restart ]]; then
        KEEP_GOING=0
    fi
done

printf "\n"
"${python_cmd}" -m pip install -r requirements_linux.txt
xterm -e "${python_cmd}" -u mediator.py "$1" &
xterm -e "${python_cmd}" -u deforumation.py "$2" &
deactivate
printf $(which pip)
printf "\n\n"