import React, { useState } from 'react';


const SkillFilterForm = ({ onSubmitSFilters }) => {
  const [skills, setSkills] = useState([{ name: '', level: ''}]);

  const handleChange = (index, field, value) => {
    const updatedSkills = [...skills];
    updatedSkills[index][field] = value;
    setSkills(updatedSkills);
  };

  const handleAddSkill = () => {
    setSkills([...skills, { name: '', level: ''}]);
  };
  const handleRemoveSkill = () => {
    setSkills([...skills,].slice(0,1).concat([...skills,].slice(1,-1)));
  };

  const handleSave = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
      if (skill.name && skill.level) {
        acc[skill.name] = skill.level;
      }
      return acc;
    }, {});     onSubmitSFilters(skillsDictionary);
};

const handleL1 = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
        if (skill.name && skill.level) {
        acc[skill.name] = skill.level;
        }
        return acc;
    }, {});  };


const handleL2 = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
        if (skill.name && skill.level) {
        acc[skill.name] = skill.level;
        }
        return acc;
    }, {});  };

const handleL3 = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
        if (skill.name && skill.level) {
        acc[skill.name] = skill.level;
        }
        return acc;
    }, {});  };
    


  return (
    <div>
        {skills.map((skill, index) => (
        <div key={index} className="mb-4 p-2 border rounded-md shadow-md w-10/12">
        <input
            type="text"
            placeholder="Skill Name"
            value={skill.name}
            onChange={(e) => handleChange(index, 'name', e.target.value)}
            className="border rounded-md p-2 mr-2 w-11/12"
        />
        <input
            type="number"
            placeholder="Skill Level"
            value={skill.level}
            onChange={(e) => handleChange(index, 'level', e.target.value)}
            className="border rounded-md p-2 mr-2 w-11/12"
        />
        </div>
    ))}
    <button
        onClick={handleAddSkill}
        className="bg-blue-500 text-white w-7 px-2 py-2 rounded-md hover:bg-blue-600 mr-2"
    >
        +
    </button>
    <button
        onClick={handleRemoveSkill}
        className="bg-blue-500 text-white w-7 px-2 py-2 rounded-md hover:bg-blue-600 mr-2"
    >
        -
    </button>
    <button
        onClick={handleSave}
        className="bg-green-500 text-white w-12 px-2 py-2 rounded-md hover:bg-green-600"
    >
        Save
    </button>
    <button
        onClick={handleL1}
        className="bg-green-500 text-white w-7 px-2 py-2 rounded-md hover:bg-green-600"
    >
        L1
    </button>
    <button
        onClick={handleL2}
        className="bg-green-500 text-white w-7 px-2 py-2 rounded-md hover:bg-green-600"
    >
        L2
    </button>
    <button
        onClick={handleL3}
        className="bg-green-500 text-white w-7 px-2 py-2 rounded-md hover:bg-green-600"
    >
        L3
    </button>
</div>

  );
};

export default SkillFilterForm;