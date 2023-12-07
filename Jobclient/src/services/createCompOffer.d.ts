declare function createCompOffer(
    requirements: JSON, 
    minSalary: number, 
    maxSalary: number,
    authToken: string): Promise<Data | null>;
export { createCompOffer };
