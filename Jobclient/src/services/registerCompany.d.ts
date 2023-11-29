declare function registerCompany(
    username: string,
    password: string,
    compnayName: string,
    description: string,
    address: string
): Promise<Data | null>;
export { registerCompany };