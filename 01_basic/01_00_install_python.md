# Install Python

## Go to official website of python and download python according to your system https://www.python.org/downloads/

- Choose your operating system, basically website will detect your machine, but be sure what you are downloading

- Installation is straight forward, check the add PATH

![Alt text](/images/01_python_installation.png)

### verify installation
After installation is completed, check if the installation is successful or not

  - go to any terminal (bash or powershell is recommended)
  ```
  python --version
  ```
  - If python is installed properly, it will gave you the version of python else gave the error
  ![Alt text](/images/01_python_install_verification.png)


Python could be written in notepad :) but we will be using VS Code as our IDE

## Install VS Code
- go to download section of official vs code website and download vs code according to your operating system
https://code.visualstudio.com/Download

- Installation is straight forward,
    - Accept the agreement after reading it, go to next page
    - Select all options
        - Add **"Open with Code"** : this will open vs code from any folder when you right click and select open with Code.
        - Register Code as an editor 
        - add to PATH


![Alt text](/images/01_install_vscode.png)

After installation of vs code is completed, we need to add python extension.
### Add python extension
- click on Extensions in left bar
- In search box search for python, or usually Python extension is displayed in popular extension section
- Select Python extension by Microsoft
- It will open detail window in right, click on install button
  
  ![Alt text](/images/01_install_extension.png) 

- After installation is completed 3 extension will be installed.
    - Python
    - Python Debugger
    - Pylance
    
    ![Alt text](/images/01_installed_extension.png)

## Install git and gitbash (for windows)
- go to git offical webpage to the download page.
  https://git-scm.com/download/win
- select your operating system and also which release of git you want. Usually stable release are at the beginning. For me my maching is 64-bit so I click on 
  - 64-bit Git for Windows Setup
- Once download is completed installation is straight forward
  - read terms and conditions and do next
  - select the location where you want to install and do next
  - leave all the component selected as it is and do next 
  ![Alt text](/images/01_select_git_component.png)
  - chooseing the default editor used by Git, select Use Visual Studio Code as Git's default editor
    ![Alt text](/images/01_git_default_editor.png)
  - Adjusting the name of initial branch, leave default and do next
  - Adjusting your PATH envionment, leave default selection and do next
  ![Alt text](/images/01_git_path.png)
  - Choosing HTTPS transport backend, leave default selection and do next
  - Configuring the line editing conversions, leave default selection and do next
  - Configuring the terminal emulator to use with Git Bash, leave default selection and do next
  - Choose the default behavior of 'git pull', leave default selection and do next
  - Choose a credential helper, leave default selection and do next
  - Configuring extra options, leave default selection and do next
  - Configuring experimental options, leave default selection (not selected anything) and click on install
