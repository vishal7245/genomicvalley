import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar import navbar
from genomicvalley.components.banner import banner
from genomicvalley.components.investor_content import investor_content



@rx.page()
def investor_relation(route="/investor-relations", title="Investor Relations"):
    return rx.vstack(
        navbar(),
        banner("Investor Relations"),
        investor_content(),
        footer(),
    )





    