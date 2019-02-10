<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [YDK](#ydk)
- [Installation](#installation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<a href="https://github.com/CiscoDevNet/ydk-py"><img src="https://cloud.githubusercontent.com/assets/17089095/14834057/2e1fe270-0bb7-11e6-9e94-73dd7d71e87d.png" height="240" width="240" ></a>

# YDK

YDK or YANG Development Kit is a Software Development Kit that provides API's that are modeled in YANG.

# Installation

##gNMI Requirements

In order to enable YDK support for gNMI protocol, which is optional, the following third party software must be installed prior to gNMI YDK component installation.

###Install protobuf and protoc

```
    wget https://github.com/google/protobuf/releases/download/v3.5.0/protobuf-cpp-3.5.0.zip
    unzip protobuf-cpp-3.5.0.zip
    cd protobuf-3.5.0
    ./configure
    make
    make check
    sudo make install
    sudo ldconfig
```

###Install gRPC

```
    git clone -b v1.9.1 https://github.com/grpc/grpc
    cd grpc
    git submodule update --init
    make
    sudo make install
    sudo ldconfig
    cd -
```

###Run-time environment

There is an open issue with gRPC on Centos/Fedora, which requires an extra step before running any YDK gNMI application. See this issue on `GRPC GitHub <https://github.com/grpc/grpc/issues/10942#issuecomment-312565041>`_ 
for details. As a workaround, the YDK based application runtime environment must include setting of `LD_LIBRARY_PATH` variable:

```
    PROTO="/Your-Protobuf-and-Grpc-installation-directory"
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PROTO/grpc/libs/opt:$PROTO/protobuf-3.5.0/src/.libs:/usr/local/lib64
```
