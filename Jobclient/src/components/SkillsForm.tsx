import React, { useState } from 'react';


const SkillForm = ({ onAddSkill }) => {
  const [skills, setSkills] = useState([{ name: '', level: '', levelName: '' }]);

  const handleChange = (index, field, value) => {
    const updatedSkills = [...skills];
    updatedSkills[index][field] = value;
    setSkills(updatedSkills);
  };

  const handleAddSkill = () => {
    setSkills([...skills, { name: '', level: '', levelName: '' }]);
  };

  const handleSubmit = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
      if (skill.name && skill.level && skill.levelName) {
        acc[skill.name] = [skill.level, skill.levelName];
      }
      return acc;
    }, {});

    onAddSkill(skillsDictionary);
  };

  return (
    <div>
        {skills.map((skill, index) => (
        <div key={index} className="mb-4 p-2 border rounded-md shadow-md">
        <input
            type="text"
            placeholder="Skill Name"
            value={skill.name}
            onChange={(e) => handleChange(index, 'name', e.target.value)}
            className="border rounded-md p-2 mr-2"
        />
        <input
            type="number"
            placeholder="Skill Level"
            value={skill.level}
            onChange={(e) => handleChange(index, 'level', e.target.value)}
            className="border rounded-md p-2 mr-2"
        />
        <input
            type="text"
            placeholder="Level Name"
            value={skill.levelName}
            onChange={(e) => handleChange(index, 'levelName', e.target.value)}
            className="border rounded-md p-2"
        />
        </div>
    ))}
    <button
        onClick={handleAddSkill}
        className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 mr-2"
    >
        Add Skill
    </button>
    <button
        onClick={handleSubmit}
        className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
    >
        Submit
    </button>
</div>

  );
};

export default SkillForm;
