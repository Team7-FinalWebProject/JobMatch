declare function MatchProfOffer(
    offerId: number,
    profOfferId: number,
    authToken: string): Promise<{text: boolean | null }>;
export { MatchProfOffer };