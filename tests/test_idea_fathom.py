import pytest
from idea_fathom import Idea, IdeaFathom

def test_validate_idea_duplicate():
    knowledge_base = [Idea("Concept 1", 100, 5)]
    idea_fathom = IdeaFathom(knowledge_base)
    new_idea = Idea("Concept 1", 200, 10)
    validation_result = idea_fathom.validate_idea(new_idea)
    assert not validation_result["valid"]
    assert validation_result["reason"] == "Duplicate concept"

def test_validate_idea_valid():
    knowledge_base = []
    idea_fathom = IdeaFathom(knowledge_base)
    new_idea = Idea("Concept 3", 300, 15)
    validation_result = idea_fathom.validate_idea(new_idea)
    assert validation_result["valid"]
    assert validation_result["metrics"]["market_size"] == 300
    assert validation_result["metrics"]["competition"] == 15

def test_add_idea_to_knowledge_base():
    knowledge_base = []
    idea_fathom = IdeaFathom(knowledge_base)
    new_idea = Idea("Concept 3", 300, 15)
    idea_fathom.add_idea_to_knowledge_base(new_idea)
    assert len(idea_fathom.knowledge_base) == 1
    assert idea_fathom.knowledge_base[0].concept == "Concept 3"

def test_validate_idea_invalid_market_size():
    knowledge_base = []
    idea_fathom = IdeaFathom(knowledge_base)
    new_idea = Idea("Concept 3", 0, 15)
    validation_result = idea_fathom.validate_idea(new_idea)
    assert not validation_result["valid"]

def test_validate_idea_invalid_competition():
    knowledge_base = []
    idea_fathom = IdeaFathom(knowledge_base)
    new_idea = Idea("Concept 3", 300, 0)
    validation_result = idea_fathom.validate_idea(new_idea)
    assert not validation_result["valid"]
