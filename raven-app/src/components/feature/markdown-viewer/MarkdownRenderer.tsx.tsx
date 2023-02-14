import React from 'react';
import { useRemarkSync, UseRemarkSyncOptions } from 'react-remark';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';


interface Props {
  content: string;
}

export const MarkdownRenderer: React.FC<Props> = ({ content }) => {
  return useRemarkSync(content, {
    remarkToRehypeOptions: { allowDangerousHtml: true },
    rehypePlugins: [rehypeRaw, rehypeSanitize] as UseRemarkSyncOptions['rehypePlugins'],
  })
}