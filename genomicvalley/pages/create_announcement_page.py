from genomicvalley.state import require_login
import reflex as rx

from genomicvalley.components.create_announcement import create_announcement


@rx.page(route="/create_announcement", title="Create Announcement")
@require_login
def create_announcement_page():
    return rx.vstack(create_announcement())
