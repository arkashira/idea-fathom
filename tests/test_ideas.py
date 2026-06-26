import pytest
from src.ideas import IdeaManager, Idea, IdeaStatus

def test_add_idea_returns_correct_id():
    manager = IdeaManager()
    idea_id = manager.add_idea("user1", "Test Idea", "A test idea description", IdeaStatus.DRAFT)
    assert idea_id == 1

def test_get_all_ideas_returns_correct_user_ideas():
    manager = IdeaManager()
    manager.add_idea("user1", "Idea1", "Desc1", IdeaStatus.DRAFT)
    manager.add_idea("user2", "Idea2", "Desc2", IdeaStatus.DRAFT)
    ideas = manager.get_all_ideas("user1")
    assert len(ideas) == 1
    assert ideas[0].title == "Idea1"

def test_update_status_works():
    manager = IdeaManager()
    manager.add_idea("user1", "Idea1", "Desc1", IdeaStatus.DRAFT)
    assert manager.update_status(1, IdeaStatus.IN_IDEATION)
    idea = manager.ideas[1]
    assert idea.status == IdeaStatus.IN_IDEATION

def test_update_status_fails_for_nonexistent_idea():
    manager = IdeaManager()
    assert not manager.update_status(1, IdeaStatus.IN_IDEATION)
