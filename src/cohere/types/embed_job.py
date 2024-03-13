# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .api_meta import ApiMeta
from .embed_job_status import EmbedJobStatus
from .embed_job_truncate import EmbedJobTruncate

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EmbedJob(pydantic.BaseModel):
    job_id: str = pydantic.Field()
    """
    ID of the embed job
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the embed job
    """

    status: EmbedJobStatus = pydantic.Field()
    """
    The status of the embed job
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The creation date of the embed job
    """

    input_dataset_id: str = pydantic.Field()
    """
    ID of the input dataset
    """

    output_dataset_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resulting output dataset
    """

    model: str = pydantic.Field()
    """
    ID of the model used to embed
    """

    truncate: EmbedJobTruncate = pydantic.Field()
    """
    The truncation option used
    """

    meta: typing.Optional[ApiMeta] = None

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
