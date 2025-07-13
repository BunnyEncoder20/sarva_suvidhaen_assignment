from sqlalchemy import Column, String, Date, Integer
from app.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specs"

    # Outer fields
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(String, nullable=False)

    # Fields inside 'fields' object
    axle_box_housing_bore_dia = Column(String)
    bearing_seat_diameter = Column(String)
    condemning_dia = Column(String)
    intermediate_wwp = Column(String)
    last_shop_issue_size = Column(String)
    roller_bearing_bore_dia = Column(String)
    roller_bearing_outer_dia = Column(String)
    roller_bearing_width = Column(String)
    tread_diameter_new = Column(String)
    variation_same_axle = Column(String)
    variation_same_bogie = Column(String)
    variation_same_coach = Column(String)
    wheel_disc_width = Column(String)
    wheel_gauge = Column(String)
    wheel_profile = Column(String)
