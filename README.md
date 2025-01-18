# PassManager

**PassManager** is a secure password manager for Linux that stores passwords in an encrypted database. It also includes a CLI tool to generate strong, random passwords.

## Features

- Secure storage of passwords using encryption.
- Command-line interface for managing passwords.
- `makepasswd`: a convenient CLI tool for generating random passwords.
- Linux-only support.

## Installation

1. Clone the repository:

  ```bash
  git clone git@github.com:jean0t/passmanager.git
  ```

2. Navigate to the project directory:

   ```bash
   cd passmanager
   ```

3. Install the package using `pip`:

   ```bash
   pip install ./dist/passmanager*.whl
   ```

## Usage

### Run PassManager

After installation, run the main program:

```bash
passmanager
```

### Generate Random Passwords

Use the `makepasswd` tool to generate random passwords:

```bash
makepasswd
```

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

## Compatibility

- **OS:** Linux only

