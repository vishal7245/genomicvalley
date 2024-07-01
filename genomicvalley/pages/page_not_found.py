import reflex as rx
from genomicvalley.components.navbar import navbar
from genomicvalley.components.footer import footer

hero_style = {
    "width": "100%",
    "height": "90vh",
    "backgroundImage": "url('/not-found.jpg')",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
}

class State(rx.State):
    @rx.var
    def not_found_path(self) -> str:
        return "/".join(self.router.page.params.get("path", []))

@rx.page(route="/[...path]")
def page_not_found():
    return rx.vstack(
        navbar(),
        rx.box(style=hero_style),
        rx.text(f"404 - Page Not Found: /{State.not_found_path}"),
        footer(),
    )