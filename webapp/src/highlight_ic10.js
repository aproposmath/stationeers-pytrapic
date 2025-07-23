import ic10 from "./ic10.json";

export default function (hljs) {
  return {
    name: "Stationeers IC10",
    case_insensitive: false,
    aliases: ["ic10"],
    keywords: {
      $pattern: "\\.?" + hljs.IDENT_RE,
      meta: "",
      built_in: ic10.keywords,
    },
    contains: [
      {
        className: "keyword",
        begin:
          "\\b(" + // mnemonics
          ic10.instructions.join("|") +
          ")",
        end: "\\s",
      },
      // lines ending with ; or # aren't really comments, probably auto-detect fail
      hljs.COMMENT("[;#](?!\\s*$)", "$"),
      hljs.C_BLOCK_COMMENT_MODE,
      hljs.QUOTE_STRING_MODE,
      {
        className: "string",
        begin: "'",
        end: "[^\\\\]'",
        relevance: 0,
      },
      {
        className: "title",
        begin: "\\|",
        end: "\\|",
        illegal: "\\n",
        relevance: 0,
      },
      {
        className: "number",
        variants: [
          {
            // hex
            begin: "0x[0-9a-f]+",
          },
          {
            // bare number
            begin: "\\b-?\\d+",
          },
        ],
        relevance: 0,
      },
      {
        className: "symbol",
        variants: [
          {
            // GNU MIPS syntax
            begin: "^\\s*[a-z_\\.\\$][a-z0-9_\\.\\$]+:",
          },
          {
            // numbered local labels
            begin: "^\\s*[0-9]+:",
          },
          {
            // number local label reference (backwards, forwards)
            begin: "[0-9]+[bf]",
          },
        ],
        relevance: 0,
      },
    ],
    // forward slashes are not allowed
    illegal: /\//,
  };
}
