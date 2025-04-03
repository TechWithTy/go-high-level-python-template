from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Property(BaseModel):
    key: str
    valueString: str

class RecordUpdate(BaseModel):
    type: str = Field(..., description="Indicates the type of record updated")
    locationId: str = Field(..., description="Identifies the location associated with the updated record")
    owners: List[str] = Field(..., description="Unique identifiers of users who own the record")
    followers: List[str] = Field(..., description="List of users following the record for updates")
    properties: List[Property] = Field(..., description="Key-value pairs representing additional record details")
    id: str = Field(..., description="Unique identifier for the updated record")
    timestamp: datetime = Field(..., description="Date and time when the record was updated")

# Example usage
example_data = {
    "id": "679b8f9bde6a0c356a0311b3",
    "locationId": "eHy2cOSZxMQzQ6Yyvl8P",
    "timestamp": "2025-02-10T08:26:05.961Z",
    "owners": ["60d5ec49f72b2a001f5f9d91"],
    "followers": ["60d5ec49f72b2a001f5f9d93", "60d5ec49f72b2a001f5f9d94"],
    "properties": [
        {
            "key": "pet_name",
            "valueString": "buddy"
        }
    ],
    "type": "RecordUpdate"
}

record_update = RecordUpdate(**example_data)

# Additional Notes:
# 1. Ensure your webhook listener is set up to handle POST requests.
# 2. The owners and followers fields help in managing record access and tracking.
# 3. The properties array allows for dynamic field storage and extensibility.
