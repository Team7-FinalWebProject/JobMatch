declare function submitSupportRequest(
    authToken: string | null, 
    content: string): Promise<File | null>;
export { submitSupportRequest };