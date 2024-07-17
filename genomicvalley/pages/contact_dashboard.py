import reflex as rx

from genomicvalley.components.contact_entries import contact_entries
from genomicvalley.components.drawer import drawer
from genomicvalley.components.dashboard_navbar import dashboard_navbar
from genomicvalley.state import require_login, LocalAuthState, ContactDatabase


@rx.page(
    route="/contact_dashboard",
    title="Contact Dashboard",
    on_load=ContactDatabase.get_entries,
)
@require_login
def contact_dashboard():
    return rx.vstack(dashboard_navbar(), drawer(), contact_entries())
