"""
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2011 Cisco Systems, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Sumit Naiksatam, Cisco Systems, Inc.
# @author: Rohit Agarwalla, Cisco Systems, Inc.
"""
"""
Exceptions used by the Cisco plugin
"""
from quantum.common import exceptions


class NoMoreNics(exceptions.QuantumException):
    """No more dynamic nics are available in the system"""
    message = _("Unable to complete operation. No more dynamic nics are " \
                 "available in the system.")


class PortProfileLimit(exceptions.QuantumException):
    """Port profile limit has been hit"""
    message = _("Unable to complete operation on port %(port_id)s " \
                "for network %(net_id)s. The system has reached the maximum" \
                "limit of allowed port profiles.")


class UCSMPortProfileLimit(exceptions.QuantumException):
    """UCSM Port profile limit has been hit"""
    message = _("Unable to complete operation on port %(port_id)s " \
                "for network %(net_id)s. The system has reached the maximum" \
                "limit of allowed UCSM port profiles.")


class NetworksLimit(exceptions.QuantumException):
    """Total number of network objects limit has been hit"""
    message = _("Unable to create new network. Number of networks" \
                "for the system has exceeded the limit")


class PortProfileNotFound(exceptions.QuantumException):
    """Port profile cannot be found"""
    message = _("Port profile %(portprofile_id)s could not be found " \
                "for tenant %(tenant_id)s")


class PortProfileInvalidDelete(exceptions.QuantumException):
    """Port profile cannot be deleted since its being used"""
    message = _("Port profile %(profile_id)s could not be deleted " \
                "for tenant %(tenant_id)s since port associations exist")


class NetworkVlanBindingAlreadyExists(exceptions.QuantumException):
    """Binding cannot be created, since it already exists"""
    message = _("NetworkVlanBinding for %(vlan_id)s and network " \
                "%(network_id)s already exists")


class PortProfileAlreadyExists(exceptions.QuantumException):
    """Port profile cannot be created since it already exisits"""
    message = _("PortProfile %(pp_name) for %(tenant_id)s " \
                "already exists")


class PortProfileBindingAlreadyExists(exceptions.QuantumException):
    """Binding cannot be created, since it already exists"""
    message = _("PortProfileBinding for port profile %(pp_id)s to " \
                 "port %(port_id) already exists")


class VlanIDNotFound(exceptions.QuantumException):
    """VLAN ID cannot be found"""
    message = _("Vlan ID %(vlan_id)s not found")


class VlanIDNotAvailable(exceptions.QuantumException):
    """VLAN ID is reserved"""
    message = _("No available Vlan ID found")

try:
    _("test")
except NameError:

    def _(a_string):
        """
        Default implementation of the gettext string
        translation function: no translation
        """
        return a_string
except TypeError:
    # during doctesting, _ might mean something else
    pass