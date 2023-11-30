declare function submitMessage(
    authToken: string | null, 
    username: string, 
    content: string): Promise<Data | null>;
export { submitMessage };