type Data = {
    [key: string]: string;
  };

declare function getData(authToken: string | null, apiUrl: string): Promise<Data | null>;

export { getData };