from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Source of the job posting"""

    url: str = Field(description="URL of the job posting")


class AgentResponse(BaseModel):
    """Schema for the agent response"""

    answer: str = Field(description="Answer to the question")
    sources: List[Source] = Field(description="Sources of the answer")
