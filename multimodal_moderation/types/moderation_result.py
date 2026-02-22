from typing import Literal
from pydantic import BaseModel, Field


class ModerationResult(BaseModel):
    """Base moderation result model with common fields shared across all moderation types.

    The base model includes the core flags required by the rubric:
    - contains_pii, is_unfriendly, is_unprofessional (with sensible defaults of False)
    - rationale (required, no default)

    Specialized subclasses override fields to make them required (no default)
    and add modality-specific fields (e.g., is_disturbing, transcription).
    """

    rationale: str = Field(description="Explanation of what was harmful and why")
    contains_pii: bool = Field(
        default=False,
        description="Whether the content contains any personally-identifiable information (PII)",
    )
    is_unfriendly: bool = Field(
        default=False,
        description="Whether unfriendly tone or content was detected",
    )
    is_unprofessional: bool = Field(
        default=False,
        description="Whether unprofessional tone or content was detected",
    )


class TextModerationResult(ModerationResult):
    """Text moderation result. Inherits base flags and overrides them as required (no defaults)."""

    contains_pii: bool = Field(description="Whether the message contains any personally-identifiable information (PII)")
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")


class ImageModerationResult(ModerationResult):
    """Image moderation result. Overrides contains_pii and adds image-specific flags."""

    contains_pii: bool = Field(
        description="Whether the image contains any person, part of a person, or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the image is disturbing")
    is_low_quality: bool = Field(description="Whether the image is low quality")


class VideoModerationResult(ModerationResult):
    """Video moderation result. Overrides contains_pii and adds video-specific flags."""

    contains_pii: bool = Field(
        description="Whether the video contains any person or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the video is disturbing")
    is_low_quality: bool = Field(description="Whether the video is low quality")


class AudioModerationResult(ModerationResult):
    """Audio moderation result. Overrides base flags as required and adds transcription."""

    transcription: str = Field(description="Transcription of the audio content")
    contains_pii: bool = Field(
        description="Whether the audio contains any personally-identifiable information (PII) such as names, addresses, phone numbers"
    )
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")
