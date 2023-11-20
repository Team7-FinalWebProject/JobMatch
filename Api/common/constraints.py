from typing import Annotated, Optional
from pydantic import StringConstraints

Allowed_Username = Annotated[str, StringConstraints(pattern=r'^\w{2,20}$')]
Allowed_Register_Password = Optional[Annotated[str, StringConstraints(min_length=8, max_length=30)]]
Allowed_Login_Password = Annotated[str, StringConstraints(min_length=8, max_length=30)]
_PROF_OFFER_STATUSES = ['active', 'hidden', 'private', 'matched']
Alloweed_ProfOffer_Statuses = Annotated[str, lambda s: s in _PROF_OFFER_STATUSES] 

##TODO: Store in DB -> Baseline skills + extendible by admin + Extra skills for company + admin approval ?
##Config table? Could also be a file
####-------------------------------------------------------------------------------------------####
_SKILL_NAMES = ['English', 'French', 'Computers']
_SKILL_LEVELS = [0, 10]
Allowed_Skill_Names = Annotated[str, lambda s: s in _SKILL_NAMES]
Allowed_Skill_Levels = Annotated[int, lambda n: _SKILL_LEVELS[0] <= n <= _SKILL_LEVELS[1]]
_USE_STATIC = False
def switch_skills_mode():
    _USE_STATIC = ~_USE_STATIC
Skills = dict[str, tuple[int, str]] if not _USE_STATIC else dict[Allowed_Skill_Names, tuple[Allowed_Skill_Levels, str]]
####-------------------------------------------------------------------------------------------####