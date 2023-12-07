declare function ProfRequestMatch(
    compOfferId: number,
    profOfferId: number,
    authToken: string): Promise<{text: string | null }>;
export { ProfRequestMatch };