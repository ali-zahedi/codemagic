<!--![GitHub All Releases](https://img.shields.io/github/downloads/ali-zahedi/codemagic/total)-->
<!--![GitHub issues](https://img.shields.io/github/issues/ali-zahedi/codemagic)-->
![GitHub](https://img.shields.io/github/license/ali-zahedi/codemagic)
![GitHub](https://img.shields.io/pypi/pyversions/codemagic.svg?maxAge=2592000)
![GitHub](https://img.shields.io/pypi/v/codemagic.svg?maxAge=2592000)
![image info](./logo.svg)

[[_TOC_]]


# Overview

With the magic of [Codemagic](https://codemagic.io), you can build, test, and publish Flutter apps with zero configuration and run builds in controlled environments using custom workflows. If you have a native Android, iOS, or React Native app, Codemagic has got your back, just use the codemagic.

For more information, visit the [Codemagic api docs](https://docs.codemagic.io/rest-api/overview/) setup guide.

# Installation

To install Codemagic Python SDK, simply execute the following command in a terminal:

```shell script
pip install codemagic
```

# Usage

First of all you need to get token. The access token is available via the Codemagic UI in  **User settings > Integrations > Codemagic API > Show**.

1. Create Codemagic instance

    ```python
    from codemagic import Codemagic, Build, BuildStatus
    
    codemagic = Codemagic(token=token)
    ```
   
1. Create `build`.

   ```python
   build: Build = codemagic.start_build(app_id=app_id, workflow_id=workflow_id, branch=branch, environment=environment)      
   if build.status == BuildStatus.QUEUED:
       print("Build request start success.")
   ```
    
1. Get `list build`. You can filter `builds` base on parameters.

    ```python
    builds: [Build] = codemagic.list_of_builds()
    ```

1. Get `details of build`.

    ```python
    build: Build = codemagic.get_build(pk=pk)
    ```

# Supported Python Versions

We currently support Python 3.6+.

# TODO

- [] Documentation

## Develop

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.


