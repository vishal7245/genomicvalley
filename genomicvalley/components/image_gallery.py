import reflex as rx


from reflex.vars import Var
from typing import Any
from reflex.utils import imports


class Carousel(rx.Component):
    """Carousel component."""

    library = "react-responsive-carousel"
    tag = "Carousel"

    dynamicHeight: bool = False  # Changed to False to maintain fixed height
    showThumbs: bool = False
    centerMode: bool = False
    infiniteLoop: bool = True
    autoPlay: bool = True
    interval: int = 3000
    swipeable: bool = True
    emulateTouch: bool = True
    showStatus: bool = False
    showIndicators: bool = False

    # Fixed height
    width: str = "100%"
    height: str = "300px"  # Fixed height, adjust as needed

    def _get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            super()._get_imports(),
            {
                "": {
                    imports.ImportVar(
                        tag="react-responsive-carousel/lib/styles/carousel.min.css"
                    )
                }
            },
        )


carousel = Carousel.create

all_images = [
    "/c5.png",
    "/labimg3.jpg",
    "/c1.png",
    "/c12.png",
    "/labimg9.jpg",
    "/labimg10.jpg",
    "/c11.png",
    "/c6.png",
    "/labimg12.jpg",
    "/c3.png",
    "/labimg4.jpg",
    "/c9.png",
    "/labimg11.jpg",
    "/c15.png",
    "/labimg2.jpg",
    "/c4.png",
    "/labimg13.jpg",
    "/labimg1.jpg",
    "/labimg15.jpg",
    "/c14.png",
    "/labimg5.jpg",
    "/c7.png",
    "/c13.png",
    "/labimg16.jpg",
    "/c2.png",
    "/labimg6.jpg",
    "/labimg14.jpg",
    "/labimg7.jpg",
    "/c10.png",
    "/c8.png",
]


def image_gallery() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "GALLERY",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "A glimpse into our company",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.html(
                        """
                        <style>
                            .carousel {
                                position: relative;
                                width: 100%;
                                overflow: hidden;
                            }

                            .carousel-track {
                                display: flex;
                                animation: scroll 30s linear infinite;
                            }

                            .carousel-slide {
                                flex: 0 0 auto;
                                height: 400px;
                                box-sizing: border-box;
                                margin: 2px;
                            }

                            .carousel-slide img {
                                width: 100%;
                                height: 100%;
                                object-fit: cover;
                            }

                            @keyframes scroll {
                                from { transform: translateX(0); }
                                to { transform: translateX(-100%); }
                            }

                            .carousel-track:hover {
                                animation-play-state: paused;
                            }
                        </style>
                        <div class="carousel">
                            <div class="carousel-track">
                                <div class="carousel-slide"><img src="/c5.png" alt="Image 5"></div>
                                <div class="carousel-slide"><img src="/labimg3.jpg" alt="Lab Image 3"></div>
                                <div class="carousel-slide"><img src="/c1.png" alt="Image 1"></div>
                                <div class="carousel-slide"><img src="/c12.png" alt="Image 4"></div>
                                <div class="carousel-slide"><img src="/labimg9.jpg" alt="Lab Image 9"></div>
                                <div class="carousel-slide"><img src="/labimg10.jpg" alt="Lab Image 10"></div>
                                <div class="carousel-slide"><img src="/c11.png" alt="Image 3"></div>
                                <div class="carousel-slide"><img src="/c6.png" alt="Image 6"></div>
                                <div class="carousel-slide"><img src="/labimg12.jpg" alt="Lab Image 12"></div>
                                <div class="carousel-slide"><img src="/c3.png" alt="Image 3"></div>
                                <div class="carousel-slide"><img src="/labimg4.jpg" alt="Lab Image 4"></div>
                                <div class="carousel-slide"><img src="/c9.png" alt="Image 1"></div>
                                <div class="carousel-slide"><img src="/labimg11.jpg" alt="Lab Image 11"></div>
                                <div class="carousel-slide"><img src="/c15.png" alt="Image 7"></div>
                                <div class="carousel-slide"><img src="/labimg2.jpg" alt="Lab Image 2"></div>
                                <div class="carousel-slide"><img src="/c4.png" alt="Image 4"></div>
                                <div class="carousel-slide"><img src="/labimg13.jpg" alt="Lab Image 13"></div>
                                <div class="carousel-slide"><img src="/labimg1.jpg" alt="Lab Image 1"></div>
                                <div class="carousel-slide"><img src="/labimg15.jpg" alt="Lab Image 15"></div>
                                <div class="carousel-slide"><img src="/c14.png" alt="Image 6"></div>
                                <div class="carousel-slide"><img src="/labimg5.jpg" alt="Lab Image 5"></div>
                                <div class="carousel-slide"><img src="/c7.png" alt="Image 7"></div>
                                <div class="carousel-slide"><img src="/c13.png" alt="Image 5"></div>
                                <div class="carousel-slide"><img src="/labimg16.jpg" alt="Lab Image 16"></div>
                                <div class="carousel-slide"><img src="/c2.png" alt="Image 2"></div>
                                <div class="carousel-slide"><img src="/labimg6.jpg" alt="Lab Image 6"></div>
                                <div class="carousel-slide"><img src="/labimg14.jpg" alt="Lab Image 14"></div>
                                <div class="carousel-slide"><img src="/labimg7.jpg" alt="Lab Image 7"></div>
                                <div class="carousel-slide"><img src="/c10.png" alt="Image 2"></div>
                                <div class="carousel-slide"><img src="/c8.png" alt="Image 8"></div>
                            </div>
                        </div>
                        <script>
                            document.addEventListener('DOMContentLoaded', () => {
                                const track = document.querySelector('.carousel-track');
                                const slides = Array.from(track.children);
                                let currentIndex = 0;

                                function moveToNextSlide() {
                                    if (currentIndex >= slides.length - 1) {
                                        currentIndex = -1;
                                    }
                                    currentIndex++;
                                    const amountToMove = slides[currentIndex].offsetWidth;
                                    track.style.transform = `translateX(-${currentIndex * amountToMove}px)`;
                                }

                                setInterval(moveToNextSlide, 3000);
                            });
                        </script>
                        """
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "GALLERY",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                        align="center",
                    ),
                    width="100%",
                ),
                rx.heading(
                    "A glimpse into our company",
                    size="6",
                    weight="medium",
                    color="black",
                    margin_bottom="10px",
                    align="center",
                ),
                rx.box(
                    carousel(
                        *[
                            rx.image(
                                src=image_src,
                                width="100%",
                                height="300px",
                                object_fit="contain",
                                background_color="black",
                            )
                            for image_src in all_images
                        ],
                    ),
                    width="100%",
                    max_width="100vw",
                    height="300px",
                    overflow="hidden",
                    position="relative",
                    padding="0.5em",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding="0.5em",
            )
        ),
    )
