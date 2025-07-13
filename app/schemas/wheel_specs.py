from pydantic import BaseModel
from typing import Optional
from typing import List
# from datetime import date

# Pydantic validation class for fields inside "Fields"
class WheelSpecFields(BaseModel):
    axleBoxHousingBoreDia: Optional[str]
    bearingSeatDiameter: Optional[str]
    condemningDia: Optional[str]
    intermediateWWP: Optional[str]
    lastShopIssueSize: Optional[str]
    rollerBearingBoreDia: Optional[str]
    rollerBearingOuterDia: Optional[str]
    rollerBearingWidth: Optional[str]
    treadDiameterNew: Optional[str]
    variationSameAxle: Optional[str]
    variationSameBogie: Optional[str]
    variationSameCoach: Optional[str]
    wheelDiscWidth: Optional[str]
    wheelGauge: Optional[str]
    wheelProfile: Optional[str]

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
