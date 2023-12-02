from typing import Annotated
from data.database import read_query
from data.readers import reader_one
from data.models.admin import ReadConfig

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

    @classmethod
    def refresh_config(cls):
        cls.config = check_config()
        cls._SKILL_NAMES = cls.config.baseline_skills or ['English', 'French', 'Computers']
        cls._SKILL_LEVELS = (cls.config.min_level, cls.config.max_level) or (0, 10)
        cls._USE_STATIC = cls.config.static_skills or False

    @classmethod
    def ALLOWED_SKILLS(cls):
        Allowed_Skill_Names = Annotated[str, lambda s: s in cls._SKILL_NAMES]
        Allowed_Skill_Levels = Annotated[int, lambda n: cls._SKILL_LEVELS[0] <= n <= cls._SKILL_LEVELS[1]]
        Skills = dict[str, tuple[int, str]] if not cls._USE_STATIC else dict[Allowed_Skill_Names, tuple[Allowed_Skill_Levels, str]]
        return Skills
    
    @classmethod
    def USE_STATIC(cls):
        return cls._USE_STATIC