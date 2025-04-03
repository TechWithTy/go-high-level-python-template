from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OpportunityAssignedToUpdate(BaseModel):
    type: str = Field(..., description="Type of the webhook event")
    locationId: str = Field(..., description="ID of the location")
    id: str = Field(..., description="ID of the opportunity")
    assignedTo: str = Field(..., description="ID of the user the opportunity is assigned to")
    contactId: str = Field(..., description="ID of the associated contact")
    monetaryValue: float = Field(..., description="Monetary value of the opportunity")
    name: str = Field(..., description="Name of the opportunity")
    pipelineId: str = Field(..., description="ID of the pipeline")
    pipelineStageId: str = Field(..., description="ID of the pipeline stage")
    source: Optional[str] = Field(None, description="Source of the opportunity")
    status: str = Field(..., description="Status of the opportunity")
    dateAdded: datetime = Field(..., description="Date and time when the opportunity was added")

# Example usage:
example_data = {
    "type": "OpportunityAssignedToUpdate",
    "locationId": "ve9EPM428h8vShlRW1KT",
    "id": "wWhVuzqpRuOA1ZVWi4FC",
    "assignedTo": "bNl8QNGXhIQJLv8eeASQ",
    "contactId": "cJAWDskpkJHbRbhAT7bs",
    "monetaryValue": 40,
    "name": "Loram ipsu",
    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
    "source": "Loram ipsu",
    "status": "open",
    "dateAdded": "2021-11-26T12:41:02.193Z"
}

opportunity_update = OpportunityAssignedToUpdate(**example_data)
print(opportunity_update)