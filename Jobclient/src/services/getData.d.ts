type Data = {
    [key: string]: string;
  };

declare function getData(authToken: string | null, apiUrl: string): Promise<Any| null>;

export { getData };