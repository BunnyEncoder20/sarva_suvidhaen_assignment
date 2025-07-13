from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from typing import List, Optional

from starlette.status import HTTP_201_CREATED

from app.database import get_db
from app.schemas.wheel_specs import WheelSpecCreate, WheelSpecGetResponse, WheelSpecPostResponse
from app.models.wheel_specs import WheelSpecification as WheelSpecs_Table

router = APIRouter(
    prefix="/api/forms/wheel-specifications",
    tags=["Wheel Specifications"]
)

@router.get("/", response_model=WheelSpecGetResponse, status_code=status.HTTP_200_OK)
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


@router.post("/", response_model=WheelSpecPostResponse, status_code=status.HTTP_201_CREATED)
def create_wheel_specification(
    data: WheelSpecCreate,
    db: Session = Depends(get_db)
):
    # make new wheel spec entry
    fields = data.fields
    new_wheel_specs = WheelSpecs_Table(
        form_number=data.formNumber,
        submitted_by=data.submittedBy,
        submitted_date=data.submittedDate,
        axle_box_housing_bore_dia=fields.axleBoxHousingBoreDia,
        bearing_seat_diameter=fields.bearingSeatDiameter,
        condemning_dia=fields.condemningDia,
        intermediate_wwp=fields.intermediateWWP,
        last_shop_issue_size=fields.lastShopIssueSize,
        roller_bearing_bore_dia=fields.rollerBearingBoreDia,
        roller_bearing_outer_dia=fields.rollerBearingOuterDia,
        roller_bearing_width=fields.rollerBearingWidth,
        tread_diameter_new=fields.treadDiameterNew,
        variation_same_axle=fields.variationSameAxle,
        variation_same_bogie=fields.variationSameBogie,
        variation_same_coach=fields.variationSameCoach,
        wheel_disc_width=fields.wheelDiscWidth,
        wheel_gauge=fields.wheelGauge,
        wheel_profile=fields.wheelProfile
    )

    db.add(new_wheel_specs)     # stage changes to db
    db.commit()                 # commit the new changes
    db.refresh(new_wheel_specs) # retreive the new entry

    return {
        "data": {
            "formNumber": new_wheel_specs.form_number,
            "status": "Saved",
            "submittedBy": new_wheel_specs.submitted_by,
            "submittedDate": new_wheel_specs.submitted_date
        },
        "message": "Wheel specification submitted successfully.",
        "success": True
    }
