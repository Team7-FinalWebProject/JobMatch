import React, { useState } from 'react';
// import { getSkillFilters } from '../services/getSkillFilters';
// import { saveSkillFilters } from '../services/saveSkillFilters';
import { getData } from '../services/getData';
import { postData } from '../services/postData';
import Cookies from 'universal-cookie';


interface Skill {
    name: string;
    level: number;
  }

const SkillFilterForm = ({ onSaveLoad, onSkillID }) => {
  const [skills, setSkills] = useState<Skill[]>([{ name: '', level: 5}]);


  const handleChange = (index, field, value) => {
    const updatedSkills = [...skills];
    updatedSkills[index][field] = value;
    setSkills(updatedSkills);
  };

  const handleAddSkill = () => {
    setSkills([...skills, { name: '', level: 5}]);
  };
  const handleRemoveSkill = () => {
    setSkills([...skills,].slice(0,1).concat([...skills,].slice(1,-1)));
  };

  const handleClear = () => {
    setSkills([{ name: '', level: 5}]);
    onSkillID(null)
  };
  const handleSave = () => {
    const skillsDictionary = skills.reduce((acc, skill) => {
      if (skill.name && skill.level) {
        acc[skill.name] = Number(skill.level);
      }
      onSkillID(0)
      return acc;
    }, {});
    const authToken = onSaveLoad()
    postData(authToken,'/search/filter', skillsDictionary);
};

const handleLoad = (id) => async () => {
    const authToken = onSaveLoad()
try {
    const newSkills = await getData(authToken, '/search/filter');
    if (Array.isArray(newSkills)) {
        const selectedObject = newSkills.find(item => item.id === id);
        // console.log(newSkills)
        if (selectedObject && selectedObject.filters && typeof selectedObject.filters === 'object') {
            const skillsArray = Object.entries(selectedObject.filters).map(([name, level]: [string, number]) => ({ name, level }));
            setSkills(skillsArray);
            onSkillID(id)
        } else {
            console.error('Invalid or missing data from getSkillFilters');
            // setSkills(newskills);
        }
    } else {
        console.error('Invalid or missing data from getSkillFilters');
        // setSkills(newskills);
    }
} catch (error) {
    console.error('Error fetching skill filters:', error);
}
};

  return (
<div className='space-y-6 py-1'>
    <button
        onClick={handleClear}
        className="bg-blue-500 text-white w-7 px-2 py-1 rounded-md hover:bg-blue-600 mr-1 shadow-md"
    >
        Clr
    </button>
    <button
        onClick={handleAddSkill}
        className="bg-blue-500 text-white w-7 px-2 py-1 rounded-md hover:bg-blue-600 mr-1 shadow-md"
    >
        +
    </button>
    <button
        onClick={handleRemoveSkill}
        className="bg-blue-500 text-white w-7 px-2 py-1 rounded-md hover:bg-blue-600 mr-1 shadow-md"
    >
        -
    </button>
    <div>
    <button
        onClick={handleSave}
        className="bg-green-500 text-white w-12 px-2 py-1 rounded-md hover:bg-green-600 mr-1 shadow-md"
    >
        Save
    </button>
    <button
        onClick={handleLoad(0)}
        className="bg-green-500 text-white w-7 px-2 py-1 rounded-md hover:bg-green-600 mr-1 shadow-md"
    >
        L1
    </button>
    <button
        onClick={handleLoad(1)}
        className="bg-green-500 text-white w-7 px-2 py-1 rounded-md hover:bg-green-600 mr-1 shadow-md"
    >
        L2
    </button>
    <button
        onClick={handleLoad(2)}
        className="bg-green-500 text-white w-7 px-2 py-1 rounded-md hover:bg-green-600 mr-1 shadow-md"
    >
        L3
    </button>
    </div>
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
</div>

  );
};

export default SkillFilterForm;