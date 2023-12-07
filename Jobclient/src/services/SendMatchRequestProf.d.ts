declare function ProfRequestMatch(
    compOfferId: number,
    profOfferId: number,
    authToken: string): Promise<{text: boolean | null }>;
export { ProfRequestMatch };