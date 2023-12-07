declare function CompRequestMatch(
    profOfferId: number,
    compOfferId: number,
    authToken: string): Promise<{text: boolean | null }>;
export { CompRequestMatch };