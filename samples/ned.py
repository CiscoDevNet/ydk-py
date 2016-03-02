#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

#  ----------------------------------------------------------------
#  ned.py Sample program illustrating use of generated api
#  ydk.models.ned.ned.py 
#


from ydk.types import Empty
from ydk.services import CRUDService
import logging

from samples.session_mgr import establish_session
from ydk.errors import YPYError
from ydk.models.ned import ned

def ned_run(crud_service, session):
    native = ned.Native()
    sr = native.segment_routing
    sr.mpls = sr.Mpls()   
    
if __name__ == "__main__":
    session = establish_session()
    crud_service = CRUDService()
    ned_run(crud_service, session)
    exit()
