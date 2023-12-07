type Data = {
    [key: string]: string;
  };

declare function getImage(authToken: string | null, apiUrl: string): Promise<Any| null>;

export { getImage };