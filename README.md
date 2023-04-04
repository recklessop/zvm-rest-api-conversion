# zvm-rest-api-conversion

## Zerto REST API Examples

This repository contains examples of using the Zerto REST API to interact with a Zerto Virtual Manager (ZVM) instance. There are two branches in this repository:

- `windows-zvm`: [Open](https://github.com/recklessop/zvm-rest-api-conversion/tree/windows-zvm) Contains an example script (`get-vpgs.py`) for connecting to a Windows-based ZVM instance and retrieving a list of Virtual Protection Groups (VPGs). 
- `linux-zvm`: [Open](https://github.com/recklessop/zvm-rest-api-conversion/tree/linux-zvm) Contains an updated example script (`get-vpgs.py`) that uses Keycloak-based authentication to connect to a Linux-based ZVM instance running Zerto version 9.7 and retrieve a list of VPGs.
- `main`: Contains the same updated example script as the `linux-zvm` branch, which is compatible with a Linux-based ZVM instance running Zerto version 9.7.

## Usage

To use the example scripts, simply download the appropriate branch or clone the entire repository:

```
git clone https://github.com/your-username/zerto-rest-api-examples.git
```


Then, navigate to the appropriate branch and run the example script using Python:

```
cd zerto-rest-api-examples/linux-zvm
python get-vpgs.py
```


## Contributing

Contributions are welcome! If you have an example script for another Zerto REST API use case or would like to improve the existing scripts, please feel free to open a pull request.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more information.
