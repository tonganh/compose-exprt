import datetime
from pydantic import BaseModel
from typing import List, Optional

class Expert(BaseModel):
    id: str = "VN-001-AI"
    name: str = "Geogre"
    title: Optional[List[str]] = ["Ph.D", "Professor"]
    dob: Optional[str] = "1954-01-01"
    email: Optional[str] = "geogre@gmail.com"
    citizen: Optional[List[str]] = ["USA", "Canada"]
    organization: Optional[List[str]] = ["University of California, Berkeley", "University of California, Los Angeles"]
    profile_url: Optional[str] = "https://www.linkedin.com/in/geogre/"
    citations: int = 1232
    h_index: int = 34
    i10_index: int = 68
    expertise: List[str] = ["Machine Learning", "Deep Learning", "Natural Language Processing"]
    coauthors: List[str] = ["John Doe", "Jane Doe"] 