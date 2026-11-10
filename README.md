# BrowserSolver for Hermes Agent

Fetch web pages behind Cloudflare, DataDome and similar protections for the built-in web_extract tool, through the BrowserSolver web unlocker API.

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

## Settings

| Setting | Default | Meaning |
|---|---|---|
| `engine` | `webunlocker` | `crawler` (plain HTTP, cheapest), `rendering` (headless browser for JavaScript pages) or `webunlocker` (gets past anti-bot protection, most expensive). |

## What it does on your machine

- **Network:** calls `https://api.browsersolver.com` only, with your `BROWSERSOLVER_API_KEY`. Calls can use credits on your BrowserSolver account ([pricing](https://www.browsersolver.com/pricing)).
- **Credentials:** reads the key only through Hermes's secret scope. It stores nothing.
- **Nothing else:** no files written, no processes started, no telemetry, no self-update. Standard library only, no dependencies.

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
