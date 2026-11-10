"""BrowserSolver web extract backend for Hermes Agent."""


def register(ctx):
    from .provider import BrowserSolverWebExtractProvider

    ctx.register_web_search_provider(BrowserSolverWebExtractProvider(ctx))
