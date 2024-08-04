from os import name
import reflex as rx


class CareerFormState(rx.State):
    form_data: dict = {}
    resume: str

    wet_lab_choices: dict[str, bool] = {
        k: False
        for k in [
            "DNA/RNA extraction",
            "PCR and qPCR",
            "Gel electrophoresis",
            "Cell culture techniques",
            "Flow cytometry",
            "CRISPR/Cas9 genome editing",
            "Microscopy (confocal, electron)",
            "Protein purification and analysis",
            "Western blotting",
            "Immunohistochemistry",
            "In situ hybridization",
            "NGS Library Preparation",
            "Whole Genome Sequencing",
            "Whole Transcriptome",
            "mRNA Sequencing",
            "Methylome",
            "miRNA Sequencing",
            "Targeted Panels (DNA/RNA)",
            "Exome Sequencing",
            "16S/ITS panel sequencing",
            "Amplicon Sequencing",
            "Cloning",
            "Sanger Sequencing",
            "Others",
        ]
    }

    dry_lab_choices: dict[str, bool] = {
        k: False
        for k in [
            "Machine learning and AI algorithms",
            "Data mining and big data analytics",
            "Statistical analysis",
            "Genomic data visualization",
            "Structural bioinformatics",
            "Systems biology modeling",
            "Molecular docking simulations",
            "High-performance computing (HPC)",
            "Database management",
            "Cloud computing",
            "NGS data analysis",
            "Data QC",
            "WGS analysis",
            "WES analysis",
            "Alignment and mapping",
            "Variant calling",
            "CNV identification",
            "Transcriptome analysis",
            "Transcriptome Mapping",
            "Differential Expression",
            "Volcano Plots",
            "PCA-Analysis",
            "Venn-Diagram",
            "HeatMap",
            "Enrichment-Analysis: Molecular Function",
            "Enrichment-Analysis: Biological Processes",
            "Enrichment-Analysis: Disease association",
            "Enrichment-Analysis: Pathway analysis",
            "Methylome analysis",
            "16s/ITS analysis",
            "Data QC",
            "OTU Clustering (Genus and Species level)",
            "Alpha and Beta diversity",
            "Targeted Panel Analysis",
            "Others",
        ]
    }

    sales_and_marketing_choices: dict[str, bool] = {
        k: False
        for k in [
            "Market research and analysis",
            "Digital marketing strategies",
            "Content creation and management",
            "Social media marketing",
            "Customer relationship management (CRM)",
            "Technical sales and product demonstrations",
            "Negotiation and closing deals",
            "Event planning and trade show coordination",
            "Lead generation and conversion",
            "Brand development and positioning",
            "Others",
        ]
    }

    def check_wet_lab_choice(self, value, index):
        self.wet_lab_choices[index] = value

    def check_dry_lab_choice(self, value, index):
        self.dry_lab_choices[index] = value

    def sales_and_marketing_choice(self, value, index):
        self.sales_and_marketing_choices[index] = value

    @rx.var
    def wet_lab_checked_choices(self):
        choices = [l for l, v in self.wet_lab_choices.items() if v]
        return choices

    @rx.var
    def dry_lab_checked_choices(self):
        choices = [l for l, v in self.dry_lab_choices.items() if v]
        return choices

    @rx.var
    def sales_and_marketing_checked_choices(self):
        choices = [l for l, v in self.sales_and_marketing_choices.items() if v]
        return choices

    def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        self.form_data["resume"] = self.resume
        print(form_data)

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).
        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            self.resume = file.filename


def render_checkboxes(values, handler):
    return rx.grid(
        rx.foreach(
            values,
            lambda choice: rx.checkbox(
                rx.text(choice[0], color="black"),
                checked=choice[1],
                color_scheme="green",
                label_color="black",
                variant="soft",
                on_change=lambda val: handler(val, choice[0]),
                style={"color": "black"},
            ),
        ),
        columns="3",
        spacing="4",
        width="100%",
    )


def form_field(
    label: str, placeholder: str, type: str, name: str, required: bool = True
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label, color="black"),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    bg="rgba(39,162,85,0.2)",
                    color="black",
                    style={"& input::placeholder": {"color": "gray"}},
                    required=required,
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def text_area_field(label: str, placeholder: str, name: str) -> rx.Component:
    return (
        rx.flex(
            rx.text(
                label,
                style={
                    "font-size": "15px",
                    "font-weight": "500",
                    "line-height": "35px",
                    "color": "black",
                },
            ),
            rx.text_area(
                placeholder=placeholder,
                name=name,
                resize="vertical",
                bg="rgba(39,162,85,0.2)",
                color="black",
                style={"& text_area::placeholder": {"color": "gray"}},
            ),
            direction="column",
            spacing="1",
        ),
    )


color = "rgb(107,99,246)"


def upload_form():
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File", color=color, bg="white", border=f"1px solid {color}"
                ),
                rx.text(
                    "Drag and drop your resume here or click to select files",
                    color="black",
                ),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
            style={"background_color": "rgba(39,162,85,0.2)"},
            width="100%",
        ),
        rx.hstack(rx.foreach(rx.selected_files("upload1"), rx.text)),
        rx.hstack(
            rx.button(
                "Upload",
                color_scheme="green",
                on_click=CareerFormState.handle_upload(
                    rx.upload_files(upload_id="upload1")
                ),
            ),
            rx.button(
                "Clear",
                color_scheme="green",
                on_click=rx.clear_selected_files("upload1"),
            ),
        ),
        padding="1em",
        width="100%",
    )


def career_form() -> rx.Component:
    return rx.section(
        rx.card(
            rx.vstack(
                rx.heading(
                    "Section A: Upload Resume",
                    size="5",
                    color="black",
                    margin_bottom="20px",
                ),
                upload_form(),
                rx.form.root(
                    rx.heading(
                        "Section B: Personal Information", size="5", color="black"
                    ),
                    rx.hstack(
                        form_field(
                            label="First Name",
                            placeholder="First Name",
                            type="text",
                            name="full_name",
                        ),
                        form_field(
                            label="Last Name",
                            placeholder="Last Name",
                            type="text",
                            name="last_name",
                        ),
                    ),
                    rx.hstack(
                        form_field(
                            label="Email",
                            placeholder="employee@mail.com",
                            type="text",
                            name="email",
                        ),
                        form_field(
                            label="Phone",
                            placeholder="+91 XXXXX XXXXX",
                            type="tel",
                            name="phone",
                        ),
                    ),
                    rx.heading("Address:", size="3", color="black", margin_top="2"),
                    rx.hstack(
                        form_field(
                            label="Street Address",
                            placeholder="House XY/23",
                            type="text",
                            name="street_address",
                        ),
                        form_field(
                            label="Landmark",
                            placeholder="Near XYZ",
                            type="text",
                            name="landmark",
                        ),
                    ),
                    rx.hstack(
                        form_field(
                            label="City", placeholder="City", type="text", name="city"
                        ),
                        form_field(
                            label="Postal Code",
                            placeholder="XXX XXX",
                            type="int",
                            name="postal_code",
                        ),
                    ),
                    rx.hstack(
                        form_field(
                            label="State/Province",
                            placeholder="State/Province",
                            type="text",
                            name="state",
                        ),
                        form_field(
                            label="Country",
                            placeholder="Country",
                            type="text",
                            name="country",
                        ),
                    ),
                    rx.heading(
                        "Section C: Position Details",
                        size="5",
                        color="black",
                        margin_top="20px",
                    ),
                    form_field(
                        label="Position Applied For:",
                        placeholder="Position",
                        type="text",
                        name="applied_position",
                    ),
                    rx.text(
                        "Department:", color="black", size="2", margin_bottom="10px"
                    ),
                    rx.radio(
                        [
                            "Personalized Healthcare",
                            "Genetic Disease Predisposition",
                            "Community Health Support",
                            "AI-Based Genome Healthcare",
                            "Metagenomics and Healthcare",
                            "Extramural Research Project",
                            "Others",
                        ],
                        name="department",
                        required=True,
                        color_scheme="green",
                        variant="soft",
                        color="black",
                    ),
                    rx.heading(
                        "Section D: Education ",
                        size="5",
                        color="black",
                        margin_top="20px",
                    ),
                    rx.text(
                        "Highest level of Education:",
                        color="black",
                        size="2",
                        margin_bottom="10px",
                    ),
                    rx.radio(
                        [
                            "High School Diploma",
                            "Associate Degree",
                            "Bachelor's Degree",
                            "Master's Degree",
                            "Doctoral Degree",
                            "Others",
                        ],
                        name="highest_education",
                        required=True,
                        color_scheme="green",
                        variant="soft",
                        color="black",
                    ),
                    form_field(
                        label="University/College Name",
                        placeholder="University/College Name",
                        type="text",
                        name="college",
                        required=True,
                    ),
                    rx.hstack(
                        form_field(
                            label="Field of Study",
                            placeholder="Field of Study",
                            type="text",
                            name="field_of_study",
                            required=True,
                        ),
                        form_field(
                            label="Year of Graduation",
                            placeholder="20XX",
                            type="int",
                            name="graduation_year",
                            required=True,
                        ),
                    ),
                    rx.heading(
                        "Section E: Employment History ",
                        size="5",
                        color="black",
                        margin_top="20px",
                    ),
                    rx.hstack(
                        form_field(
                            label="Current/Most Recent Job Title",
                            placeholder="Current/Recent Job Title",
                            type="text",
                            name="recent_job",
                            required=True,
                        ),
                        form_field(
                            label="Company Name",
                            placeholder="Past Compant Name",
                            type="text",
                            name="past_company",
                            required=True,
                        ),
                    ),
                    rx.hstack(
                        form_field(
                            label="Start Date",
                            placeholder="DD/MM/YYYY",
                            type="str",
                            name="start_date",
                            required=True,
                        ),
                        form_field(
                            label="End Date",
                            placeholder="DD/MM/YYYY",
                            type="str",
                            name="end_date",
                            required=True,
                        ),
                    ),
                    text_area_field(
                        label="Responsibilities and Achievements",
                        placeholder="Responsibilities and Achievements",
                        name="responsibilities_and_achievements",
                    ),
                    rx.heading(
                        "Section F: Skills",
                        size="5",
                        color="black",
                        margin_top="20px",
                        margin_bottom="10px",
                    ),
                    rx.text(
                        "Wet lab skills:", color="black", size="2", margin_bottom="10px"
                    ),
                    rx.scroll_area(
                        render_checkboxes(
                            CareerFormState.wet_lab_choices,
                            CareerFormState.check_wet_lab_choice,
                        ),
                        type="always",
                        scrollbars="vertical",
                        style={"height": 200},
                    ),
                    rx.text(
                        "Dry lab skills:",
                        color="black",
                        size="2",
                        margin_bottom="10px",
                        margin_top="30px",
                    ),
                    rx.scroll_area(
                        render_checkboxes(
                            CareerFormState.dry_lab_choices,
                            CareerFormState.check_dry_lab_choice,
                        ),
                        type="always",
                        scrollbars="vertical",
                        style={"height": 200},
                    ),
                    rx.text(
                        "Sales and Marketing skills:",
                        color="black",
                        size="2",
                        margin_bottom="10px",
                        margin_top="30px",
                    ),
                    render_checkboxes(
                        CareerFormState.sales_and_marketing_choices,
                        CareerFormState.sales_and_marketing_choice,
                    ),
                    rx.heading(
                        "Section G: Additional Information",
                        size="5",
                        color="black",
                        margin_top="20px",
                    ),
                    text_area_field(
                        label="Certifications: ",
                        placeholder="Certifications",
                        name="certifications",
                    ),
                    text_area_field(
                        label="Why do you want to work at Genomic Valley Biotech Limited?: ",
                        placeholder="Your Response",
                        name="why_work",
                    ),
                    rx.text(
                        "How did you hear about this position?:",
                        color="black",
                        size="2",
                        margin_bottom="10px",
                        margin_top="10px",
                    ),
                    rx.radio(
                        [
                            "Company Website",
                            "Job Board",
                            "Referral",
                            "Social Media",
                            "Others",
                        ],
                        name="source",
                        required=True,
                        color_scheme="green",
                        variant="soft",
                        color="black",
                    ),
                    rx.heading(
                        "Section H: Declaration",
                        size="5",
                        color="black",
                        margin_top="20px",
                    ),
                    rx.text(
                        " I certify that the information provided in this application is true and complete to the best of my knowledge: ",
                        color="black",
                        size="2",
                    ),
                    rx.form.submit(
                        rx.button(
                            "Submit", color_scheme="green", margin_top="20px", size="4"
                        ),
                        as_child=True,
                    ),
                    on_submit=CareerFormState.handle_form_submit,
                ),
            ),
            width="70%",
        ),
        width="100%",
        display="flex",
        justify_content="center",
        align_items="flex-start",
    )
