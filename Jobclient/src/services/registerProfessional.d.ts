declare function registerProfessional(
    username: string, 
    password: string, 
    firstName: string, 
    lastName: string, 
    address: string, 
    summary: string, 
    photo: File): Promise<string | null>;
export { registerProfessional };