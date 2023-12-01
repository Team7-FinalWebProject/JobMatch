type Data = {
    [key: string]: string;
  };

declare function getAvatar(authToken: string | null, professional: string): Promise<Data | null>;

export { getAvatar };