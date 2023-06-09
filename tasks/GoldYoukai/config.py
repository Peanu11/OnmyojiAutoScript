# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field

from tasks.GoldYoukai.config_scheduler import Scheduler


class GoldYoukai(BaseModel):
    scheduler: Scheduler = Field(default_factory=Scheduler)