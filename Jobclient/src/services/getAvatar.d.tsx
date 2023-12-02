declare function getAvatar(
    authToken: string | null, 
    apiUrl: string): Promise<Blob | null>;

export { getAvatar };