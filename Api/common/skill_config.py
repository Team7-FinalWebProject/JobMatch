from typing import Annotated, List, Dict, Tuple
from pydantic.functional_validators import AfterValidator
from data.database import read_query
from data.readers import reader_one
from data.models.admin import ReadConfig
from dotenv import load_dotenv
load_dotenv()

def check_config():
    data = read_query(
        '''SELECT static_skills,min_level,max_level,baseline_skills,approved_skills,pending_approval_skills from config
           WHERE lock = %s''', ('X',))
    return reader_one(ReadConfig, data)

class Config:
    config = check_config()
    _SKILL_NAMES = config.baseline_skills or ['English', 'French', 'Computers']
    _SKILL_LEVELS = (config.min_level, config.max_level) or (0, 10)
    _USE_STATIC = config.static_skills or False
    Valid_int = Annotated[int, AfterValidator(int)]
    Valid_str = Annotated[str, AfterValidator(str)]

    @classmethod
    def refresh_config(cls):
        cls.config = check_config()
        cls._SKILL_NAMES = cls.config.baseline_skills or ['English', 'French', 'Computers']
        cls._SKILL_LEVELS = (cls.config.min_level, cls.config.max_level) or (0, 10)
        cls._USE_STATIC = cls.config.static_skills or False

    @classmethod
    def ALLOWED_SKILLS(cls):
        Allowed_Skill_Names = Annotated[cls.Valid_str, lambda s: s in cls._SKILL_NAMES]
        Allowed_Skill_Levels = Annotated[cls.Valid_int, lambda n: cls._SKILL_LEVELS[0] <= n <= cls._SKILL_LEVELS[1]]
        Skills = Dict[cls.Valid_str, Tuple[cls.Valid_int, cls.Valid_str]] if not cls._USE_STATIC else Dict[Allowed_Skill_Names, Tuple[Allowed_Skill_Levels, cls.Valid_str]]
        return Skills
    
    @classmethod
    def FILTER_SKILLS(cls):
        return Dict[cls.Valid_str, cls.Valid_int]

    @classmethod
    def USE_STATIC(cls):
        return cls._USE_STATIC