from pydantic import BaseModel
from typing import Optional
from typing import List
# from datetime import date

# Pydantic validation class for fields inside "Fields"
class WheelSpecFields(BaseModel):
    axleBoxHousingBoreDia: Optional[str] = None
    bearingSeatDiameter: Optional[str] = None
    condemningDia: Optional[str] = None
    intermediateWWP: Optional[str] = None
    lastShopIssueSize: Optional[str] = None
    rollerBearingBoreDia: Optional[str] = None
    rollerBearingOuterDia: Optional[str] = None
    rollerBearingWidth: Optional[str] = None
    treadDiameterNew: Optional[str] = None
    variationSameAxle: Optional[str] = None
    variationSameBogie: Optional[str] = None
    variationSameCoach: Optional[str] = None
    wheelDiscWidth: Optional[str] = None
    wheelGauge: Optional[str] = None
    wheelProfile: Optional[str] = None

# Pydantic validation class for Complete table
class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecFields



# --------------------------------------------------
# Pydantic validation class for Wheen Spec data Responses

# Get response data
class WheelSpecGetData(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecFields

# Get response
class WheelSpecGetResponse(BaseModel):
    data: List[WheelSpecGetData]
    message: Optional[str]
    success: bool

# Post response data
class WheelSpecPostData(BaseModel):
    formNumber: str
    status: str
    submittedBy: str
    submittedDate: str

# Pose response
class WheelSpecPostResponse(BaseModel):
    data: WheelSpecPostData
    message: Optional[str]
    success: bool
