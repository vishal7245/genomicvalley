import reflex as rx

def image_gallery() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading("GALLERY", size="5", weight="bold", margin_bottom="1em", color="green"),
                    rx.heading("A glimpse into our company", size="8", weight="medium", color="black", margin_bottom="10px"),
                    rx.html(
                        """
                        <style>
                            .carousel {
                                position: relative;
                                width: 100vw;
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
                                <div class="carousel-slide"><img src="/c1.png" alt="Image 1"></div>
                                <div class="carousel-slide"><img src="/c2.png" alt="Image 2"></div>
                                <div class="carousel-slide"><img src="/c3.png" alt="Image 3"></div>
                                <div class="carousel-slide"><img src="/c4.png" alt="Image 4"></div>
                                <div class="carousel-slide"><img src="/c5.png" alt="Image 5"></div>
                                <div class="carousel-slide"><img src="/c6.png" alt="Image 6"></div>
                                <div class="carousel-slide"><img src="/c7.png" alt="Image 7"></div>
                                <div class="carousel-slide"><img src="/c8.png" alt="Image 8"></div>
                                <div class="carousel-slide"><img src="/c9.png" alt="Image 1"></div>
                                <div class="carousel-slide"><img src="/c10.png" alt="Image 2"></div>
                                <div class="carousel-slide"><img src="/c11.png" alt="Image 3"></div>
                                <div class="carousel-slide"><img src="/c12.png" alt="Image 4"></div>
                                <div class="carousel-slide"><img src="/c13.png" alt="Image 5"></div>
                                <div class="carousel-slide"><img src="/c14.png" alt="Image 6"></div>
                                <div class="carousel-slide"><img src="/c15.png" alt="Image 7"></div>
                                <div class="carousel-slide"><img src="/c16.png" alt="Image 8"></div>
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
    )