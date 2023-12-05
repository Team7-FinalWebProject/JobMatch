declare function submitSupportRequest(
    content: string): Promise<{text: string | null; audio: string | null}>;
export { submitSupportRequest };