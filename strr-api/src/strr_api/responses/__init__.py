"""
This module is for the responses used in the API.
"""
from .AccountResponse import Account
from .DocumentResponse import Document
from .EventsResponse import Events
from .Pagination import Pagination
from .RegistrationResponse import Registration
from .SBCAccountResponse import SBCAccount

from .AutoApprovalResponse import AutoApproval  # isort: skip
from .AutoApprovalRecordResponse import AutoApprovalRecord  # isort: skip
from .LTSAResponse import LtsaResponse, TitleSummaries  # isort: skip
from .LTSARecordResponse import LTSARecord  # isort: skip
