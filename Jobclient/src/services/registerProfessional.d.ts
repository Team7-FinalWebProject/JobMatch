declare function registerProfessional(
    username: string, 
    password: string, 
    firstName: string, 
    lastName: string, 
    address: string, 
    summary: string): Promise<Data | null>;
export { registerProfessional };