import reflex as rx

from genomicvalley.components.contact_entries import contact_entries
from genomicvalley.components.drawer import drawer
from genomicvalley.components.dashboard_navbar import dashboard_navbar
from genomicvalley.state import require_login, VisitorStats
from genomicvalley.components.visiting_basic_stats import visiting_basic_stats


@rx.page(
    route="/dashboard", title="Dashboard", on_load=VisitorStats.get_visitor_entries
)
@require_login
def dashboard():
    return rx.vstack(dashboard_navbar(), drawer(), visiting_basic_stats())
