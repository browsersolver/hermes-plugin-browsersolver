# BrowserSolver for Hermes Agent

Read web pages that block bots, from [Hermes Agent](https://hermes-agent.nousresearch.com), through the [BrowserSolver](https://www.browsersolver.com) web unlocker API.

Many shops, marketplaces and travel sites answer automated requests with a challenge page from Cloudflare, DataDome, Akamai or PerimeterX instead of their content. With BrowserSolver as the backend of Hermes's built-in `web_extract` tool, Hermes gets the real page and reads its text.

## Contents

- [Install](#install)
- [How it works](#how-it-works)
- [Engines](#engines)
- [Settings](#settings)
- [Example prompts](#example-prompts)
- [Credits and errors](#credits-and-errors)
- [What it does on your machine](#what-it-does-on-your-machine)

## Install

```sh
hermes plugins install browsersolver
```

Hermes asks for `BROWSERSOLVER_API_KEY` during the install. Create a key in the [BrowserSolver dashboard](https://app.browsersolver.com).

Then select it in `hermes tools`, or in `~/.hermes/config.yaml`:

```yaml
web:
  extract_backend: browsersolver
```

It is extract only, so keep a search backend for `web_search`.

## How it works

When the model calls `web_extract` with one or more URLs, the plugin sends each one to `https://api.browsersolver.com`. BrowserSolver loads the page with the engine you chose, gets past the bot challenge when there is one, and returns the HTML. The plugin turns it into readable text (title, headings, paragraphs and lists; scripts, styles and markup removed) and hands it back to Hermes, one document per URL.

```
Hermes web_extract  ──URL──▶  plugin  ──GET /v1/website/<engine>──▶  api.browsersolver.com  ──▶  site
                    ◀──text──         ◀──HTML────────────────────
```

Each document also keeps the raw HTML (`raw_content`) and records which engine fetched it. A URL that fails returns its own error without stopping the others.

## Engines

| Engine | How it loads the page | Good for | Credits |
|---|---|---|---|
| `webunlocker` (default) | BrowserSolver's highest tier: solves the bot challenges that still block a headless browser. | Shops, marketplaces and other sites behind Cloudflare, DataDome, Akamai or PerimeterX. The site's domain must be on your BrowserSolver whitelist. | 3 |
| `rendering` | A headless browser that runs the page's JavaScript before returning the HTML. | Single-page apps and content that loads after the first paint, on sites without a bot wall. | 2 |
| `crawler` | A plain HTTP request, no browser. | Static and server-rendered pages. The fastest and cheapest. | 1 |

The default is `webunlocker` because that is what BrowserSolver is for. If most of the pages you read are not protected, set `crawler` or `rendering` to spend fewer credits, and keep `webunlocker` for the sites that need it.

To get a domain added to your whitelist, ask BrowserSolver support.

## Settings

| Setting | Default | Meaning |
|---|---|---|
| `engine` | `webunlocker` | `webunlocker`, `rendering` or `crawler`, as above. It applies to every `web_extract` call. |

Set it in the plugin's settings form (Plugins tab of the Hermes desktop app), or in `~/.hermes/config.yaml`:

```yaml
plugins:
  entries:
    browsersolver:
      settings:
        engine: crawler
```

## Example prompts

With BrowserSolver selected as the extract backend, Hermes uses it whenever it reads a page:

- "Read this product page and give me the price, the delivery date and the return policy: https://…"
- "Compare the specifications on these three product pages."
- "Summarize the reviews shown on this page."
- "What does this page say about the cancellation policy?"

## Credits and errors

- Each URL fetched uses the engine's credits: 3 for `webunlocker`, 2 for `rendering`, 1 for `crawler`. Plans and prices: [browsersolver.com/pricing](https://www.browsersolver.com/pricing).
- A failed URL comes back with `error: "BrowserSolver: <message>"` and the API's own message (invalid key, no credits left, domain not on the whitelist, page not reachable), so the model can explain it or try another page.
- Calls time out after 120 seconds.

## What it does on your machine

- **Network:** calls `https://api.browsersolver.com` only, with your `BROWSERSOLVER_API_KEY`. Calls use credits on your BrowserSolver account.
- **Credentials:** reads the key only through Hermes's secret scope. It stores nothing.
- **Nothing else:** no files written, no processes started, no telemetry, no self-update. Standard library only, no dependencies.

Read only pages you are allowed to access, and respect each site's terms.

## Development

```sh
python -m pytest
```

The tests mock the network and run without Hermes installed.

## Contact

- Source: https://github.com/browsersolver/hermes-plugin-browsersolver
- BrowserSolver: https://www.browsersolver.com
- Issues: https://github.com/browsersolver/hermes-plugin-browsersolver/issues

## License

MIT
