import reflex as rx # type: ignore


font_style = {
    "color": "#565957",
}


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", style=font_style), href=url
    )

def blur_background():
    return rx.fragment(
        rx.script(
            """
            window.onscroll = function() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                var scrollThreshold = 100;
                var navbar = document.getElementById('navbar');
                if (!navbar) {
                    return;
                }

                if (scrollTop > scrollThreshold) {
                    navbar.classList.add('blur-navbar');
                } else {
                    navbar.classList.remove('blur-navbar');
                }
            };
            """
        ),
        rx.html(
            """
            <style>
            .blur-navbar {
                border: 1px solid rgba(29, 29, 32, 0.08);
                background: HSLA(147,100%,50%,0.1);
                box-shadow: 0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;
                backdrop-filter: blur(20px);
            }
            </style>
            """
        ),
    )

def redirect(url):
    return rx.redirect(url)


def navbar_white() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(rx.image(src="/logo1.png", alt="Genomic Valley", max_height="100px"), href="/"),
                    align_items="center",
                    margin_left="1em",
                    margin_top="1em",
                    max_height="40px",
                    margin_bottom="1em",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About Us", "/about"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text(
                                    "Services",
                                    size="4",
                                    weight="medium",
                                    style = font_style,
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                                color = "green",
                                _hover = {
                                    "background": "#93f599"
                                },
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Diagnostic Services", on_click=lambda: redirect("/diagnostic-services")),
                            rx.menu.item("Research Services", on_click=lambda: redirect("/research-services")),
                        )
                    ),
                    rx.link(
                        rx.button(
                                rx.text(
                                    "Contact",
                                    size="4",
                                    weight="medium",
                                    style = font_style,
                                ),
                                weight="medium",
                                variant="ghost",
                                size="4",
                                _hover = {
                                    "background": "#93f599"
                                },
                            ),
                        href="/contact"
                        ),
                    justify="end",
                    spacing="5",
                    margin_right="2em",
                    margin_top="1.3em",
                ),
                justify="between",
            ),
        ),
        blur_background(),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30, color="black")
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=lambda: redirect("/")),
                        rx.menu.item("About Us", on_click=lambda: redirect("/about")),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Services"),
                            rx.menu.sub_content(
                                rx.menu.item("Diagnostic Services", on_click=lambda: redirect("/diagnostic-services")),
                                rx.menu.item("Research Services", on_click=lambda: redirect("/research-services")),
                            ),
                        ),
                        rx.menu.item("Contact", on_click=lambda: redirect("/contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        id="navbar",
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )