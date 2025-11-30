# GraphAuto
Afim de auxiliar pessoas que não tem familiaridade com código ou terminal, resolvi criar programas executáveis com interface gráfica em python. Assim, qualquer um que precise otimizar sua máquina, seja em qual for o sistema operacional, poderá usar um desses programas e executá-los facilmente. Podendo assim otimizar seu tempo e poupar esforços.


## Organização do projeto
- As pastas principais organizam os programas conforme o sistema operacional para melhor organização. Contudo, pode haver programas que rodem em mais de um sistema operacional.
    -- Exemplo: na pasta Win há programas que rodam no Windows e podem rodar no Linux, mas que, foram criados para serem usados com foco no Windows.

# GraphAuto: User-Friendly System Automation Tools

GraphAuto is a collection of Python-based graphical applications designed to simplify common system tasks and machine optimization for users without coding or terminal experience. This project aims to empower individuals to enhance their productivity and maintain their systems with intuitive, click-and-run tools.

## Key Features

*   **Effortless File Backup**: A dedicated tool to easily back up folders and files from a specified source to a destination, saving time and ensuring data safety.
*   **Automated Directory Structure Creation**: Generate complex project directory and file structures rapidly from a simple, indented text-based blueprint. This is ideal for developers, students, and project managers needing consistent and organized project setups.
*   **Windows System Optimization (WinTune)**: A powerful utility to improve Windows machine performance by cleaning temporary files, defragmenting disks, and performing other essential maintenance tasks with a user-friendly interface.
*   **User-Friendly Graphical Interfaces**: All tools are provided as standalone executables with intuitive graphical interfaces, eliminating the need for command-line interaction or technical expertise.
*   **Cross-Platform Potential**: While currently focused on Windows, the modular architecture allows for future expansion and development of tools for other operating systems.

## Tech Stack

*   **Python**: The core programming language used for developing all applications.
*   **PyInstaller**: Utilized to package the Python scripts into standalone executables, making them easy to distribute and run without requiring a Python installation on the end-user's machine.
*   **Standard Python Libraries**: Leveraged for file system operations, system commands, and graphical user interface components (specific GUI library not explicitly named but implied by the project's nature).

## Getting Started

The tools within GraphAuto are designed to be run as standalone executables.

### For End-Users

1.  **Download**: Navigate to the specific tool's directory (e.g., `Win/Backup/`) and locate the `dist` folder. Download the executable file (e.g., `backup.exe`, `Matrure.exe`, `WinTune.exe`).
2.  **Run**: Simply double-click the downloaded executable file to launch the application.
    *   **Note**: For the Windows Performance Optimizer (WinTune), it is recommended to run the executable as an administrator to enable all features.

### For Developers (to build from source)

If you wish to modify the tools or build the executables yourself, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/sousadevelop/GraphAuto.git
    cd GraphAuto
    ```
2.  **Install Python**: Ensure you have Python (version 3.x recommended) installed on your system.
3.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```
4.  **Build a Specific Tool**:
    *   Navigate to the directory of the tool you want to build (e.g., `cd Win/Backup`).
    *   Run PyInstaller using the provided `.spec` file:
        ```bash
        pyinstaller backup.spec
        ```
        (Replace `backup.spec` with `Matrure.spec` or `WinTune.spec` for other tools).
    *   The generated executable will be located in the `dist` folder within that tool's directory.

## Usage Guide

Each tool offers a straightforward graphical interface for its specific function.

### 1. Backup Tool

*   **Purpose**: To efficiently back up files and folders from a source to a destination.
*   **How to Use**:
    1.  Launch `backup.exe`.
    2.  The interface will prompt you to select a source folder and a destination folder.
    3.  Once selected, click the "Backup" button to initiate the file transfer.
*   **Business Value**: Automates routine data backup, ensuring important files are safely duplicated without manual dragging and dropping, saving significant time and reducing the risk of data loss.

### 2. Directory Structure Creator (Matrure)

*   **Purpose**: To quickly generate a hierarchical structure of directories and files based on a simple text input.
*   **How to Use**:
    1.  **Prepare Input File**: Create a text file (e.g., `estrutura.txt`) where you define your desired directory and file hierarchy using indentation (typically 4 spaces per level). An example `estrutura.txt` is provided in the `Win/Make_structure_of_directories/` folder.
        *   Directories should end with a `/`.
        *   Files will be created with default content based on their extension (e.g., `.md`, `.ps1`).
    2.  Launch `Matrure.exe`.
    3.  The application will likely ask for the path to your `estrutura.txt` file.
    4.  Confirm the creation, and the program will build the specified structure.
*   **Business Value**: Streamlines project setup, ensures consistent folder structures across projects or teams, and eliminates tedious manual folder creation, boosting productivity for developers, educators, and content creators.

### 3. Windows Performance Optimizer (WinTune)

*   **Purpose**: To perform various actions to optimize the Windows operating system's performance.
*   **How to Use**:
    1.  Launch `WinTune.exe`. **For full functionality, right-click and select "Run as administrator."**
    2.  The graphical interface will present various optimization options (e.g., clean temporary files, defragment disk).
    3.  Select the desired action and click the corresponding button to execute it.
*   **Business Value**: Empowers non-technical users to maintain and improve their Windows machine's performance, extending hardware lifespan, reducing system slowdowns, and enhancing overall user experience without needing deep technical knowledge.

## Architecture Overview

The GraphAuto project is organized to be modular and extensible:

*   **Operating System Grouping**: The top-level directories (e.g., `Win/`) categorize tools based on the operating system they target. This allows for clear organization and future expansion to other platforms like Linux or macOS.
*   **Tool-Specific Directories**: Each individual tool (e.g., `Backup`, `Make_structure_of_directories`, `Optimization_of_Machine_Performance`) resides in its own sub-directory.
*   **Standalone Executables**: Each tool is developed as a Python script and then compiled into a standalone executable using PyInstaller. This approach ensures that end-users can run the applications without needing to install Python or any dependencies.
*   **Focus on User Experience**: The core design principle is to provide simple, graphical interfaces that abstract away the complexities of system commands and file operations, making powerful automation accessible to everyone.

## API Reference

This project consists of standalone graphical applications designed for direct user interaction. It does not expose a public API for programmatic access or integration with other software.
