import reflex as rx
from genomicvalley.components.navbar_2 import navbar_white as navbar
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
        rx.html(
        """
                <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-7C0KZ36E1J"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-7C0KZ36E1J');
        </script>
        """    
        ),
        navbar(),
        rx.box(style=hero_style),
        rx.text(f"404 - Page Not Found: /{State.not_found_path}"),
        footer(),
    )