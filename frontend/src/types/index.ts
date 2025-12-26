export interface WordData {
  word: string;
  weight: number;
}

export interface APIResponse {
  words: WordData[];
  article_length: number;
  status: string;
}