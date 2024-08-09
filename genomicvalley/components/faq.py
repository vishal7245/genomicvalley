import reflex as rx

# Update the accordion_style dictionary
accordion_style = {
    "color": "#000000",  # Change this to your desired color
}

def accordion_faq()-> rx.Component:
    return rx.section(
        rx.html("""
               <style>
                .accordion {
                    max-width: 60vw;
                    margin: 0 auto;
                    background-color: #fff;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                }

                .accordion-item {
                    border-top: 1px solid #ddd;
                }

                .accordion-item:first-child {
                    border-top: none;
                }

                .accordion-header {
                    background-color: #fff;
                    cursor: pointer;
                    padding: 15px 20px;
                    color: black;
                    width: 100%;
                    text-align: left;
                    border: none;
                    outline: none;
                    font-size: 16px;
                    transition: background-color 0.3s ease;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-weight: bold;
                }

                .accordion-header:hover {
                    background-color: rgba(39,162,85,0.2);;
                }

                .accordion-header:after {
                    content: '+';
                    font-size: 20px;
                    transition: transform 0.3s ease;
                    font-weight: bold;
                }

                .accordion-header.active:after {
                    transform: rotate(45deg);
                }

                .accordion-content {
                    max-height: 0;
                    overflow: hidden;
                    padding: 0 20px;
                    border-top: 1px solid #ddd;
                    background-color: #fff;
                    transition: max-height 0.3s ease, padding 0.3s ease;
                }

                .accordion-content p {
                    margin-bottom: 30px;
                    padding: 15px 0;
                    color: black;
                }
            </style>

            <div class="accordion">
                <div class="accordion-item">
                    <button class="accordion-header">What are the primary diagnostic services offered by Genomic Valley Bharat Pvt. Ltd.?</button>
                    <div class="accordion-content">
                        <p>We specialize in Next-Generation Sequencing (NGS)-based molecular diagnostics, focusing on identifying genetic mutations and abnormalities with advanced AI integration. Our services enable early detection and personalized treatment plans, particularly in oncology.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">What are the key components of your personalized healthcare services?</button>
                    <div class="accordion-content">
                        <p>Our personalized healthcare utilizes NGS and AI technologies to tailor medical treatments based on individual genetic profiles. This approach enhances therapy effectiveness, minimizes adverse effects, and ensures tailored care aligned with each patient's genetic makeup.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">Could you explain your genetic disease predisposition services?</button>
                    <div class="accordion-content">
                        <p>We offer genetic disease predisposition analysis using NGS to predict susceptibility to hereditary conditions along with pharmacogenomics for recommendation of patient-centred drugs. This service supports proactive healthcare measures and informed decision-making for patients and healthcare providers.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">How does Genomic Valley Bharat Pvt. Ltd. support community health through genomic initiatives?</button>
                    <div class="accordion-content">
                        <p>We envision to integrate AI into NGS to conduct population-wide genetic screening aimed at improving public health outcomes. Our initiatives will help identify prevalent health risks and design targeted community health programs for disease prevention and management.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">How does Genomic Valley Bharat Pvt. Ltd. contribute to oncology research?</button>
                    <div class="accordion-content">
                        <p>We leverage over a decade of experience in NGS and AI to pioneer advancements in cancer research. Our focus includes uncovering novel biomarkers and genetic insights, collaborating with leading institutions to develop more effective diagnostic tools and therapeutic strategies.</p>
                    </div>
                </div>
            </div>     

            <script>
                document.addEventListener("DOMContentLoaded", function() {
                    var accordionHeaders = document.querySelectorAll(".accordion-header");

                    accordionHeaders.forEach(function(header) {
                        header.addEventListener("click", function() {
                            var content = this.nextElementSibling;

                            if (content.style.maxHeight) {
                                content.style.maxHeight = null;
                                content.style.paddingTop = null;
                                content.style.paddingBottom = null;
                                this.classList.remove("active");
                            } else {
                                // Close all other sections
                                var allContents = document.querySelectorAll(".accordion-content");
                                var allHeaders = document.querySelectorAll(".accordion-header");
                                allContents.forEach(function(item) {
                                    item.style.maxHeight = null;
                                    item.style.paddingTop = null;
                                    item.style.paddingBottom = null;
                                });
                                allHeaders.forEach(function(item) {
                                    item.classList.remove("active");
                                });

                                // Open the clicked section
                                content.style.maxHeight = content.scrollHeight + "px";
                                content.style.paddingTop = "15px";
                                content.style.paddingBottom = "15px";
                                this.classList.add("active");
                            }
                        });
                    });
                });
            </script>


                """),
        width="100%",
        justify_content="center",
        align_items="center",
    )
    
def mobile_accordion_faq()-> rx.Component:
    return rx.section(
        rx.html("""
               <style>
                .accordion {
                    max-width: 90vw;
                    margin: 0 auto;
                    background-color: #fff;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                }

                .accordion-item {
                    border-top: 1px solid #ddd;
                }

                .accordion-item:first-child {
                    border-top: none;
                }

                .accordion-header {
                    background-color: #fff;
                    cursor: pointer;
                    padding: 15px 20px;
                    color: black;
                    width: 100%;
                    text-align: left;
                    border: none;
                    outline: none;
                    font-size: 16px;
                    transition: background-color 0.3s ease;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-weight: bold;
                }

                .accordion-header:hover {
                    background-color: rgba(39,162,85,0.2);;
                }

                .accordion-header:after {
                    content: '+';
                    font-size: 20px;
                    transition: transform 0.3s ease;
                    font-weight: bold;
                }

                .accordion-header.active:after {
                    transform: rotate(45deg);
                }

                .accordion-content {
                    max-height: 0;
                    overflow: hidden;
                    padding: 0 20px;
                    border-top: 1px solid #ddd;
                    background-color: #fff;
                    transition: max-height 0.3s ease, padding 0.3s ease;
                }

                .accordion-content p {
                    margin-bottom: 30px;
                    padding: 15px 0;
                    color: black;
                }
            </style>

            <div class="accordion">
                <div class="accordion-item">
                    <button class="accordion-header">What are the primary diagnostic services offered by Genomic Valley Bharat Pvt. Ltd.?</button>
                    <div class="accordion-content">
                        <p>We specialize in Next-Generation Sequencing (NGS)-based molecular diagnostics, focusing on identifying genetic mutations and abnormalities with advanced AI integration. Our services enable early detection and personalized treatment plans, particularly in oncology.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">What are the key components of your personalized healthcare services?</button>
                    <div class="accordion-content">
                        <p>Our personalized healthcare utilizes NGS and AI technologies to tailor medical treatments based on individual genetic profiles. This approach enhances therapy effectiveness, minimizes adverse effects, and ensures tailored care aligned with each patient's genetic makeup.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">Could you explain your genetic disease predisposition services?</button>
                    <div class="accordion-content">
                        <p>We offer genetic disease predisposition analysis using NGS to predict susceptibility to hereditary conditions along with pharmacogenomics for recommendation of patient-centred drugs. This service supports proactive healthcare measures and informed decision-making for patients and healthcare providers.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">How does Genomic Valley Bharat Pvt. Ltd. support community health through genomic initiatives?</button>
                    <div class="accordion-content">
                        <p>We envision to integrate AI into NGS to conduct population-wide genetic screening aimed at improving public health outcomes. Our initiatives will help identify prevalent health risks and design targeted community health programs for disease prevention and management.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <button class="accordion-header">How does Genomic Valley Bharat Pvt. Ltd. contribute to oncology research?</button>
                    <div class="accordion-content">
                        <p>We leverage over a decade of experience in NGS and AI to pioneer advancements in cancer research. Our focus includes uncovering novel biomarkers and genetic insights, collaborating with leading institutions to develop more effective diagnostic tools and therapeutic strategies.</p>
                    </div>
                </div>
            </div>     

            <script>
                document.addEventListener("DOMContentLoaded", function() {
                    var accordionHeaders = document.querySelectorAll(".accordion-header");

                    accordionHeaders.forEach(function(header) {
                        header.addEventListener("click", function() {
                            var content = this.nextElementSibling;

                            if (content.style.maxHeight) {
                                content.style.maxHeight = null;
                                content.style.paddingTop = null;
                                content.style.paddingBottom = null;
                                this.classList.remove("active");
                            } else {
                                // Close all other sections
                                var allContents = document.querySelectorAll(".accordion-content");
                                var allHeaders = document.querySelectorAll(".accordion-header");
                                allContents.forEach(function(item) {
                                    item.style.maxHeight = null;
                                    item.style.paddingTop = null;
                                    item.style.paddingBottom = null;
                                });
                                allHeaders.forEach(function(item) {
                                    item.classList.remove("active");
                                });

                                // Open the clicked section
                                content.style.maxHeight = content.scrollHeight + "px";
                                content.style.paddingTop = "15px";
                                content.style.paddingBottom = "15px";
                                this.classList.add("active");
                            }
                        });
                    });
                });
            </script>


                """),
        width="100%",
        justify_content="center",
        align_items="center",
    )


def faq_section() -> rx.Component:
    return rx.section(
                rx.section(
                    rx.vstack(
                        rx.heading("FAQ", size="5", weight="bold", margin_bottom="1em", color="green", align="center", id="faq"),
                        rx.heading("Frequently Asked Questions", size="8", weight="medium", color="black", margin_bottom="10px", align="center"),
                        rx.text(
                            "For any other questions, please feel free to contact us.",
                            size="5", align="center", margin_bottom="1em", color="gray", padding="10px"
                        ),
                        accordion_faq(),
                        justify_content="center",
                        align_items="center",
                        width="100%",
                    ),
                    width="100%",
                ),
            
        width="100%",
    )