declare function MatchCompOffer(
    offerId: number,
    compOfferId: number,
    authToken: string): Promise<{text: boolean | null }>;
export { MatchCompOffer };