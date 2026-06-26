import csv
import io

import pytest

from idea_fathom import IdeaFathomDashboard


@pytest.fixture
def dashboard():
    return IdeaFathomDashboard()


def test_add_idea_increments_total(dashboard):
    assert dashboard.total_ideas() == 0
    id1 = dashboard.add_idea("First idea")
    assert isinstance(id1, int)
    assert dashboard.total_ideas() == 1
    id2 = dashboard.add_idea("Second idea")
    assert dashboard.total_ideas() == 2
    # Ensure ids are unique
    assert id1 != id2


def test_validate_idea_updates_counts_and_average(dashboard):
    id1 = dashboard.add_idea("Idea A")
    id2 = dashboard.add_idea("Idea B")
    # No validated ideas yet
    assert dashboard.validated_ideas() == 0
    assert dashboard.average_validation_score() == 0.0

    dashboard.validate_idea(id1, 8.0)
    assert dashboard.validated_ideas() == 1
    assert dashboard.average_validation_score() == 8.0

    dashboard.validate_idea(id2, 4.0)
    assert dashboard.validated_ideas() == 2
    assert dashboard.average_validation_score() == pytest.approx((8.0 + 4.0) / 2)


def test_average_when_none_validated_returns_zero(dashboard):
    dashboard.add_idea("Lonely idea")
    assert dashboard.validated_ideas() == 0
    assert dashboard.average_validation_score() == 0.0


def test_export_csv_structure_and_content(dashboard):
    id1 = dashboard.add_idea("Alpha")
    id2 = dashboard.add_idea("Beta")
    dashboard.validate_idea(id2, 5.5)

    csv_text = dashboard.export_csv()
    f = io.StringIO(csv_text)
    reader = csv.reader(f)
    rows = list(reader)

    # Header + two data rows
    assert rows[0] == ["id", "title", "validated", "validation_score"]
    # Row order corresponds to insertion order (dict preserves order in py3.7+)
    assert rows[1] == [str(id1), "Alpha", "False", ""]
    assert rows[2] == [str(id2), "Beta", "True", "5.50"]


def test_validate_nonexistent_idea_raises_key_error(dashboard):
    with pytest.raises(KeyError) as exc:
        dashboard.validate_idea(999, 3.0)
    assert "Idea id 999 not found" in str(exc.value)


def test_validate_negative_score_raises_value_error(dashboard):
    iid = dashboard.add_idea("NegScore")
    with pytest.raises(ValueError) as exc:
        dashboard.validate_idea(iid, -1.0)
    assert "must be non‑negative" in str(exc.value)


def test_add_idea_requires_nonempty_title(dashboard):
    with pytest.raises(ValueError):
        dashboard.add_idea("")
    with pytest.raises(ValueError):
        dashboard.add_idea(123)  # type: ignore
