declare function CompRequestMatch(
    profOfferId: number,
    compOfferId: number,
    authToken: string): Promise<{text: string | null }>;
export { CompRequestMatch };