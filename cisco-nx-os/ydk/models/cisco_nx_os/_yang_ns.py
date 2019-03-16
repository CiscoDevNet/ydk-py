BUNDLE_NAME = "cisco_nx_os"

CAPABILITIES = {
    "Cisco-NX-OS-device": "2019-02-17",
}

ENTITY_LOOKUP = {
    ("http://cisco.com/ns/yang/cisco-nx-os-device", "System"): "Cisco_NX_OS_device.System",
    ("Cisco-NX-OS-device", "System"): "Cisco_NX_OS_device.System",
}

NAMESPACE_LOOKUP = {
    "Cisco-NX-OS-device": "http://cisco.com/ns/yang/cisco-nx-os-device",
}

IDENTITY_LOOKUP = {
    'Cisco-NX-OS-device:inactive':('ydk.models.cisco_nx_os.Cisco_NX_OS_device', 'Inactive'),
}

