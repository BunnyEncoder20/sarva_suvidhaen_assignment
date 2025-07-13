from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from typing import List, Optional

from app.database import get_db
from app.schemas.wheel_specs import WheelSpecCreate, WheelSpecGetResponse, WheelSpecPostResponse
from app.models.wheel_specs import WheelSpecification as WheelSpecs_Table

router = APIRouter(
    prefix="/api/forms/wheel-specifications",
    tags=["Posts"]
)

@router.get("/", response_model=WheelSpecGetResponse)
def get_wheel_specifications(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    db_query = db.query(WheelSpecs_Table)

    # add filters if they exist
    if formNumber:
        db_query = db_query.filter(WheelSpecs_Table.form_number == formNumber)
    if submittedBy:
        db_query = db_query.filter(WheelSpecs_Table.submitted_by == submittedBy)
    if submittedDate:
        db_query = db_query.filter(WheelSpecs_Table.submitted_date == submittedDate)

    # fetch the data from db
    raw_data = db_query.all()

    # debugging
    print("DB_DATA:\n",raw_data)

    # process data
    data = []
    for obj in raw_data:
        data.append({
            "formNumber": obj.form_number,
            "submittedBy": obj.submitted_by,
            "submittedDate": obj.submitted_date,
            "fields": {
                "condemningDia": obj.condemning_dia,
                "lastShopIssueSize": obj.last_shop_issue_size,
                "treadDiameterNew": obj.tread_diameter_new,
                "wheelGauge": obj.wheel_gauge
            }
        })

    return {
        "data": data,
        "message": "Filtered wheel specification forms fetched successfully.",
        "success": True
    }
