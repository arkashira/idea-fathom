import pytest
from src.dashboard import Dashboard
from src.ideas import IdeaManager, IdeaStatus

def test_display_ideas_with_ideas_prints_correct_output():
    manager = IdeaManager()
    manager.add_idea("user1", "Idea1", "Desc1", IdeaStatus.DRAFT)
    dashboard = Dashboard(manager)
    import io
    import sys
    captured = io.StringIO()
    sys.stdout = captured
    dashboard.display_ideas("user1")
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "Your Ideas:" in output
    assert "ID: 1, Title: Idea1, Status: Draft, Description: Desc1" in output

def test_display_ideas_with_no_ideas_prints_message():
    manager = IdeaManager()
    dashboard = Dashboard(manager)
    import io
    import sys
    captured = io.StringIO()
    sys.stdout = captured
    dashboard.display_ideas("user1")
    sys.stdout = sys.__stdout__
    output = captured.getvalue()
    assert "No ideas found for this user." in output
