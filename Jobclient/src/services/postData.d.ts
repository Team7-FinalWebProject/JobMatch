type SkillFilters = {
    [key: string]: int;
  };

declare function postData(authToken: string | null, apiUrl: string, content: Any | null): Any;

export { postData };