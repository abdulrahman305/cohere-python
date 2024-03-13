# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .chat_message_role import ChatMessageRole

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChatMessage(pydantic.BaseModel):
    """
    A single message in a chat history. Contains the role of the sender, the text contents of the message.
    """

    role: ChatMessageRole = pydantic.Field()
    """
    One of CHATBOT|USER to identify who the message is coming from.
    """

    message: str = pydantic.Field()
    """
    Contents of the chat message.
    """

    generation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the generated reply. Useful for submitting feedback.
    """

    response_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the response.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
