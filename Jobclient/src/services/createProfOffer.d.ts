declare function createProfOffer(
    description: string, 
    offer_status: string, 
    skills: JSON, 
    minSalary: number, 
    maxSalary: number,
    authToken: string): Promise<Data | null>;
export { createProfOffer };
